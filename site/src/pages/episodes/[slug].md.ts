import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  const episodes = await getCollection('episodes');
  return episodes.map((ep) => ({
    params: { slug: ep.data.slug },
    props: { entry: ep },
  }));
}

export const GET: APIRoute = ({ props }) => {
  const { entry } = props as { entry: any };
  const { episode, title, date, description } = entry.data;
  const header = [
    `# Episode ${episode}: ${title}`,
    '',
    description ? `> ${description}` : null,
    '',
    `Published: ${date}`,
    `Source: https://adipod.ai/episodes/${entry.data.slug}/`,
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
