import {
  ButtonItem,
  Focusable,
  Navigation,
  PanelSection,
  PanelSectionRow,
  Field,
  ScrollPanelGroup,
  TextField,
  ToggleField,
} from "@decky/ui";
import { callable, openFilePicker, toaster } from "@decky/api";
import { FC, useEffect, useState } from "react";

// FileSelectionType enum values from @decky/api
const FileSelectionType = { FILE: 0, FOLDER: 1 } as const;

// Python backend bridge functions
const getPlatforms = callable<[], Platform[]>("get_platforms");
const getSetting = callable<[key: string, defaults: unknown], unknown>(
  "settings_getSetting",
);
const setSetting = callable<[key: string, value: unknown], void>(
  "settings_setSetting",
);
const commitSettings = callable<[], void>("settings_commit");

export const PLATFORM_PATHS_ROUTE = "/decky-romm-client-platform-paths";

interface Platform {
  id: number;
  name: string;
  slug: string;
  fs_slug: string;
  display_name: string;
  rom_count: number;
  url_logo: string | null;
}

/** Mapping of platform slug → local directory path */
type PlatformPathMap = Record<string, string>;

export const PlatformPathsPage: FC = () => {
  const [platforms, setPlatforms] = useState<Platform[]>([]);
  const [pathMap, setPathMap] = useState<PlatformPathMap>({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [searchQuery, setSearchQuery] = useState("");
  const [hideEmpty, setHideEmpty] = useState(true);

  // Load platforms from RomM and saved path mappings on mount
  useEffect(() => {
    (async () => {
      try {
        const [platformList, savedPaths] = await Promise.all([
          getPlatforms(),
          getSetting("platformPaths", {}) as Promise<PlatformPathMap>,
        ]);
        setPlatforms(platformList);
        setPathMap((savedPaths as PlatformPathMap) ?? {});
      } catch (e) {
        const msg = e instanceof Error ? e.message : String(e);
        console.error("Failed to load platforms:", msg);
        setError(msg);
      } finally {
        setLoading(false);
      }
    })();
  }, []);

  const browsePath = async (platformSlug: string, currentPath: string) => {
    try {
      const result = await openFilePicker(
        FileSelectionType.FOLDER,
        currentPath || "/home",
        false,  // includeFiles
        true,   // includeFolders
      );
      if (result?.path) {
        setPathMap((prev) => ({ ...prev, [platformSlug]: result.path }));
      }
    } catch (e) {
      console.error("File picker cancelled or failed:", e);
    }
  };

  const onSave = async () => {
    try {
      await setSetting("platformPaths", pathMap);
      await commitSettings();
      toaster.toast({
        title: "Platform paths saved",
        body: `Saved download paths for ${Object.keys(pathMap).filter((k) => pathMap[k]).length} platform(s).`,
      });
    } catch (e) {
      console.error("Failed to save platform paths:", e);
      toaster.toast({
        title: "Error",
        body: "Failed to save platform paths. Check the logs for details.",
      });
    }
  };

  const onClear = (slug: string) => {
    setPathMap((prev) => {
      const next = { ...prev };
      delete next[slug];
      return next;
    });
  };

  const filteredPlatforms = platforms.filter((p) => {
    if (hideEmpty && p.rom_count === 0) return false;
    if (searchQuery.trim()) {
      const q = searchQuery.toLowerCase();
      return (
        p.name.toLowerCase().includes(q) ||
        p.display_name.toLowerCase().includes(q)
      );
    }
    return true;
  });

  return (
    <Focusable
      onCancelButton={() => Navigation.NavigateBack()}
      onCancelActionDescription="Back"
      style={{
        marginTop: "40px",
        height: "calc(100% - 40px)",
        overflow: "auto",
      }}
    >
      <ScrollPanelGroup>
        {loading ? (
          <PanelSection title="Loading...">
            <PanelSectionRow>Loading platforms from RomM...</PanelSectionRow>
          </PanelSection>
        ) : error ? (
          <PanelSection title="Error">
            <PanelSectionRow>
              {error}
            </PanelSectionRow>
            <PanelSectionRow>
              <ButtonItem layout="below" onClick={() => window.location.reload()}>
                Retry
              </ButtonItem>
            </PanelSectionRow>
          </PanelSection>
        ) : platforms.length === 0 ? (
          <PanelSection title="No Platforms">
            <PanelSectionRow>
              No platforms found on your RomM server. Add some ROMs first.
            </PanelSectionRow>
          </PanelSection>
        ) : (
          <>
            <PanelSection title="Platform Download Paths">
              <PanelSectionRow>
                <span style={{ fontSize: "12px", opacity: 0.7 }}>
                  Choose where ROMs for each platform should be saved after downloading.
                </span>
              </PanelSectionRow>
              <PanelSectionRow>
                <TextField
                  label="Search Platforms"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                />
              </PanelSectionRow>
              <PanelSectionRow>
                <ToggleField
                  label="Hide platforms with no games"
                  checked={hideEmpty}
                  onChange={(enabled) => setHideEmpty(enabled)}
                />
              </PanelSectionRow>
            </PanelSection>

            {filteredPlatforms.map((platform) => (
              <PanelSection
                key={platform.slug}
                title={`${platform.display_name} (${platform.rom_count})`}
              >
                <PanelSectionRow>
                  <Field
                    label="Download path"
                    description={pathMap[platform.slug] || "Not configured"}
                  >
                    <Focusable
                      style={{ display: "flex", gap: "8px" }}
                      flow-children="row"
                    >
                      <ButtonItem
                        layout="below"
                        onClick={() =>
                          browsePath(platform.slug, pathMap[platform.slug] || "")
                        }
                      >
                        Browse
                      </ButtonItem>
                      {pathMap[platform.slug] && (
                        <ButtonItem
                          layout="below"
                          onClick={() => onClear(platform.slug)}
                        >
                          Clear
                        </ButtonItem>
                      )}
                    </Focusable>
                  </Field>
                </PanelSectionRow>
              </PanelSection>
            ))}

            {filteredPlatforms.length === 0 && (
              <PanelSection>
                <PanelSectionRow>
                  No platforms match your search or filter criteria.
                </PanelSectionRow>
              </PanelSection>
            )}

            <PanelSection>
              <PanelSectionRow>
                <ButtonItem layout="below" onClick={onSave}>
                  Save All Paths
                </ButtonItem>
              </PanelSectionRow>
            </PanelSection>
          </>
        )}
      </ScrollPanelGroup>
    </Focusable>
  );
};
