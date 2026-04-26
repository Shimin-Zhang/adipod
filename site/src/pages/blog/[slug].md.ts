import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  const posts = await getCollection('blog');
  return posts.map((p) => ({
    params: { slug: p.data.slug },
    props: { entry: p },
  }));
}

export const GET: APIRoute = ({ props }) => {
  const { entry } = props as { entry: any };
  const { title, description, date, lastUpdated } = entry.data;
  const header = [
    `# ${title}`,
    '',
    `> ${description}`,
    '',
    date ? `Published: ${date}` : null,
    lastUpdated ? `Last updated: ${lastUpdated}` : null,
    `Source: https://adipod.ai/blog/${entry.data.slug}/`,
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
