import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    // Content lives in ../content so it can be edited without touching the frontend.
    fs: { allow: [".."] },
  },
});
