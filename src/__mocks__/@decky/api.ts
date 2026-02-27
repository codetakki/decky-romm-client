/**
 * Mock for @decky/api
 *
 * Provides stub implementations of all Decky Loader API functions
 * so components can be rendered and tested outside the Steam Deck environment.
 *
 * Per-route callable mocks are stored in `callableMocks` from
 * `src/__tests__/decky-api-helpers.ts`. Import that helper in your tests
 * to configure return values.
 */
import { vi } from "vitest";
import { callableMocks } from "../../__tests__/decky-api-helpers";

export const call = vi.fn(async () => undefined);

export const callable = vi.fn((route: string) => {
  if (!callableMocks[route]) {
    callableMocks[route] = vi.fn(async () => undefined);
  }
  return callableMocks[route];
});

export const addEventListener = vi.fn(
  (_event: string, listener: (...args: unknown[]) => unknown) => listener,
);

export const removeEventListener = vi.fn();

export const routerHook = {
  addRoute: vi.fn(),
  addPatch: vi.fn(),
  addGlobalComponent: vi.fn(),
  removeRoute: vi.fn(),
  removePatch: vi.fn(),
  removeGlobalComponent: vi.fn(),
};

export const toaster = {
  toast: vi.fn(() => ({ data: {}, dismiss: vi.fn() })),
};

export const openFilePicker = vi.fn(async () => ({ path: "", realpath: "" }));

export const executeInTab = vi.fn(async () => ({
  success: true,
  result: undefined,
}));

export const injectCssIntoTab = vi.fn(() => "");
export const removeCssFromTab = vi.fn();

export const fetchNoCors = vi.fn(async () => new Response());

export const getExternalResourceURL = vi.fn((url: string) => url);

export const useQuickAccessVisible = vi.fn(() => true);

export const definePlugin = vi.fn((fn: () => unknown) => fn);
