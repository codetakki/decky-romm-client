import { describe, it, expect, vi, beforeEach } from "vitest";
import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { callableMocks, toaster } from "@decky/api";
import { SettingsPage } from "../Settings";

describe("SettingsPage", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    // Reset each route mock to the default (resolve undefined) rather than replacing.
    // This preserves the references held by module-level variables in Settings.tsx.
    for (const mock of Object.values(callableMocks)) {
      mock.mockReset();
      mock.mockResolvedValue(undefined);
    }
  });

  it("shows loading state then renders fields after settings load", async () => {
    render(<SettingsPage />);

    await waitFor(() => {
      expect(screen.getByLabelText("RomM URL")).toBeInTheDocument();
    });
    expect(screen.getByLabelText("Username")).toBeInTheDocument();
    expect(screen.getByLabelText("Password")).toBeInTheDocument();
  });

  it("renders the save button after loading", async () => {
    render(<SettingsPage />);

    await waitFor(() => {
      expect(screen.getByText("Save")).toBeInTheDocument();
    });
  });

  it("loads persisted settings from backend on mount", async () => {
    // Configure the existing getSetting mock to return saved values
    callableMocks["settings_getSetting"].mockImplementation(
      async (key: string) => {
        const values: Record<string, string> = {
          rommUrl: "http://192.168.1.50:8080",
          username: "admin",
          password: "secret123",
        };
        return values[key] ?? "";
      },
    );

    render(<SettingsPage />);

    await waitFor(() => {
      const urlInput = screen.getByLabelText("RomM URL") as HTMLInputElement;
      expect(urlInput.value).toBe("http://192.168.1.50:8080");
    });

    expect(
      (screen.getByLabelText("Username") as HTMLInputElement).value,
    ).toBe("admin");
    expect(
      (screen.getByLabelText("Password") as HTMLInputElement).value,
    ).toBe("secret123");
  });

  it("allows typing into the URL field", async () => {
    const user = userEvent.setup();
    render(<SettingsPage />);

    await waitFor(() => {
      expect(screen.getByLabelText("RomM URL")).toBeInTheDocument();
    });

    const urlInput = screen.getByLabelText("RomM URL") as HTMLInputElement;
    await user.type(urlInput, "http://192.168.1.100:8080");

    expect(urlInput.value).toBe("http://192.168.1.100:8080");
  });

  it("allows typing into the username field", async () => {
    const user = userEvent.setup();
    render(<SettingsPage />);

    await waitFor(() => {
      expect(screen.getByLabelText("Username")).toBeInTheDocument();
    });

    const usernameInput = screen.getByLabelText("Username") as HTMLInputElement;
    await user.type(usernameInput, "testuser");

    expect(usernameInput.value).toBe("testuser");
  });

  it("renders password field as password type", async () => {
    render(<SettingsPage />);

    await waitFor(() => {
      expect(screen.getByLabelText("Password")).toBeInTheDocument();
    });

    const passwordInput = screen.getByLabelText("Password") as HTMLInputElement;
    expect(passwordInput.type).toBe("password");
  });

  it("saves settings to backend and shows toast on save", async () => {
    const user = userEvent.setup();
    render(<SettingsPage />);

    await waitFor(() => {
      expect(screen.getByText("Save")).toBeInTheDocument();
    });

    // Type some values
    await user.type(screen.getByLabelText("RomM URL"), "http://myromm:8080");
    await user.type(screen.getByLabelText("Username"), "deck");
    await user.type(screen.getByLabelText("Password"), "pass");

    await user.click(screen.getByText("Save"));

    // Verify setSetting was called for each field
    await waitFor(() => {
      expect(callableMocks["settings_setSetting"]).toHaveBeenCalledWith(
        "rommUrl",
        "http://myromm:8080",
      );
    });
    expect(callableMocks["settings_setSetting"]).toHaveBeenCalledWith(
      "username",
      "deck",
    );
    expect(callableMocks["settings_setSetting"]).toHaveBeenCalledWith(
      "password",
      "pass",
    );

    // Verify commit was called
    expect(callableMocks["settings_commit"]).toHaveBeenCalled();

    // Verify success toast
    expect(toaster.toast).toHaveBeenCalledWith(
      expect.objectContaining({
        title: "Settings saved",
      }),
    );
  });

  it("shows error toast if save fails", async () => {
    const user = userEvent.setup();

    // Make setSetting reject
    callableMocks["settings_setSetting"].mockRejectedValue(
      new Error("disk full"),
    );

    render(<SettingsPage />);

    await waitFor(() => {
      expect(screen.getByText("Save")).toBeInTheDocument();
    });

    await user.click(screen.getByText("Save"));

    await waitFor(() => {
      expect(toaster.toast).toHaveBeenCalledWith(
        expect.objectContaining({
          title: "Error",
        }),
      );
    });
  });
});
