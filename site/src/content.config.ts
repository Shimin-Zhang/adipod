import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const episodes = defineCollection({
  loader: glob({ base: '../episodes', pattern: '**/*.md' }),
  schema: z.object({
    episode: z.string(),
    title: z.string(),
    date: z.string(),
    slug: z.string(),
    description: z.string().optional(),
    keywords: z.string().optional(),
    appleUrl: z.string().optional(),
    spotifyUrl: z.string().optional(),
    overcastUrl: z.string().optional(),
    pocketCastsUrl: z.string().optional(),
    amazonUrl: z.string().optional(),
    transistorId: z.string().optional(),
    youtubeId: z.string().optional(),
  }),
});

const glossary = defineCollection({
  loader: glob({ base: './src/content/glossary', pattern: '**/*.md' }),
  schema: z.object({
    term: z.string(),
    definition: z.string(),
    episodes: z.array(z.string()).optional(),
    slug: z.string(),
    aliases: z.array(z.string()).optional(),
  }),
});

const blog = defineCollection({
  loader: glob({ base: './src/content/blog', pattern: '**/*.md' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.string(),
    slug: z.string(),
    keywords: z.string().optional(),
    lastUpdated: z.string().optional(),
    episodes: z.array(z.string()).optional(),
  }),
});

const topics = defineCollection({
  loader: glob({ base: './src/content/topics', pattern: '**/*.md' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    slug: z.string(),
    keywords: z.string().optional(),
    lastUpdated: z.string().optional(),
  }),
});

const segments = defineCollection({
  loader: glob({ base: './src/content/segments', pattern: '**/*.md' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    slug: z.string(),
    segmentName: z.string(),
  }),
});

export const collections = { episodes, glossary, blog, topics, segments };
