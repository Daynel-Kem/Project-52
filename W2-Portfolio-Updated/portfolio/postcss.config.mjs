const config = {
  theme: {
    extend: {
        colors: {
            lightHover: '#fcf4ff',
            darkHover: '#2a004a',
            darkTheme: '#11001F'
        },
        fontFamily: {
            Outfit: ["Outfit", "sans-serif"],
            Ovo: ["Ovo", "sans-serif"],
        },
        boxShadow: {
            'black' : '4px 4px 0 #000',
            'white' : '4px 4px 0 #fff',
        }
    }
},
plugins: ["@tailwindcss/postcss"],
};

export default config;
