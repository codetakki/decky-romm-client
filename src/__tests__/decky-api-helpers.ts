/**
 * Test helpers for the @decky/api mock.
 *
 * Import `callableMocks` from here (not from "@decky/api") to access and
 * configure per-route mocks created by `callable()`.
 *
 * Usage:
 *   import { callableMocks } from "./decky-api-helpers";
 *   callableMocks["settings_getSetting"].mockResolvedValue("http://...");
 */
import { vi } from "vitest";

/**
 * Registry of per-route mock functions created by `callable()`.
 * Keyed by the route name string passed to `callable("route_name")`.
 */
export const callableMocks: Record<string, ReturnType<typeof vi.fn>> = {};

/**
 * Reset every route mock to the default behaviour (resolves `undefined`).
 * Call this in `beforeEach` to isolate tests.
 */
export function resetCallableMocks(): void {
  for (const mock of Object.values(callableMocks)) {
    mock.mockReset();
    mock.mockResolvedValue(undefined);
  }
}
