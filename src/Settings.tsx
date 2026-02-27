import {
  ButtonItem,
  PanelSection,
  PanelSectionRow,
  TextField,
} from "@decky/ui";
import { callable, toaster } from "@decky/api";
import { FC, useEffect, useState } from "react";

// Python backend bridge functions
const getSetting = callable<[key: string, defaults: unknown], unknown>(
  "settings_getSetting",
);
const setSetting = callable<[key: string, value: unknown], void>(
  "settings_setSetting",
);
const commitSettings = callable<[], void>("settings_commit");

export const SETTINGS_ROUTE = "/decky-romm-client-settings";

export const SettingsPage: FC = () => {
  const [rommUrl, setRommUrl] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(true);

  // Load persisted settings on mount
  useEffect(() => {
    (async () => {
      try {
        const [url, user, pass] = await Promise.all([
          getSetting("rommUrl", ""),
          getSetting("username", ""),
          getSetting("password", ""),
        ]);
        setRommUrl((url as string) ?? "");
        setUsername((user as string) ?? "");
        setPassword((pass as string) ?? "");
      } catch (e) {
        console.error("Failed to load settings:", e);
      } finally {
        setLoading(false);
      }
    })();
  }, []);

  const onSave = async () => {
    try {
      await setSetting("rommUrl", rommUrl);
      await setSetting("username", username);
      await setSetting("password", password);
      await commitSettings();
      toaster.toast({
        title: "Settings saved",
        body: "Your RomM connection settings have been saved.",
      });
    } catch (e) {
      console.error("Failed to save settings:", e);
      toaster.toast({
        title: "Error",
        body: "Failed to save settings. Check the logs for details.",
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
      {loading ? (
        <PanelSection title="Loading...">
          <PanelSectionRow>Loading settings...</PanelSectionRow>
        </PanelSection>
      ) : (
        <>
          <PanelSection title="RomM Connection">
            <PanelSectionRow>
              <TextField
                label="RomM URL"
                description="e.g. http://192.168.1.100:8080"
                value={rommUrl}
                onChange={(e) => setRommUrl(e.target.value)}
              />
            </PanelSectionRow>

            <PanelSectionRow>
              <TextField
                label="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />
            </PanelSectionRow>

            <PanelSectionRow>
              <TextField
                label="Password"
                bIsPassword
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </PanelSectionRow>
          </PanelSection>

          <PanelSection>
            <PanelSectionRow>
              <ButtonItem layout="below" onClick={onSave}>
                Save
              </ButtonItem>
            </PanelSectionRow>
          </PanelSection>
        </>
      )}
    </div>
  );
};
