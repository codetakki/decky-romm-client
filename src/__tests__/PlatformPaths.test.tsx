import { describe, it, expect, vi, beforeEach } from "vitest";
import { render, screen, waitFor, fireEvent } from "@testing-library/react";
import { toaster, openFilePicker } from "@decky/api";
import { callableMocks, resetCallableMocks } from "./decky-api-helpers";
import { PlatformPathsPage } from "../PlatformPaths";

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

const mockPlatforms = [
  {
    id: 1,
    name: "snes",
    slug: "snes",
    fs_slug: "snes",
    display_name: "Super Nintendo",
    rom_count: 42,
    url_logo: null,
  },
  {
    id: 2,
    name: "gba",
    slug: "gba",
    fs_slug: "gba",
    display_name: "Game Boy Advance",
    rom_count: 18,
    url_logo: "http://example.com/gba.png",
  },
  {
    id: 3,
    name: "n64",
    slug: "n64",
    fs_slug: "n64",
    display_name: "Nintendo 64",
    rom_count: 10,
    url_logo: null,
  },
  {
    id: 4,
    name: "psx",
    slug: "psx",
    fs_slug: "psx",
    display_name: "PlayStation",
    rom_count: 0,
    url_logo: null,
  },
];

// ---------------------------------------------------------------------------
// Tests
// ---------------------------------------------------------------------------

