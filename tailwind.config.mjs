/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        // Charte Corail Conciergerie
        corail: {
          turquoise: '#72C9C2',
          'turquoise-dark': '#5BA8A2',
          'turquoise-light': '#A6DCD7',
          cream: '#F5F2ED',
          'cream-dark': '#E8E2D6',
          sand: '#D9CDB4',
          ink: '#1F2A2E',
          accent: '#E89888'
        }
      },
      fontFamily: {
        display: ['"Cormorant Garamond"', 'Georgia', 'serif'],
        sans: ['Inter', 'system-ui', 'sans-serif']
      },
      backgroundImage: {
        'gradient-cover': 'linear-gradient(180deg, rgba(31,42,46,0) 0%, rgba(31,42,46,0.7) 100%)'
      },
      animation: {
        'fade-up': 'fadeUp 0.6s ease-out both'
      },
      keyframes: {
        fadeUp: {
          '0%': { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' }
        }
      }
    }
  }
};
