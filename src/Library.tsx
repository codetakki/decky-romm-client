import {
  ButtonItem,
  Focusable,
  PanelSection,
  PanelSectionRow,
  TextField,
} from "@decky/ui";
import { callable, openFilePicker, toaster } from "@decky/api";
import { FC, useCallback, useState } from "react";

// FileSelectionType enum values from @decky/api
const FileSelectionType = { FILE: 0, FOLDER: 1 } as const;

/** Shape returned by the Python `search_roms` backend method. */
export interface RomSearchResult {
  id: number;
  name: string | null;
  platform_id: number;
  platform_name: string;
  platform_slug: string;
  file_name: string;
  file_size_bytes: number;
  url_cover: string | null;
}

// Python backend bridge
const searchRoms = callable<[search_term: string, limit: number], RomSearchResult[]>(
  "search_roms",
);
const getSetting = callable<[key: string, defaults: unknown], unknown>(
  "settings_getSetting",
);
const setSetting = callable<[key: string, value: unknown], void>(
  "settings_setSetting",
);
const commitSettings = callable<[], void>("settings_commit");

export const LIBRARY_ROUTE = "/decky-romm-client-library";

export const LibraryPage: FC = () => {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<RomSearchResult[]>([]);
  const [searching, setSearching] = useState(false);
  const [searched, setSearched] = useState(false);

  const onSearch = useCallback(async () => {
    if (!query.trim()) return;
    setSearching(true);
    setSearched(false);
    try {
      const roms = await searchRoms(query.trim(), 50);
      setResults(roms ?? []);
    } catch (e) {
      console.error("ROM search failed:", e);
      toaster.toast({
        title: "Search failed",
        body: String(e),
      });
      setResults([]);
    } finally {
      setSearching(false);
      setSearched(true);
    }
  }, [query]);

  const handleSelectRom = async (rom: RomSearchResult) => {
    try {
      let paths = (await getSetting("platformPaths", {})) as Record<string, string>;
      let path = paths[rom.platform_slug];

      if (!path) {
        toaster.toast({
          title: "Setup Required",
          body: `Please select a download folder for ${rom.platform_name}.`,
        });

        const result = await openFilePicker(
          FileSelectionType.FOLDER,
          "/home",
          false,
          true
        );

        if (result?.path) {
          path = result.path;
          paths = { ...paths, [rom.platform_slug]: path };
          await setSetting("platformPaths", paths);
          await commitSettings();
          toaster.toast({
            title: "Path Saved",
            body: `Folder set for ${rom.platform_name}`,
          });
        } else {
          return; // user cancelled file picker
        }
      }

      toaster.toast({
        title: "Ready to download",
        body: `Will download to: ${path}`, // Placeholder until actual download is implemented
      });
    } catch (e) {
      console.error("Error setting download path:", e);
      toaster.toast({
        title: "Error",
        body: "Failed to configure download path.",
      });
    }
  };

  return (
    <div
      style={{
        marginTop: "40px",
        height: "calc(100% - 40px)",
        overflow: "auto",
      }}
    >
      <PanelSection title="ROM Library">
        <PanelSectionRow>
          <TextField
            label="Search ROMs"
            description="Search by title"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
        </PanelSectionRow>
        <PanelSectionRow>
          <ButtonItem layout="below" onClick={onSearch} disabled={searching || !query.trim()}>
            {searching ? "Searching..." : "Search"}
          </ButtonItem>
        </PanelSectionRow>
      </PanelSection>

      {searched && results.length === 0 && (
        <PanelSection title="No Results">
          <PanelSectionRow>No ROMs found for &quot;{query}&quot;.</PanelSectionRow>
        </PanelSection>
      )}

      {results.length > 0 && (
        <PanelSection title={`Results (${results.length})`}>
          <Focusable
            style={{
              display: "grid",
              gridTemplateColumns: "repeat(auto-fill, minmax(120px, 1fr))",
              gap: "12px",
              padding: "8px 0",
            }}
          >
            {results.map((rom) => (
              <RomCard key={rom.id} rom={rom} onSelect={handleSelectRom} />
            ))}
          </Focusable>
        </PanelSection>
      )}
    </div>
  );
};

/* -------------------------------------------------------------------------- */
/*  ROM Card                                                                  */
/* -------------------------------------------------------------------------- */

const PLACEHOLDER_COVER =
  "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='160' fill='%23333'%3E%3Crect width='120' height='160'/%3E%3Ctext x='50%25' y='50%25' fill='%23888' font-size='12' text-anchor='middle' dy='.3em'%3ENo Cover%3C/text%3E%3C/svg%3E";

export const RomCard: FC<{ rom: RomSearchResult; onSelect: (rom: RomSearchResult) => void }> = ({ rom, onSelect }) => {
  const coverUrl = rom.url_cover ?? PLACEHOLDER_COVER;

  return (
    <Focusable
      data-testid="rom-card"
      onClick={() => onSelect(rom)}
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        textAlign: "center",
        cursor: "pointer",
        padding: "8px",
        borderRadius: "4px",
      }}
    >
      <img
        src={coverUrl}
        alt={rom.name ?? rom.file_name}
        style={{
          width: "120px",
          height: "160px",
          objectFit: "cover",
          borderRadius: "4px",
          backgroundColor: "#222",
        }}
      />
      <span
        style={{
          marginTop: "4px",
          fontSize: "12px",
          maxWidth: "120px",
          overflow: "hidden",
          textOverflow: "ellipsis",
          whiteSpace: "nowrap",
          display: "block",
        }}
        title={rom.name ?? rom.file_name}
      >
        {rom.name ?? rom.file_name}
      </span>
      <span style={{ fontSize: "10px", color: "#aaa" }}>
        {rom.platform_name}
      </span>
    </Focusable>
  );
};
