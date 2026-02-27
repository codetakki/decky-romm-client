/// <reference types="vitest" />
import { defineConfig } from "vitest/config";
import { resolve } from "path";

export default defineConfig({
  test: {
    globals: true,
    environment: "jsdom",
    setupFiles: ["./src/__tests__/setup.ts"],
    include: ["src/**/*.test.{ts,tsx}"],
    alias: {
      "@decky/api": resolve(__dirname, "src/__mocks__/@decky/api.ts"),
      "@decky/ui": resolve(__dirname, "src/__mocks__/@decky/ui.ts"),
    },
  },
});
