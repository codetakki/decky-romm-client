import { describe, it, expect, vi, beforeEach } from "vitest";
import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { toaster } from "@decky/api";
import { callableMocks, resetCallableMocks } from "./decky-api-helpers";
import { LibraryPage, RomCard, type RomSearchResult } from "../Library";

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

function makeRom(overrides: Partial<RomSearchResult> = {}): RomSearchResult {
  return {
    id: 1,
    name: "Super Mario Bros",
    platform_id: 10,
    platform_name: "NES",
    platform_slug: "nes",
    file_name: "super_mario_bros.nes",
    file_size_bytes: 40960,
    url_cover: "https://romm.example.com/covers/smb.jpg",
    ...overrides,
  };
}

const SAMPLE_RESULTS: RomSearchResult[] = [
  makeRom({ id: 1, name: "Super Mario Bros", platform_name: "NES" }),
  makeRom({ id: 2, name: "Zelda", platform_name: "NES", url_cover: null }),
  makeRom({ id: 3, name: "Sonic", platform_name: "Genesis", platform_slug: "genesis" }),
];

// ---------------------------------------------------------------------------
// Tests
// ---------------------------------------------------------------------------

describe("LibraryPage", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    resetCallableMocks();
  });

  it("renders the search field and button", () => {
    render(<LibraryPage />);

    expect(screen.getByLabelText("Search ROMs")).toBeInTheDocument();
    expect(screen.getByText("Search")).toBeInTheDocument();
  });

  it("search button is disabled when input is empty", () => {
    render(<LibraryPage />);

    const btn = screen.getByText("Search");
    expect(btn).toBeDisabled();
  });

  it("enables search button when query is entered", async () => {
    const user = userEvent.setup();
    render(<LibraryPage />);

    await user.type(screen.getByLabelText("Search ROMs"), "mario");

    expect(screen.getByText("Search")).not.toBeDisabled();
  });

  it("calls search_roms backend and displays results", async () => {
    callableMocks["search_roms"].mockResolvedValue(SAMPLE_RESULTS);

    const user = userEvent.setup();
    render(<LibraryPage />);

    await user.type(screen.getByLabelText("Search ROMs"), "mario");
    await user.click(screen.getByText("Search"));

    // Wait for results to appear
    await waitFor(() => {
      expect(screen.getByText("Results (3)")).toBeInTheDocument();
    });

    // Verify all ROM cards rendered
    const cards = screen.getAllByTestId("rom-card");
    expect(cards).toHaveLength(3);

    // Verify backend was called with correct args
    expect(callableMocks["search_roms"]).toHaveBeenCalledWith("mario", 50);
  });

  it("displays ROM names and platform names in cards", async () => {
    callableMocks["search_roms"].mockResolvedValue(SAMPLE_RESULTS);

    const user = userEvent.setup();
    render(<LibraryPage />);

    await user.type(screen.getByLabelText("Search ROMs"), "test");
    await user.click(screen.getByText("Search"));

    await waitFor(() => {
      expect(screen.getByText("Super Mario Bros")).toBeInTheDocument();
    });
    expect(screen.getByText("Zelda")).toBeInTheDocument();
    expect(screen.getByText("Sonic")).toBeInTheDocument();

    // Platform names
    expect(screen.getAllByText("NES")).toHaveLength(2);
    expect(screen.getByText("Genesis")).toBeInTheDocument();
  });

  it("shows cover images for ROMs that have them", async () => {
    callableMocks["search_roms"].mockResolvedValue([
      makeRom({ id: 1, name: "With Cover", url_cover: "https://example.com/cover.jpg" }),
    ]);

    const user = userEvent.setup();
    render(<LibraryPage />);

    await user.type(screen.getByLabelText("Search ROMs"), "test");
    await user.click(screen.getByText("Search"));

    await waitFor(() => {
      const img = screen.getByAltText("With Cover") as HTMLImageElement;
      expect(img.src).toBe("https://example.com/cover.jpg");
    });
  });

  it("shows placeholder for ROMs without a cover", async () => {
    callableMocks["search_roms"].mockResolvedValue([
      makeRom({ id: 1, name: "No Cover ROM", url_cover: null }),
    ]);

    const user = userEvent.setup();
    render(<LibraryPage />);

    await user.type(screen.getByLabelText("Search ROMs"), "test");
    await user.click(screen.getByText("Search"));

    await waitFor(() => {
      const img = screen.getByAltText("No Cover ROM") as HTMLImageElement;
      expect(img.src).toContain("data:image/svg+xml");
    });
  });

  it("shows 'no results' message when search returns empty", async () => {
    callableMocks["search_roms"].mockResolvedValue([]);

    const user = userEvent.setup();
    render(<LibraryPage />);

    await user.type(screen.getByLabelText("Search ROMs"), "zzzznotfound");
    await user.click(screen.getByText("Search"));

    await waitFor(() => {
      expect(screen.getByText(/No ROMs found/)).toBeInTheDocument();
    });
  });

  it("shows error toast when search fails", async () => {
    callableMocks["search_roms"].mockRejectedValue(
      new Error("Connection refused"),
    );

    const user = userEvent.setup();
    render(<LibraryPage />);

    await user.type(screen.getByLabelText("Search ROMs"), "mario");
    await user.click(screen.getByText("Search"));

    await waitFor(() => {
      expect(toaster.toast).toHaveBeenCalledWith(
        expect.objectContaining({ title: "Search failed" }),
      );
    });
  });

  it("shows 'Searching...' while request is in flight", async () => {
    // Create a promise we control to keep the search pending
    let resolveSearch!: (value: RomSearchResult[]) => void;
    callableMocks["search_roms"].mockImplementation(
      () => new Promise<RomSearchResult[]>((resolve) => { resolveSearch = resolve; }),
    );

    const user = userEvent.setup();
    render(<LibraryPage />);

    await user.type(screen.getByLabelText("Search ROMs"), "mario");
    await user.click(screen.getByText("Search"));

    // Should show searching state
    expect(screen.getByText("Searching...")).toBeInTheDocument();

    // Resolve and verify it goes back to normal
    resolveSearch(SAMPLE_RESULTS);
    await waitFor(() => {
      expect(screen.getByText("Results (3)")).toBeInTheDocument();
    });
  });
});

// ---------------------------------------------------------------------------
// RomCard unit tests
// ---------------------------------------------------------------------------

describe("RomCard", () => {
  it("renders name and platform", () => {
    const rom = makeRom({ name: "Tetris", platform_name: "Game Boy" });
    render(<RomCard rom={rom} />);

    expect(screen.getByText("Tetris")).toBeInTheDocument();
    expect(screen.getByText("Game Boy")).toBeInTheDocument();
  });

  it("falls back to file_name when name is null", () => {
    const rom = makeRom({ name: null, file_name: "tetris.gb" });
    render(<RomCard rom={rom} />);

    expect(screen.getByText("tetris.gb")).toBeInTheDocument();
  });

  it("renders the cover image with correct src", () => {
    const rom = makeRom({ url_cover: "https://example.com/cover.png" });
    render(<RomCard rom={rom} />);

    const img = screen.getByRole("img") as HTMLImageElement;
    expect(img.src).toBe("https://example.com/cover.png");
  });

  it("uses placeholder when url_cover is null", () => {
    const rom = makeRom({ url_cover: null });
    render(<RomCard rom={rom} />);

    const img = screen.getByRole("img") as HTMLImageElement;
    expect(img.src).toContain("data:image/svg+xml");
  });
});
