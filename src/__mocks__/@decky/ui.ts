/**
 * Mock for @decky/ui
 *
 * Provides lightweight HTML-element-based stand-ins for Decky UI components.
 * These render real DOM so @testing-library queries work, but they carry no
 * Steam client dependencies.
 */
import React, { type FC, type ReactNode } from "react";
import { vi } from "vitest";

/* -------------------------------------------------------------------------- */
/*  Component helpers                                                         */
/* -------------------------------------------------------------------------- */

/** Utility to create a simple wrapper component */
function wrap(displayName: string, tag: keyof HTMLElementTagNameMap = "div") {
  const Comp: FC<Record<string, unknown> & { children?: ReactNode }> = ({
    children,
    ...rest
  }) => React.createElement(tag, { "data-testid": displayName, ...rest }, children);
  Comp.displayName = displayName;
  return Comp;
}

/* -------------------------------------------------------------------------- */
/*  Panel                                                                     */
/* -------------------------------------------------------------------------- */

export const PanelSection: FC<{
  title?: string;
  spinner?: boolean;
  children?: ReactNode;
}> = ({ title, children }) =>
  React.createElement(
    "div",
    { "data-testid": "PanelSection" },
    title ? React.createElement("h2", null, title) : null,
    children,
  );
PanelSection.displayName = "PanelSection";

export const PanelSectionRow: FC<{ children?: ReactNode }> = ({ children }) =>
  React.createElement("div", { "data-testid": "PanelSectionRow" }, children);
PanelSectionRow.displayName = "PanelSectionRow";

/* -------------------------------------------------------------------------- */
/*  Button / ButtonItem                                                       */
/* -------------------------------------------------------------------------- */

export const ButtonItem: FC<{
  layout?: string;
  onClick?: () => void;
  children?: ReactNode;
  disabled?: boolean;
}> = ({ children, onClick, disabled }) =>
  React.createElement(
    "button",
    { "data-testid": "ButtonItem", onClick, disabled },
    children,
  );
ButtonItem.displayName = "ButtonItem";

export const Button: FC<{
  onClick?: () => void;
  children?: ReactNode;
  disabled?: boolean;
}> = ({ children, onClick, disabled }) =>
  React.createElement(
    "button",
    { "data-testid": "Button", onClick, disabled },
    children,
  );
Button.displayName = "Button";

/* -------------------------------------------------------------------------- */
/*  TextField                                                                 */
/* -------------------------------------------------------------------------- */

export const TextField: FC<{
  label?: string;
  description?: string;
  value?: string;
  bIsPassword?: boolean;
  onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void;
}> = ({ label, description, value, bIsPassword, onChange }) =>
  React.createElement(
    "div",
    { "data-testid": "TextField" },
    label ? React.createElement("label", null, label) : null,
    description
      ? React.createElement("span", { className: "description" }, description)
      : null,
    React.createElement("input", {
      type: bIsPassword ? "password" : "text",
      value,
      onChange,
      "aria-label": label,
    }),
  );
TextField.displayName = "TextField";

/* -------------------------------------------------------------------------- */
/*  Other components (stubs)                                                  */
/* -------------------------------------------------------------------------- */

export const Dropdown = wrap("Dropdown");
export const SliderField = wrap("SliderField");

export const ToggleField: FC<{
  label?: string;
  checked?: boolean;
  onChange?: (checked: boolean) => void;
}> = ({ label, checked, onChange }) =>
  React.createElement(
    "div",
    { "data-testid": "ToggleField" },
    React.createElement(
      "label",
      null,
      label,
      React.createElement("input", {
        type: "checkbox",
        checked,
        onChange: (e: React.ChangeEvent<HTMLInputElement>) =>
          onChange && onChange(e.target.checked),
        "aria-label": label,
      }),
    ),
  );
ToggleField.displayName = "ToggleField";

export const Toggle = wrap("Toggle");
export const Focusable = wrap("Focusable");
export const Carousel = wrap("Carousel");
export const Spinner = wrap("Spinner");
export const SteamSpinner = wrap("SteamSpinner");
export const ProgressBar = wrap("ProgressBar");
export const Tabs = wrap("Tabs");
export const DialogButton = wrap("DialogButton", "button");
export const Field: FC<{
  label?: string;
  description?: ReactNode;
  children?: ReactNode;
}> = ({ label, description, children }) =>
  React.createElement(
    "div",
    { "data-testid": "Field" },
    label ? React.createElement("span", { "data-testid": "Field-label" }, label) : null,
    description != null
      ? React.createElement("span", { "data-testid": "Field-description" }, description)
      : null,
    children,
  );
Field.displayName = "Field";
export const FocusRing = wrap("FocusRing");
export const Marquee = wrap("Marquee");
export const SidebarNavigation = wrap("SidebarNavigation");

/* -------------------------------------------------------------------------- */
/*  Navigation / Router                                                       */
/* -------------------------------------------------------------------------- */

export const Navigation = {
  Navigate: vi.fn(),
  NavigateBack: vi.fn(),
  NavigateToExternalWeb: vi.fn(),
  CloseSideMenus: vi.fn(),
  OpenSideMenu: vi.fn(),
  OpenQuickAccessMenu: vi.fn(),
  OpenMainMenu: vi.fn(),
};

export const Router = {
  Navigate: vi.fn(),
  NavigateBack: vi.fn(),
  NavigateToStore: vi.fn(),
  NavigateToExternalWeb: vi.fn(),
  CloseSideMenus: vi.fn(),
};

/* -------------------------------------------------------------------------- */
/*  Utilities / globals                                                       */
/* -------------------------------------------------------------------------- */

export const staticClasses = new Proxy(
  {} as Record<string, string>,
  {
    get(_target, prop: string) {
      // Return the property name as-is so `staticClasses.Title` → "Title"
      return prop;
    },
  },
);

export const findClassModule = vi.fn();
export const findClass = vi.fn();
export const findClassByName = vi.fn();
export const unminifyClass = vi.fn();

/* -------------------------------------------------------------------------- */
/*  Webpack utilities (no-ops in test)                                        */
/* -------------------------------------------------------------------------- */

export const findModule = vi.fn();
export const findModuleExport = vi.fn();
export const findModuleByExport = vi.fn();
export const findModuleDetailsByExport = vi.fn(() => [{}, undefined]);

/* -------------------------------------------------------------------------- */
/*  Legacy re-export (deprecated in favour of @decky/api)                     */
/* -------------------------------------------------------------------------- */

export const definePlugin = vi.fn((fn: () => unknown) => fn);
