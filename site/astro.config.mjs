import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import episodeRedirects from './integrations/episode-redirects.mjs';

export default defineConfig({
  site: 'https://adipod.ai',
  integrations: [sitemap({ filter: (page) => !page.endsWith('.md') }), episodeRedirects()],
  output: 'static',
});
