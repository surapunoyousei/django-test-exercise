/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./todo/templates/**/*.html", "./config/templates/**/*.html"],
  theme: {
    extend: {},
  },
  plugins: [require("@tailwindcss/forms"), require("daisyui")],
  daisyui: {
    themes: ["light", "dark"],
  },
};