describe("PlatformPathsPage", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    resetCallableMocks();

    // Default mocks
    callableMocks["get_platforms"].mockResolvedValue(mockPlatforms);
    callableMocks["settings_getSetting"].mockResolvedValue({});
    callableMocks["settings_setSetting"].mockResolvedValue(undefined);
    callableMocks["settings_commit"].mockResolvedValue(undefined);
  });

  it("shows loading state initially", () => {
    // Make platforms hang
    callableMocks["get_platforms"].mockImplementation(() => new Promise(() => {}));

    render(<PlatformPathsPage />);
    expect(screen.getByText(/loading platforms/i)).toBeTruthy();
  });

  it("renders all non-empty platforms from RomM by default", async () => {
    render(<PlatformPathsPage />);

    await waitFor(() => {
      expect(screen.getByText(/Super Nintendo \(42\)/)).toBeTruthy();
    });

    expect(screen.getByText(/Game Boy Advance \(18\)/)).toBeTruthy();
    expect(screen.getByText(/Nintendo 64 \(10\)/)).toBeTruthy();
    expect(screen.queryByText(/PlayStation/)).toBeNull(); // filtered by default
  });

  it("shows empty platforms when toggle is unchecked", async () => {
    render(<PlatformPathsPage />);

    await waitFor(() => {
      expect(screen.getByText(/Super Nintendo/)).toBeTruthy();
    });

    const toggle = screen.getByLabelText(/Hide platforms with no games/i);
    fireEvent.click(toggle);

    await waitFor(() => {
      expect(screen.getByText(/PlayStation \(0\)/)).toBeTruthy();
    });
  });

  it("filters platforms based on search query", async () => {
    render(<PlatformPathsPage />);

    await waitFor(() => {
      expect(screen.getByText(/Super Nintendo/)).toBeTruthy();
    });

    const searchInput = screen.getByLabelText(/Search Platforms/i);
    fireEvent.change(searchInput, { target: { value: "Advance" } });

    await waitFor(() => {
      expect(screen.getByText(/Game Boy Advance/)).toBeTruthy();
      expect(screen.queryByText(/Super Nintendo/)).toBeNull();
    });
  });

  it("shows 'Not configured' when no path is set", async () => {
    render(<PlatformPathsPage />);

    await waitFor(() => {
      expect(screen.getByText(/Super Nintendo/)).toBeTruthy();
    });

    const notConfigured = screen.getAllByText("Not configured");
    expect(notConfigured.length).toBe(3);
  });

  it("loads saved platform paths from settings", async () => {
    callableMocks["settings_getSetting"].mockResolvedValue({
      snes: "/roms/snes",
      gba: "/roms/gba",
    });

    render(<PlatformPathsPage />);

    await waitFor(() => {
      expect(screen.getByText("/roms/snes")).toBeTruthy();
    });
    expect(screen.getByText("/roms/gba")).toBeTruthy();
    // n64 has no saved path
    expect(screen.getByText("Not configured")).toBeTruthy();
  });

  it("calls openFilePicker when Browse is clicked", async () => {
    const mockFilePicker = openFilePicker as ReturnType<typeof vi.fn>;
    mockFilePicker.mockResolvedValue({
      path: "/mnt/roms/snes",
      realpath: "/mnt/roms/snes",
    });

    render(<PlatformPathsPage />);

    await waitFor(() => {
      expect(screen.getByText(/Super Nintendo/)).toBeTruthy();
    });

    const browseButtons = screen.getAllByText("Browse");
    fireEvent.click(browseButtons[0]);

    await waitFor(() => {
      expect(mockFilePicker).toHaveBeenCalledWith(
        1, // FOLDER
        "/home",
        false,
        true,
      );
    });

    await waitFor(() => {
      expect(screen.getByText("/mnt/roms/snes")).toBeTruthy();
    });
  });

  it("uses existing path as start path for file picker", async () => {
    callableMocks["settings_getSetting"].mockResolvedValue({
      snes: "/existing/snes/path",
    });
    const mockFilePicker = openFilePicker as ReturnType<typeof vi.fn>;
    mockFilePicker.mockResolvedValue({
      path: "/new/path",
      realpath: "/new/path",
    });

    render(<PlatformPathsPage />);

    await waitFor(() => {
      expect(screen.getByText("/existing/snes/path")).toBeTruthy();
    });

    const browseButtons = screen.getAllByText("Browse");
    fireEvent.click(browseButtons[0]); // SNES is first

    await waitFor(() => {
      expect(mockFilePicker).toHaveBeenCalledWith(
        1,
        "/existing/snes/path",
        false,
        true,
      );
    });
  });

  it("clears a platform path when Clear is clicked", async () => {
    callableMocks["settings_getSetting"].mockResolvedValue({
      snes: "/roms/snes",
    });

    render(<PlatformPathsPage />);

    await waitFor(() => {
      expect(screen.getByText("/roms/snes")).toBeTruthy();
    });

    const clearButton = screen.getByText("Clear");
    fireEvent.click(clearButton);

    await waitFor(() => {
      const notConfigured = screen.getAllByText("Not configured");
      expect(notConfigured.length).toBe(3);
    });
  });

  it("saves all platform paths when Save is clicked", async () => {
    callableMocks["settings_getSetting"].mockResolvedValue({
      snes: "/roms/snes",
      gba: "/roms/gba",
    });

    render(<PlatformPathsPage />);

    await waitFor(() => {
      expect(screen.getByText(/Super Nintendo/)).toBeTruthy();
    });

    const saveButton = screen.getByText("Save All Paths");
    fireEvent.click(saveButton);

    await waitFor(() => {
      expect(callableMocks["settings_setSetting"]).toHaveBeenCalledWith(
        "platformPaths",
        { snes: "/roms/snes", gba: "/roms/gba" },
      );
      expect(callableMocks["settings_commit"]).toHaveBeenCalled();
    });
  });

  it("shows error toast when save fails", async () => {
    callableMocks["settings_setSetting"].mockRejectedValue(new Error("Save failed"));

    render(<PlatformPathsPage />);

    await waitFor(() => {
      expect(screen.getByText(/Super Nintendo/)).toBeTruthy();
    });

    fireEvent.click(screen.getByText("Save All Paths"));

    await waitFor(() => {
      expect(toaster.toast).toHaveBeenCalledWith(
        expect.objectContaining({ title: "Error" }),
      );
    });
  });

  it("shows success toast when save succeeds", async () => {
    callableMocks["settings_getSetting"].mockResolvedValue({
      snes: "/roms/snes",
    });

    render(<PlatformPathsPage />);

    await waitFor(() => {
      expect(screen.getByText(/Super Nintendo/)).toBeTruthy();
    });

    fireEvent.click(screen.getByText("Save All Paths"));

    await waitFor(() => {
      expect(toaster.toast).toHaveBeenCalledWith(
        expect.objectContaining({ title: "Platform paths saved" }),
      );
    });
  });

  it("shows error state when platforms fail to load", async () => {
    callableMocks["get_platforms"].mockRejectedValue(new Error("Connection refused"));

    render(<PlatformPathsPage />);

    await waitFor(() => {
      expect(screen.getByText(/Connection refused/)).toBeTruthy();
    });

    expect(screen.getByText("Retry")).toBeTruthy();
  });

  it("shows no platforms message when server returns empty list", async () => {
    callableMocks["get_platforms"].mockResolvedValue([]);

    render(<PlatformPathsPage />);

    await waitFor(() => {
      expect(screen.getByText(/No platforms found/i)).toBeTruthy();
    });
  });

  it("renders a Browse button for each platform", async () => {
    render(<PlatformPathsPage />);

    await waitFor(() => {
      expect(screen.getByText(/Super Nintendo/)).toBeTruthy();
    });

    const browseButtons = screen.getAllByText("Browse");
    expect(browseButtons.length).toBe(3);
  });

  it("handles file picker cancellation gracefully", async () => {
    const mockFilePicker = openFilePicker as ReturnType<typeof vi.fn>;
    mockFilePicker.mockRejectedValue(new Error("User cancelled"));

    render(<PlatformPathsPage />);

    await waitFor(() => {
      expect(screen.getByText(/Super Nintendo/)).toBeTruthy();
    });

    const browseButtons = screen.getAllByText("Browse");
    fireEvent.click(browseButtons[0]);

    // Should not crash — path remains "Not configured"
    await waitFor(() => {
      const notConfigured = screen.getAllByText("Not configured");
      expect(notConfigured.length).toBe(3);
    });
  });
});
