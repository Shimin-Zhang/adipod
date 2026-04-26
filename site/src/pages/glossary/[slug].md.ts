import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  const terms = await getCollection('glossary');
  return terms.map((t) => ({
    params: { slug: t.data.slug },
    props: { entry: t },
  }));
}

export const GET: APIRoute = ({ props }) => {
  const { entry } = props as { entry: any };
  const { term, definition, episodes } = entry.data;
  const header = [
    `# ${term}`,
    '',
    `> ${definition}`,
    '',
    `Source: https://adipod.ai/glossary/${entry.data.slug}/`,
    episodes && episodes.length > 0 ? `Related episodes: ${episodes.join(', ')}` : null,
    '',
    '---',
    '',
  ].filter((line) => line !== null).join('\n');

  return new Response(header + (entry.body || ''), {
    headers: {
      'Content-Type': 'text/markdown; charset=utf-8',
    },
  });
};
