import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

export const GET: APIRoute = async () => {
  const [topics, blog, glossary] = await Promise.all([
    getCollection('topics'),
    getCollection('blog'),
    getCollection('glossary'),
  ]);

  const sections: string[] = [];

  sections.push('# ADI Pod — Full Content for AI Systems');
  sections.push('');
  sections.push('> Concatenated topic guides, blog posts, and glossary terms from adipod.ai. For per-page markdown, append `.md` to any content URL.');
  sections.push('');
  sections.push('---');
  sections.push('');

  sections.push('# Topics');
  sections.push('');
  for (const t of topics) {
    sections.push(`## ${t.data.title}`);
    sections.push('');
    sections.push(`> ${t.data.description}`);
    sections.push('');
    sections.push(`Source: https://adipod.ai/topics/${t.data.slug}/`);
    sections.push('');
    sections.push(t.body || '');
    sections.push('');
    sections.push('---');
    sections.push('');
  }

  sections.push('# Blog');
  sections.push('');
  for (const p of blog) {
    sections.push(`## ${p.data.title}`);
    sections.push('');
    sections.push(`> ${p.data.description}`);
    sections.push('');
    sections.push(`Source: https://adipod.ai/blog/${p.data.slug}/`);
    sections.push('');
    sections.push(p.body || '');
    sections.push('');
    sections.push('---');
    sections.push('');
  }

  sections.push('# Glossary');
  sections.push('');
  for (const g of glossary) {
    sections.push(`## ${g.data.term}`);
    sections.push('');
    sections.push(`> ${g.data.definition}`);
    sections.push('');
    sections.push(`Source: https://adipod.ai/glossary/${g.data.slug}/`);
    sections.push('');
    sections.push(g.body || '');
    sections.push('');
    sections.push('---');
    sections.push('');
  }

  return new Response(sections.join('\n'), {
    headers: {
      'Content-Type': 'text/plain; charset=utf-8',
    },
  });
};
