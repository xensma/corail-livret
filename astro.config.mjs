import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://livrets.corailconciergerie.com',
  integrations: [tailwind()],
  build: {
    inlineStylesheets: 'auto',
    assets: 'assets'
  },
  vite: {
    build: {
      cssCodeSplit: false
    }
  }
});
