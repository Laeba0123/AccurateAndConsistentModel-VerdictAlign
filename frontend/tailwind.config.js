/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],

  theme: {
    extend: {

      colors: {

        primary: "#2563eb",
        secondary: "#1e293b",
        accent: "#06b6d4",
        success: "#10b981",
        danger: "#ef4444",
        darkbg: "#0f172a",
        cardbg: "#111827"
      }
    },
  },

  plugins: [],
}