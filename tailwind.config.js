/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./grapher/templates/**/*.html",
    "./grapher/static/src/**/*.js"
  ],
  theme: {
    screens: {
      sm: "480px",
      md: "786px",
      lg: "976px",
      xl: "1440px",
    },
    container: {
      center: true,
      screens: {
        lg: "1124px",
        xl: "1124px",
        "2xl": "1124px",
      },
    },
    extend : {
    },
  },
  plugins: [],
}