import {
  ButtonItem,
  PanelSection,
  PanelSectionRow,
  TextField,
} from "@decky/ui";
import { toaster } from "@decky/api";
import { FC, useState } from "react";

export const SETTINGS_ROUTE = "/decky-romm-client-settings";

export const SettingsPage: FC = () => {
  const [rommUrl, setRommUrl] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const onSave = () => {
    // TODO: persist settings to backend
    console.log("Saving settings:", { rommUrl, username, password });
    toaster.toast({
      title: "Settings saved",
      body: "Your RomM connection settings have been saved.",
    });
  };

  return (
    <div
      style={{
        marginTop: "40px",
        height: "calc(100% - 40px)",
        overflow: "auto",
      }}
    >
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
    </div>
  );
};
