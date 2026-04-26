import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  const topics = await getCollection('topics');
  return topics.map((t) => ({
    params: { slug: t.data.slug },
    props: { entry: t },
  }));
}

export const GET: APIRoute = ({ props }) => {
  const { entry } = props as { entry: any };
  const { title, description, lastUpdated } = entry.data;
  const header = [
    `# ${title}`,
    '',
    `> ${description}`,
    '',
    lastUpdated ? `Last updated: ${lastUpdated}` : null,
    `Source: https://adipod.ai/topics/${entry.data.slug}/`,
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
