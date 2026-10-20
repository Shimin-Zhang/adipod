// Writes dist/_redirects so the short episode links Transistor puts in the RSS
// feed (https://www.adipod.ai/43) 301 to the episode page. Cloudflare Pages
// reads _redirects from the deploy root.
import { readdirSync, readFileSync, writeFileSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

const episodesDir = fileURLToPath(new URL('../../episodes/', import.meta.url));

export default function episodeRedirects() {
  return {
    name: 'episode-redirects',
    hooks: {
      'astro:build:done': ({ dir, logger }) => {
        const outDir = fileURLToPath(dir);
        const lines = [];
        for (const file of readdirSync(episodesDir).filter((f) => f.endsWith('.md'))) {
          const text = readFileSync(episodesDir + file, 'utf8');
          const episode = text.match(/^episode:\s*"?(\d+)"?\s*$/m)?.[1];
          const slug = text.match(/^slug:\s*"([^"]+)"\s*$/m)?.[1];
          if (!episode || !slug) {
            logger.warn(`${file}: missing episode or slug, no redirect`);
            continue;
          }
          if (!existsSync(`${outDir}episodes/${slug}/index.html`)) {
            logger.warn(`${file}: /episodes/${slug}/ not built, no redirect`);
            continue;
          }
          lines.push([Number(episode), `/${episode} /episodes/${slug}/ 301`, `/${episode}/ /episodes/${slug}/ 301`]);
        }
        lines.sort((a, b) => a[0] - b[0]);
        writeFileSync(`${outDir}_redirects`, lines.flatMap(([, ...l]) => l).join('\n') + '\n');
        logger.info(`wrote _redirects for ${lines.length} episodes`);
      },
    },
  };
}
