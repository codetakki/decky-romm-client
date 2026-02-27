/**
 * Bridge logic tests — scaffold for testing the frontend ↔ Python backend bridge.
 *
 * The Decky plugin communicates with its Python backend via `callable()` from @decky/api.
 * This test file is the place to add tests for any logic that wraps those calls:
 *   - Data transformation before/after backend calls
 *   - Error handling around backend calls
 *   - State management driven by backend responses
 *
 * The `callable` mock (from src/__mocks__/@decky/api.ts) returns a stable vi.fn() per
 * route name, stored in `callableMocks`. You can configure responses before importing
 * the code under test, or directly call the mock to verify arguments.
 */
import { describe, it, expect, vi, beforeEach } from "vitest";
import { callable } from "@decky/api";
import { callableMocks } from "./decky-api-helpers";

describe("Backend bridge (scaffold)", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    // Reset per-route mocks
    for (const key of Object.keys(callableMocks)) {
      delete callableMocks[key];
    }
  });

  it("callable returns a mock function for any route", () => {
    const myBackendFn = callable<[url: string], boolean>("some_python_method");
    expect(myBackendFn).toBeTypeOf("function");
  });

  it("callable returns the same mock for the same route", () => {
    const fn1 = callable("my_route");
    const fn2 = callable("my_route");
    expect(fn1).toBe(fn2);
  });

  it("callableMocks can be pre-configured before callable() is called", async () => {
    callableMocks["search_roms"] = vi.fn().mockResolvedValue({ ok: true, data: [1, 2, 3] });

    const backendCall = callable<[query: string], { ok: boolean; data: number[] }>(
      "search_roms",
    );
    const result = await backendCall("mario");

    expect(result).toEqual({ ok: true, data: [1, 2, 3] });
    expect(callableMocks["search_roms"]).toHaveBeenCalledWith("mario");
  });

  it("callable mock can simulate a backend error", async () => {
    callableMocks["failing_method"] = vi.fn().mockRejectedValue(new Error("Backend unreachable"));

    const backendCall = callable<[], void>("failing_method");

    await expect(backendCall()).rejects.toThrow("Backend unreachable");
  });
});
