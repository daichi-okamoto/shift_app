/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './public/*.html',
    './app/helpers/**/*.rb',
    './app/javascript/**/*.js',
    './app/views/**/*',
  ],
  theme: {
    colors: {
      'blue': '#13b5ea',
      'black': '#777777',
      'white': '#ffffff',
      'gray': '#EFEFEF',
      'blue-focus': '#4776e6',
    },
    extend: {
      borderWidth: {
        '1': '1px',
      },
    },
    fontFamily: {
      'reddit': ["Reddit Mono"]
    },
  },
  daisyui: {
    themes: [
      {
        mytheme: {
          'primary': '#13b5ea',
        },
      },
    ],
  },
  plugins: [
    require('daisyui'),
  ],
};
