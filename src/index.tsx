import {
  ButtonItem,
  Navigation,
  PanelSection,
  PanelSectionRow,
  staticClasses
} from "@decky/ui";
import {
  callable,
  definePlugin,
  toaster,
  routerHook,
} from "@decky/api"
import { FaShip } from "react-icons/fa";
import { SettingsPage, SETTINGS_ROUTE } from "./Settings";
import { LibraryPage, LIBRARY_ROUTE } from "./Library";

function Content() {
  return (
    <>
      <PanelSection title="RomM Client">
        <PanelSectionRow>
          <ButtonItem
            layout="below"
            onClick={() => {
              Navigation.Navigate(LIBRARY_ROUTE);
              Navigation.CloseSideMenus();
            }}
          >
            ROM Library
          </ButtonItem>
        </PanelSectionRow>
        <PanelSectionRow>
          <ButtonItem
            layout="below"
            onClick={() => {
              Navigation.Navigate(SETTINGS_ROUTE);
              Navigation.CloseSideMenus();
            }}
          >
            Settings
          </ButtonItem>
        </PanelSectionRow>
      </PanelSection>
    </>
  );
};

export default definePlugin(() => {
  console.log("RomM Client plugin initializing")

  routerHook.addRoute(SETTINGS_ROUTE, SettingsPage, { exact: true });
  routerHook.addRoute(LIBRARY_ROUTE, LibraryPage, { exact: true });

  return {
    name: "RomM Client",
    titleView: <div className={staticClasses.Title}>RomM Client</div>,
    // The content of your plugin's menu
    content: <Content />,
    // The icon displayed in the plugin list
    icon: <FaShip />,
    // The function triggered when your plugin unloads
    onDismount() {
      routerHook.removeRoute(SETTINGS_ROUTE);
      routerHook.removeRoute(LIBRARY_ROUTE);
    },
  };
});
