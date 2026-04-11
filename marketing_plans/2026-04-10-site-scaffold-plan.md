# ADI Pod Site Scaffold — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the Astro static site for adipod.ai with content collections, schema markup, layouts, and Cloudflare Pages deployment — producing 20 episode pages from existing transcript data on day one.

**Architecture:** Astro static site using content collections backed by markdown files. Episode data is loaded from the existing transcript/summary markdown files in the podcast-agent workspace. Layouts inject JSON-LD schema markup (PodcastSeries, PodcastEpisode, Article, DefinedTerm, FAQPage, Person) automatically based on content type. Deployed to Cloudflare Pages via git push.

**Tech Stack:** Astro 5.x, Node 22, TypeScript, Zod (via astro/zod), Cloudflare Pages

**Spec:** `marketing_plans/2026-04-10-agent-powered-seo-geo-plan.md`

**Transcript data location:** `/home/shimin/agents/podcast-agent/workspace/.pi/skills/podcast-transcripts/transcripts/ep-*.md` and `/home/shimin/agents/podcast-agent/workspace/.pi/skills/podcast-transcripts/summaries/ep-*-summary.md`

---

## File Structure

```
site/
├── astro.config.mjs
├── package.json
├── tsconfig.json
├── src/
│   ├── content.config.ts          # Content collection definitions
│   ├── content/
│   │   ├── episodes/              # Symlinked or copied episode markdown
│   │   ├── glossary/              # Term definitions (empty initially, agent fills later)
│   │   ├── blog/                  # Blog posts (empty initially, agent fills later)
│   │   ├── topics/                # Pillar pages (empty initially)
│   │   └── segments/              # Segment hub pages (empty initially)
│   ├── layouts/
│   │   ├── BaseLayout.astro       # HTML shell, meta, OG tags, global schema
│   │   ├── EpisodeLayout.astro    # Episode page layout with PodcastEpisode schema
│   │   ├── ArticleLayout.astro    # Blog/topic/segment layout with Article schema
│   │   └── GlossaryLayout.astro   # Glossary entry layout with DefinedTerm schema
│   ├── components/
│   │   ├── SchemaMarkup.astro     # JSON-LD renderer component
│   │   ├── Nav.astro              # Site navigation
│   │   ├── Footer.astro           # Site footer
│   │   └── EpisodeCard.astro      # Episode list item component
│   ├── pages/
│   │   ├── index.astro            # Homepage
│   │   ├── episodes/
│   │   │   ├── index.astro        # Episode listing page
│   │   │   └── [...slug].astro    # Dynamic episode pages
│   │   ├── glossary/
│   │   │   ├── index.astro        # Glossary listing page
│   │   │   └── [...slug].astro    # Dynamic glossary pages
│   │   ├── blog/
│   │   │   ├── index.astro        # Blog listing page
│   │   │   └── [...slug].astro    # Dynamic blog pages
│   │   ├── topics/
│   │   │   └── [...slug].astro    # Dynamic pillar pages
│   │   ├── segments/
│   │   │   └── [...slug].astro    # Dynamic segment hub pages
│   │   └── about/
│   │       ├── index.astro        # About overview
│   │       ├── shimin.astro       # Shimin bio with Person schema
│   │       ├── dan.astro          # Dan bio with Person schema
│   │       └── rahul.astro        # Rahul bio with Person schema
│   └── styles/
│       └── global.css             # Minimal global styles
├── public/
│   ├── favicon.svg
│   └── robots.txt
└── scripts/
    └── copy-episodes.sh           # Copies transcript+summary data into content/episodes/
```

---

### Task 1: Initialize Astro Project

**Files:**
- Create: `site/package.json`
- Create: `site/astro.config.mjs`
- Create: `site/tsconfig.json`

- [ ] **Step 1: Create the site directory**

```bash
mkdir -p /home/shimin/projects/adi_pod/site
```

- [ ] **Step 2: Initialize Astro project**

```bash
cd /home/shimin/projects/adi_pod/site && npm create astro@latest -- . --template minimal --no-install --no-git --typescript strict
```

If the interactive prompts can't be avoided, create the files manually instead. The key files needed:

`site/package.json`:
```json
{
  "name": "adipod-site",
  "type": "module",
  "version": "0.0.1",
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview"
  },
  "dependencies": {
    "astro": "^5.0.0",
    "@astrojs/sitemap": "^3.0.0"
  }
}
```

- [ ] **Step 3: Configure Astro**

`site/astro.config.mjs`:
```javascript
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://adipod.ai',
  integrations: [sitemap()],
  output: 'static',
});
```

- [ ] **Step 4: Configure TypeScript**

`site/tsconfig.json`:
```json
{
  "extends": "astro/tsconfigs/strict",
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  }
}
```

- [ ] **Step 5: Install dependencies**

```bash
cd /home/shimin/projects/adi_pod/site && npm install
```

Expected: `node_modules/` created, no errors.

- [ ] **Step 6: Verify Astro runs**

```bash
cd /home/shimin/projects/adi_pod/site && npx astro build
```

Expected: Build succeeds (may warn about no pages, that's fine).

- [ ] **Step 7: Commit**

```bash
cd /home/shimin/projects/adi_pod && git add site/package.json site/package-lock.json site/astro.config.mjs site/tsconfig.json
git commit -m "feat: initialize Astro project for adipod.ai"
```

---

### Task 2: Episode Data Pipeline

**Files:**
- Create: `site/scripts/copy-episodes.sh`
- Create: `site/src/content/episodes/` (directory with generated markdown files)

The existing transcript files have frontmatter (`episode`, `title`, `date`, `added`) but need a slug and summary merged in. This script copies transcripts, injects the summary as a frontmatter field, and generates an SEO-friendly slug.

- [ ] **Step 1: Create the copy script**

`site/scripts/copy-episodes.sh`:
```bash
#!/usr/bin/env bash
set -euo pipefail

TRANSCRIPT_DIR="/home/shimin/agents/podcast-agent/workspace/.pi/skills/podcast-transcripts/transcripts"
SUMMARY_DIR="/home/shimin/agents/podcast-agent/workspace/.pi/skills/podcast-transcripts/summaries"
OUTPUT_DIR="/home/shimin/projects/adi_pod/site/src/content/episodes"

mkdir -p "$OUTPUT_DIR"

for transcript in "$TRANSCRIPT_DIR"/ep-*.md; do
  filename=$(basename "$transcript")
  ep_num=$(echo "$filename" | sed 's/ep-\(.*\)\.md/\1/')
  summary_file="$SUMMARY_DIR/ep-${ep_num}-summary.md"

  # Read frontmatter fields from transcript
  title=$(sed -n 's/^title: "\(.*\)"/\1/p' "$transcript")
  date=$(sed -n 's/^date: "\(.*\)"/\1/p' "$transcript")

  # Generate slug from title: lowercase, replace non-alphanumeric with hyphens, trim
  slug=$(echo "$title" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-//;s/-$//')
  slug="${ep_num}-${slug}"

  # Extract summary overview (the line after **Overview:**)
  description=""
  if [ -f "$summary_file" ]; then
    description=$(sed -n 's/^\*\*Overview:\*\* //p' "$summary_file")
  fi

  # Extract keywords from summary
  keywords=""
  if [ -f "$summary_file" ]; then
    keywords=$(sed -n 's/^\*\*Keywords:\*\* //p' "$summary_file")
  fi

  # Get transcript body (everything after frontmatter closing ---)
  body=$(awk 'BEGIN{c=0} /^---$/{c++; if(c==2){found=1; next}} found{print}' "$transcript")

  # Get summary body (everything after frontmatter closing ---)
  summary_body=""
  if [ -f "$summary_file" ]; then
    summary_body=$(awk 'BEGIN{c=0} /^---$/{c++; if(c==2){found=1; next}} found{print}' "$summary_file")
  fi

  # Write combined episode file
  cat > "$OUTPUT_DIR/$filename" <<FRONTMATTER
---
episode: "$ep_num"
title: "$title"
date: "$date"
slug: "$slug"
description: "$(echo "$description" | sed 's/"/\\"/g')"
keywords: "$keywords"
---

$summary_body

---

## Full Transcript

$body
FRONTMATTER

  echo "Processed ep-${ep_num}: $title"
done

echo "Done. $(ls "$OUTPUT_DIR"/ep-*.md | wc -l) episodes copied."
```

- [ ] **Step 2: Make it executable and run it**

```bash
chmod +x /home/shimin/projects/adi_pod/site/scripts/copy-episodes.sh
/home/shimin/projects/adi_pod/site/scripts/copy-episodes.sh
```

Expected: `Done. 20 episodes copied.`

- [ ] **Step 3: Verify output**

```bash
head -15 /home/shimin/projects/adi_pod/site/src/content/episodes/ep-1.md
```

Expected: Frontmatter with episode, title, date, slug, description, keywords fields, followed by summary body and transcript.

- [ ] **Step 4: Add episodes directory to .gitignore**

These are generated files — the source of truth is the transcript skill directory.

Add to `site/.gitignore`:
```
src/content/episodes/
```

- [ ] **Step 5: Commit**

```bash
cd /home/shimin/projects/adi_pod && git add site/scripts/copy-episodes.sh site/.gitignore
git commit -m "feat: add episode data pipeline script"
```

---

### Task 3: Content Collections Config

**Files:**
- Create: `site/src/content.config.ts`
- Create: `site/src/content/glossary/.gitkeep`
- Create: `site/src/content/blog/.gitkeep`
- Create: `site/src/content/topics/.gitkeep`
- Create: `site/src/content/segments/.gitkeep`

- [ ] **Step 1: Define content collections**

`site/src/content.config.ts`:
```typescript
import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const episodes = defineCollection({
  loader: glob({ base: './src/content/episodes', pattern: '**/*.md' }),
  schema: z.object({
    episode: z.string(),
    title: z.string(),
    date: z.string(),
    slug: z.string(),
    description: z.string().optional(),
    keywords: z.string().optional(),
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
```

- [ ] **Step 2: Create placeholder directories**

```bash
mkdir -p /home/shimin/projects/adi_pod/site/src/content/{glossary,blog,topics,segments}
touch /home/shimin/projects/adi_pod/site/src/content/{glossary,blog,topics,segments}/.gitkeep
```

- [ ] **Step 3: Verify collections sync**

```bash
cd /home/shimin/projects/adi_pod/site && npx astro sync
```

Expected: No errors. Type definitions generated.

- [ ] **Step 4: Commit**

```bash
cd /home/shimin/projects/adi_pod && git add site/src/content.config.ts site/src/content/glossary/.gitkeep site/src/content/blog/.gitkeep site/src/content/topics/.gitkeep site/src/content/segments/.gitkeep
git commit -m "feat: define content collections for episodes, glossary, blog, topics, segments"
```

---

### Task 4: Base Layout with Schema Markup

**Files:**
- Create: `site/src/components/SchemaMarkup.astro`
- Create: `site/src/components/Nav.astro`
- Create: `site/src/components/Footer.astro`
- Create: `site/src/layouts/BaseLayout.astro`
- Create: `site/src/styles/global.css`
- Create: `site/public/robots.txt`
- Create: `site/public/favicon.svg`

- [ ] **Step 1: Create SchemaMarkup component**

`site/src/components/SchemaMarkup.astro`:
```astro
---
interface Props {
  schema: Record<string, unknown> | Record<string, unknown>[];
}

const { schema } = Astro.props;
const schemas = Array.isArray(schema) ? schema : [schema];
---

{schemas.map((s) => (
  <script type="application/ld+json" set:html={JSON.stringify(s)} />
))}
```

- [ ] **Step 2: Create Nav component**

`site/src/components/Nav.astro`:
```astro
---
const currentPath = Astro.url.pathname;

const links = [
  { href: '/', label: 'Home' },
  { href: '/episodes/', label: 'Episodes' },
  { href: '/blog/', label: 'Blog' },
  { href: '/topics/', label: 'Topics' },
  { href: '/glossary/', label: 'Glossary' },
  { href: '/about/', label: 'About' },
];
---

<nav>
  <a href="/" class="nav-brand">ADI Pod</a>
  <div class="nav-links">
    {links.map(({ href, label }) => (
      <a href={href} class:list={[{ active: currentPath.startsWith(href) && href !== '/' || currentPath === href }]}>
        {label}
      </a>
    ))}
  </div>
</nav>

<style>
  nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 2rem;
    border-bottom: 1px solid #e5e5e5;
    max-width: 1200px;
    margin: 0 auto;
  }
  .nav-brand {
    font-weight: 700;
    font-size: 1.25rem;
    text-decoration: none;
    color: #111;
  }
  .nav-links {
    display: flex;
    gap: 1.5rem;
  }
  .nav-links a {
    text-decoration: none;
    color: #555;
    font-size: 0.9rem;
  }
  .nav-links a:hover, .nav-links a.active {
    color: #111;
  }
</style>
```

- [ ] **Step 3: Create Footer component**

`site/src/components/Footer.astro`:
```astro
---
const year = new Date().getFullYear();
---

<footer>
  <p>&copy; {year} Artificial Developer Intelligence (ADI Pod). Shimin Zhang &amp; Dan Lasky.</p>
  <p>
    <a href="https://podcasts.apple.com/us/podcast/artificial-developer-intelligence" target="_blank" rel="noopener">Apple Podcasts</a>
    &middot;
    <a href="https://open.spotify.com/show/artificial-developer-intelligence" target="_blank" rel="noopener">Spotify</a>
    &middot;
    <a href="https://www.youtube.com/@adipod" target="_blank" rel="noopener">YouTube</a>
    &middot;
    <a href="mailto:humans@adipod.ai">humans@adipod.ai</a>
  </p>
</footer>

<style>
  footer {
    border-top: 1px solid #e5e5e5;
    padding: 2rem;
    text-align: center;
    color: #888;
    font-size: 0.85rem;
    max-width: 1200px;
    margin: 4rem auto 0;
  }
  footer a {
    color: #555;
  }
</style>
```

- [ ] **Step 4: Create global styles**

`site/src/styles/global.css`:
```css
*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
  line-height: 1.6;
  color: #222;
}

body {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

h1, h2, h3, h4, h5, h6 {
  line-height: 1.3;
  margin-top: 1.5em;
  margin-bottom: 0.5em;
}

h1 { font-size: 2rem; }
h2 { font-size: 1.5rem; }
h3 { font-size: 1.25rem; }

p { margin-bottom: 1em; }

a { color: #2563eb; }
a:hover { color: #1d4ed8; }

ul, ol { margin-bottom: 1em; padding-left: 1.5em; }

code {
  background: #f3f4f6;
  padding: 0.15em 0.3em;
  border-radius: 3px;
  font-size: 0.9em;
}

pre {
  background: #f3f4f6;
  padding: 1rem;
  border-radius: 6px;
  overflow-x: auto;
  margin-bottom: 1em;
}

pre code {
  background: none;
  padding: 0;
}

blockquote {
  border-left: 3px solid #d1d5db;
  padding-left: 1rem;
  color: #555;
  margin-bottom: 1em;
}

article {
  max-width: 800px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 1em;
}

th, td {
  border: 1px solid #e5e5e5;
  padding: 0.5rem 0.75rem;
  text-align: left;
}

th { background: #f9fafb; font-weight: 600; }
```

- [ ] **Step 5: Create BaseLayout**

`site/src/layouts/BaseLayout.astro`:
```astro
---
import Nav from '../components/Nav.astro';
import Footer from '../components/Footer.astro';
import SchemaMarkup from '../components/SchemaMarkup.astro';
import '../styles/global.css';

interface Props {
  title: string;
  description?: string;
  schema?: Record<string, unknown> | Record<string, unknown>[];
  ogType?: string;
  canonicalUrl?: string;
}

const {
  title,
  description = 'Artificial Developer Intelligence — a weekly podcast where practicing engineers navigate AI-enabled software development.',
  schema,
  ogType = 'website',
  canonicalUrl,
} = Astro.props;

const siteUrl = 'https://adipod.ai';
const fullTitle = title === 'ADI Pod' ? title : `${title} — ADI Pod`;
const canonical = canonicalUrl || new URL(Astro.url.pathname, siteUrl).href;

const podcastSeriesSchema = {
  '@context': 'https://schema.org',
  '@type': 'PodcastSeries',
  name: 'Artificial Developer Intelligence',
  alternateName: 'ADI Pod',
  url: siteUrl,
  description: 'Weekly AI news and deep dives for software developers. Claude Code, vibe coding, AI coding agents, LLM architectures, and AI bubble analysis from practicing engineers.',
  author: [
    { '@type': 'Person', name: 'Shimin Zhang' },
    { '@type': 'Person', name: 'Dan Lasky' },
  ],
  genre: ['Technology', 'Software Development', 'Artificial Intelligence'],
  inLanguage: 'en',
};

const allSchemas = [podcastSeriesSchema, ...(schema ? (Array.isArray(schema) ? schema : [schema]) : [])];
---

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{fullTitle}</title>
    <meta name="description" content={description} />
    <link rel="canonical" href={canonical} />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <link rel="sitemap" href="/sitemap-index.xml" />

    <!-- Open Graph -->
    <meta property="og:title" content={fullTitle} />
    <meta property="og:description" content={description} />
    <meta property="og:type" content={ogType} />
    <meta property="og:url" content={canonical} />
    <meta property="og:site_name" content="ADI Pod" />

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary" />
    <meta name="twitter:title" content={fullTitle} />
    <meta name="twitter:description" content={description} />

    <SchemaMarkup schema={allSchemas} />
  </head>
  <body>
    <Nav />
    <main>
      <slot />
    </main>
    <Footer />
  </body>
</html>
```

- [ ] **Step 6: Create robots.txt**

`site/public/robots.txt`:
```
User-agent: *
Allow: /
Sitemap: https://adipod.ai/sitemap-index.xml
```

- [ ] **Step 7: Create favicon placeholder**

`site/public/favicon.svg`:
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <rect width="32" height="32" rx="4" fill="#111"/>
  <text x="50%" y="55%" dominant-baseline="central" text-anchor="middle" font-family="sans-serif" font-weight="700" font-size="16" fill="#fff">A</text>
</svg>
```

- [ ] **Step 8: Verify build**

```bash
cd /home/shimin/projects/adi_pod/site && npx astro build
```

Expected: Build succeeds (may warn about no pages using the layout yet).

- [ ] **Step 9: Commit**

```bash
cd /home/shimin/projects/adi_pod && git add site/src/components/ site/src/layouts/BaseLayout.astro site/src/styles/global.css site/public/
git commit -m "feat: add base layout with schema markup, nav, footer, global styles"
```

---

### Task 5: Episode Layout and Pages

**Files:**
- Create: `site/src/layouts/EpisodeLayout.astro`
- Create: `site/src/components/EpisodeCard.astro`
- Create: `site/src/pages/episodes/index.astro`
- Create: `site/src/pages/episodes/[...slug].astro`

- [ ] **Step 1: Create EpisodeLayout**

`site/src/layouts/EpisodeLayout.astro`:
```astro
---
import BaseLayout from './BaseLayout.astro';

interface Props {
  episode: string;
  title: string;
  date: string;
  description?: string;
  keywords?: string;
}

const { episode, title, date, description, keywords } = Astro.props;

const episodeSchema = {
  '@context': 'https://schema.org',
  '@type': 'PodcastEpisode',
  name: title,
  episodeNumber: episode,
  datePublished: date,
  description: description || '',
  partOfSeries: {
    '@type': 'PodcastSeries',
    name: 'Artificial Developer Intelligence',
    url: 'https://adipod.ai',
  },
  author: [
    { '@type': 'Person', name: 'Shimin Zhang' },
    { '@type': 'Person', name: 'Dan Lasky' },
  ],
};
---

<BaseLayout title={`Ep ${episode}: ${title}`} description={description} schema={episodeSchema} ogType="article">
  <article>
    <header>
      <p class="episode-meta">Episode {episode} &middot; {new Date(date + 'T00:00:00').toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}</p>
      <h1>{title}</h1>
      {keywords && <p class="keywords">{keywords}</p>}
    </header>
    <slot />
  </article>
</BaseLayout>

<style>
  .episode-meta {
    color: #888;
    font-size: 0.9rem;
    margin-bottom: 0.25rem;
  }
  h1 {
    margin-top: 0.25rem;
  }
  .keywords {
    color: #888;
    font-size: 0.85rem;
    font-style: italic;
  }
  article {
    padding: 2rem 0;
  }
</style>
```

- [ ] **Step 2: Create EpisodeCard component**

`site/src/components/EpisodeCard.astro`:
```astro
---
interface Props {
  episode: string;
  title: string;
  date: string;
  slug: string;
  description?: string;
}

const { episode, title, date, slug, description } = Astro.props;
---

<a href={`/episodes/${slug}/`} class="episode-card">
  <span class="ep-num">Ep {episode}</span>
  <span class="ep-date">{new Date(date + 'T00:00:00').toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })}</span>
  <h3>{title}</h3>
  {description && <p>{description}</p>}
</a>

<style>
  .episode-card {
    display: block;
    text-decoration: none;
    color: inherit;
    padding: 1.25rem;
    border: 1px solid #e5e5e5;
    border-radius: 8px;
    margin-bottom: 1rem;
    transition: border-color 0.15s;
  }
  .episode-card:hover {
    border-color: #2563eb;
  }
  .ep-num {
    font-weight: 600;
    font-size: 0.85rem;
    color: #2563eb;
  }
  .ep-date {
    color: #888;
    font-size: 0.85rem;
    margin-left: 0.75rem;
  }
  h3 {
    margin: 0.25rem 0;
    font-size: 1.1rem;
  }
  p {
    color: #555;
    font-size: 0.9rem;
    margin: 0;
  }
</style>
```

- [ ] **Step 3: Create episode listing page**

`site/src/pages/episodes/index.astro`:
```astro
---
import { getCollection } from 'astro:content';
import BaseLayout from '../../layouts/BaseLayout.astro';
import EpisodeCard from '../../components/EpisodeCard.astro';

const episodes = await getCollection('episodes');
const sorted = episodes.sort((a, b) => parseInt(b.data.episode) - parseInt(a.data.episode));
---

<BaseLayout title="Episodes" description="All episodes of the ADI Pod — Artificial Developer Intelligence.">
  <section style="padding: 2rem 0;">
    <h1>Episodes</h1>
    <p>All {sorted.length} episodes of the ADI Pod.</p>
    {sorted.map((ep) => (
      <EpisodeCard
        episode={ep.data.episode}
        title={ep.data.title}
        date={ep.data.date}
        slug={ep.data.slug}
        description={ep.data.description}
      />
    ))}
  </section>
</BaseLayout>
```

- [ ] **Step 4: Create dynamic episode pages**

`site/src/pages/episodes/[...slug].astro`:
```astro
---
import { getCollection, render } from 'astro:content';
import EpisodeLayout from '../../layouts/EpisodeLayout.astro';

export async function getStaticPaths() {
  const episodes = await getCollection('episodes');
  return episodes.map((ep) => ({
    params: { slug: ep.data.slug },
    props: { entry: ep },
  }));
}

const { entry } = Astro.props;
const { Content } = await render(entry);
---

<EpisodeLayout
  episode={entry.data.episode}
  title={entry.data.title}
  date={entry.data.date}
  description={entry.data.description}
  keywords={entry.data.keywords}
>
  <Content />
</EpisodeLayout>
```

- [ ] **Step 5: Run the copy script to ensure episode data exists, then build**

```bash
cd /home/shimin/projects/adi_pod && ./site/scripts/copy-episodes.sh && cd site && npx astro build
```

Expected: Build succeeds. 20 episode pages generated. Check output:

```bash
ls dist/episodes/ | head -5
```

Expected: Directories named by slug.

- [ ] **Step 6: Commit**

```bash
cd /home/shimin/projects/adi_pod && git add site/src/layouts/EpisodeLayout.astro site/src/components/EpisodeCard.astro site/src/pages/episodes/
git commit -m "feat: add episode listing and dynamic episode pages with PodcastEpisode schema"
```

---

### Task 6: Glossary, Blog, Topics, and Segments Page Shells

**Files:**
- Create: `site/src/layouts/ArticleLayout.astro`
- Create: `site/src/layouts/GlossaryLayout.astro`
- Create: `site/src/pages/glossary/index.astro`
- Create: `site/src/pages/glossary/[...slug].astro`
- Create: `site/src/pages/blog/index.astro`
- Create: `site/src/pages/blog/[...slug].astro`
- Create: `site/src/pages/topics/[...slug].astro`
- Create: `site/src/pages/segments/[...slug].astro`

- [ ] **Step 1: Create ArticleLayout**

`site/src/layouts/ArticleLayout.astro`:
```astro
---
import BaseLayout from './BaseLayout.astro';

interface Props {
  title: string;
  description: string;
  date?: string;
  keywords?: string;
  lastUpdated?: string;
}

const { title, description, date, keywords, lastUpdated } = Astro.props;

const articleSchema = {
  '@context': 'https://schema.org',
  '@type': 'Article',
  headline: title,
  description: description,
  datePublished: date || undefined,
  dateModified: lastUpdated || date || undefined,
  author: [
    { '@type': 'Person', name: 'Shimin Zhang' },
    { '@type': 'Person', name: 'Dan Lasky' },
  ],
  publisher: {
    '@type': 'Organization',
    name: 'ADI Pod',
    url: 'https://adipod.ai',
  },
};
---

<BaseLayout title={title} description={description} schema={articleSchema} ogType="article">
  <article style="padding: 2rem 0;">
    <header>
      {date && <p class="meta">{new Date(date + 'T00:00:00').toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}{lastUpdated ? ` · Updated ${new Date(lastUpdated + 'T00:00:00').toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}` : ''}</p>}
      <h1>{title}</h1>
      {keywords && <p class="keywords">{keywords}</p>}
    </header>
    <slot />
  </article>
</BaseLayout>

<style>
  .meta { color: #888; font-size: 0.9rem; margin-bottom: 0.25rem; }
  h1 { margin-top: 0.25rem; }
  .keywords { color: #888; font-size: 0.85rem; font-style: italic; }
</style>
```

- [ ] **Step 2: Create GlossaryLayout**

`site/src/layouts/GlossaryLayout.astro`:
```astro
---
import BaseLayout from './BaseLayout.astro';

interface Props {
  term: string;
  definition: string;
  episodes?: string[];
}

const { term, definition, episodes } = Astro.props;

const definedTermSchema = {
  '@context': 'https://schema.org',
  '@type': 'DefinedTerm',
  name: term,
  description: definition,
  inDefinedTermSet: {
    '@type': 'DefinedTermSet',
    name: 'ADI Pod Glossary',
    url: 'https://adipod.ai/glossary/',
  },
};
---

<BaseLayout title={term} description={definition} schema={definedTermSchema}>
  <article style="padding: 2rem 0;">
    <p><a href="/glossary/">&larr; Glossary</a></p>
    <h1>{term}</h1>
    <p class="definition"><em>{definition}</em></p>
    <slot />
    {episodes && episodes.length > 0 && (
      <section>
        <h2>Related Episodes</h2>
        <ul>
          {episodes.map((ep) => <li>Episode {ep}</li>)}
        </ul>
      </section>
    )}
  </article>
</BaseLayout>

<style>
  .definition { font-size: 1.1rem; color: #555; margin-bottom: 1.5rem; }
</style>
```

- [ ] **Step 3: Create glossary listing page**

`site/src/pages/glossary/index.astro`:
```astro
---
import { getCollection } from 'astro:content';
import BaseLayout from '../../layouts/BaseLayout.astro';

const terms = await getCollection('glossary');
const sorted = terms.sort((a, b) => a.data.term.localeCompare(b.data.term));
---

<BaseLayout title="Glossary" description="Key terms and concepts from the ADI Pod — AI developer vocabulary defined by practitioners.">
  <section style="padding: 2rem 0;">
    <h1>Glossary</h1>
    <p>Key terms and concepts discussed on the ADI Pod, defined by practitioners.</p>
    {sorted.length === 0 ? (
      <p><em>Glossary entries coming soon.</em></p>
    ) : (
      <dl>
        {sorted.map((t) => (
          <>
            <dt><a href={`/glossary/${t.data.slug}/`}>{t.data.term}</a></dt>
            <dd>{t.data.definition}</dd>
          </>
        ))}
      </dl>
    )}
  </section>
</BaseLayout>

<style>
  dl { margin-top: 1.5rem; }
  dt { font-weight: 600; margin-top: 1rem; }
  dt a { text-decoration: none; }
  dd { color: #555; margin-left: 0; margin-bottom: 0.5rem; }
</style>
```

- [ ] **Step 4: Create dynamic glossary pages**

`site/src/pages/glossary/[...slug].astro`:
```astro
---
import { getCollection, render } from 'astro:content';
import GlossaryLayout from '../../layouts/GlossaryLayout.astro';

export async function getStaticPaths() {
  const terms = await getCollection('glossary');
  return terms.map((t) => ({
    params: { slug: t.data.slug },
    props: { entry: t },
  }));
}

const { entry } = Astro.props;
const { Content } = await render(entry);
---

<GlossaryLayout term={entry.data.term} definition={entry.data.definition} episodes={entry.data.episodes}>
  <Content />
</GlossaryLayout>
```

- [ ] **Step 5: Create blog listing page**

`site/src/pages/blog/index.astro`:
```astro
---
import { getCollection } from 'astro:content';
import BaseLayout from '../../layouts/BaseLayout.astro';

const posts = await getCollection('blog');
const sorted = posts.sort((a, b) => new Date(b.data.date).getTime() - new Date(a.data.date).getTime());
---

<BaseLayout title="Blog" description="Articles on AI development, coding agents, and LLM engineering from the ADI Pod.">
  <section style="padding: 2rem 0;">
    <h1>Blog</h1>
    {sorted.length === 0 ? (
      <p><em>Blog posts coming soon.</em></p>
    ) : (
      sorted.map((post) => (
        <article class="post-card">
          <p class="meta">{new Date(post.data.date + 'T00:00:00').toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })}</p>
          <h2><a href={`/blog/${post.data.slug}/`}>{post.data.title}</a></h2>
          <p>{post.data.description}</p>
        </article>
      ))
    )}
  </section>
</BaseLayout>

<style>
  .post-card { margin-bottom: 2rem; }
  .meta { color: #888; font-size: 0.85rem; margin-bottom: 0.25rem; }
  h2 { margin-top: 0; font-size: 1.25rem; }
  h2 a { text-decoration: none; }
</style>
```

- [ ] **Step 6: Create dynamic blog pages**

`site/src/pages/blog/[...slug].astro`:
```astro
---
import { getCollection, render } from 'astro:content';
import ArticleLayout from '../../layouts/ArticleLayout.astro';

export async function getStaticPaths() {
  const posts = await getCollection('blog');
  return posts.map((post) => ({
    params: { slug: post.data.slug },
    props: { entry: post },
  }));
}

const { entry } = Astro.props;
const { Content } = await render(entry);
---

<ArticleLayout title={entry.data.title} description={entry.data.description} date={entry.data.date} keywords={entry.data.keywords}>
  <Content />
</ArticleLayout>
```

- [ ] **Step 7: Create dynamic topics pages**

`site/src/pages/topics/[...slug].astro`:
```astro
---
import { getCollection, render } from 'astro:content';
import ArticleLayout from '../../layouts/ArticleLayout.astro';

export async function getStaticPaths() {
  const topics = await getCollection('topics');
  return topics.map((t) => ({
    params: { slug: t.data.slug },
    props: { entry: t },
  }));
}

const { entry } = Astro.props;
const { Content } = await render(entry);
---

<ArticleLayout title={entry.data.title} description={entry.data.description} keywords={entry.data.keywords} lastUpdated={entry.data.lastUpdated}>
  <Content />
</ArticleLayout>
```

- [ ] **Step 8: Create dynamic segments pages**

`site/src/pages/segments/[...slug].astro`:
```astro
---
import { getCollection, render } from 'astro:content';
import ArticleLayout from '../../layouts/ArticleLayout.astro';

export async function getStaticPaths() {
  const segments = await getCollection('segments');
  return segments.map((s) => ({
    params: { slug: s.data.slug },
    props: { entry: s },
  }));
}

const { entry } = Astro.props;
const { Content } = await render(entry);
---

<ArticleLayout title={entry.data.title} description={entry.data.description}>
  <Content />
</ArticleLayout>
```

- [ ] **Step 9: Build and verify**

```bash
cd /home/shimin/projects/adi_pod/site && npx astro build
```

Expected: Build succeeds. Episode pages generated. Glossary/blog/topics/segments pages exist but are empty (no content yet).

- [ ] **Step 10: Commit**

```bash
cd /home/shimin/projects/adi_pod && git add site/src/layouts/ArticleLayout.astro site/src/layouts/GlossaryLayout.astro site/src/pages/glossary/ site/src/pages/blog/ site/src/pages/topics/ site/src/pages/segments/
git commit -m "feat: add glossary, blog, topics, segments page shells with schema markup"
```

---

### Task 7: Homepage and About Pages

**Files:**
- Create: `site/src/pages/index.astro`
- Create: `site/src/pages/about/index.astro`
- Create: `site/src/pages/about/shimin.astro`
- Create: `site/src/pages/about/dan.astro`
- Create: `site/src/pages/about/rahul.astro`

- [ ] **Step 1: Create homepage**

`site/src/pages/index.astro`:
```astro
---
import { getCollection } from 'astro:content';
import BaseLayout from '../layouts/BaseLayout.astro';
import EpisodeCard from '../components/EpisodeCard.astro';

const episodes = await getCollection('episodes');
const latest = episodes
  .sort((a, b) => parseInt(b.data.episode) - parseInt(a.data.episode))
  .slice(0, 5);
---

<BaseLayout title="ADI Pod" description="Artificial Developer Intelligence — weekly AI news and deep dives for software developers. Claude Code, vibe coding, AI agents, LLM architectures, and AI bubble analysis from practicing engineers.">
  <section class="hero">
    <h1>Artificial Developer Intelligence</h1>
    <p>Weekly AI news and deep dives for software developers. No LinkedIn cringe. No corporate hype. Just two engineers navigating the AI-enabled software engineering landscape.</p>
    <div class="cta-row">
      <a href="/episodes/" class="cta">Browse Episodes</a>
      <a href="/topics/" class="cta-secondary">Explore Topics</a>
    </div>
  </section>

  <section class="latest">
    <h2>Latest Episodes</h2>
    {latest.map((ep) => (
      <EpisodeCard
        episode={ep.data.episode}
        title={ep.data.title}
        date={ep.data.date}
        slug={ep.data.slug}
        description={ep.data.description}
      />
    ))}
    <p><a href="/episodes/">View all episodes &rarr;</a></p>
  </section>
</BaseLayout>

<style>
  .hero {
    padding: 3rem 0 2rem;
  }
  .hero h1 {
    margin-top: 0;
    font-size: 2.5rem;
  }
  .hero p {
    font-size: 1.15rem;
    color: #555;
    max-width: 600px;
  }
  .cta-row {
    display: flex;
    gap: 1rem;
    margin-top: 1.5rem;
  }
  .cta {
    display: inline-block;
    padding: 0.6rem 1.5rem;
    background: #111;
    color: #fff;
    text-decoration: none;
    border-radius: 6px;
    font-size: 0.95rem;
  }
  .cta:hover { background: #333; color: #fff; }
  .cta-secondary {
    display: inline-block;
    padding: 0.6rem 1.5rem;
    border: 1px solid #d1d5db;
    color: #333;
    text-decoration: none;
    border-radius: 6px;
    font-size: 0.95rem;
  }
  .cta-secondary:hover { border-color: #999; }
  .latest {
    padding: 2rem 0;
  }
</style>
```

- [ ] **Step 2: Create about index page**

`site/src/pages/about/index.astro`:
```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
---

<BaseLayout title="About" description="About the ADI Pod — Artificial Developer Intelligence podcast hosted by Shimin Zhang and Dan Lasky.">
  <section style="padding: 2rem 0;">
    <h1>About the ADI Pod</h1>
    <p>Artificial Developer Intelligence is a weekly podcast where practicing software engineers navigate the AI-enabled development landscape. We cover AI news, LLM architectures, coding agents, AI bubble economics, and the evolving craft of software engineering — all without the LinkedIn cringe.</p>

    <h2>Hosts</h2>
    <ul>
      <li><a href="/about/shimin/">Shimin Zhang</a> — Co-host, software engineer, informed skeptic</li>
      <li><a href="/about/dan/">Dan Lasky</a> — Co-host, software engineer, resident ranter</li>
      <li><a href="/about/rahul/">Rahul Yadav</a> — Recurring guest, Director of Engineering at Functionize</li>
    </ul>

    <h2>Recurring Segments</h2>
    <ul>
      <li><strong>Two Minutes to Midnight</strong> — Weekly AI bubble tracker using the doomsday clock metaphor</li>
      <li><strong>Dan's Rant</strong> — Unfiltered opinions on the week's developments</li>
      <li><strong>Technique Corner</strong> — Practical tips for working with AI tools</li>
      <li><strong>Vibe &amp; Tell</strong> — Hands-on project reviews and experiences</li>
      <li><strong>Tool Shed</strong> — AI tool reviews and recommendations</li>
      <li><strong>Post-Processing</strong> — Deep analysis of papers and trends</li>
    </ul>

    <h2>Contact</h2>
    <p>Email: <a href="mailto:humans@adipod.ai">humans@adipod.ai</a></p>
  </section>
</BaseLayout>
```

- [ ] **Step 3: Create host bio pages**

`site/src/pages/about/shimin.astro`:
```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';

const personSchema = {
  '@context': 'https://schema.org',
  '@type': 'Person',
  name: 'Shimin Zhang',
  jobTitle: 'Software Engineer',
  description: 'Co-host of the ADI Pod. Practitioner-scholar, informed skeptic, deadpan humor.',
  url: 'https://adipod.ai/about/shimin/',
};
---

<BaseLayout title="Shimin Zhang" description="Shimin Zhang — co-host of the ADI Pod. Software engineer, AI practitioner, informed skeptic." schema={personSchema}>
  <section style="padding: 2rem 0;">
    <p><a href="/about/">&larr; About</a></p>
    <h1>Shimin Zhang</h1>
    <p>Co-host of the ADI Pod. Software engineer and AI practitioner. Practitioner-scholar hybrid who connects dots across papers, tools, and industry trends. Informed skeptic with deadpan humor and a 2.7:1 technical-to-casual ratio.</p>
  </section>
</BaseLayout>
```

`site/src/pages/about/dan.astro`:
```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';

const personSchema = {
  '@context': 'https://schema.org',
  '@type': 'Person',
  name: 'Dan Lasky',
  jobTitle: 'Software Engineer',
  description: 'Co-host of the ADI Pod. Software engineer, resident ranter, hardware enthusiast.',
  url: 'https://adipod.ai/about/dan/',
};
---

<BaseLayout title="Dan Lasky" description="Dan Lasky — co-host of the ADI Pod. Software engineer, resident ranter, hardware enthusiast." schema={personSchema}>
  <section style="padding: 2rem 0;">
    <p><a href="/about/">&larr; About</a></p>
    <h1>Dan Lasky</h1>
    <p>Co-host of the ADI Pod. Software engineer with strong opinions about AI developer tools. Known for Dan's Rant segment, hardware experiments (TuringPie clusters, Arch Linux), and saying what everyone's thinking about the AI hype cycle.</p>
  </section>
</BaseLayout>
```

`site/src/pages/about/rahul.astro`:
```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';

const personSchema = {
  '@context': 'https://schema.org',
  '@type': 'Person',
  name: 'Rahul Yadav',
  jobTitle: 'Director of Engineering',
  worksFor: { '@type': 'Organization', name: 'Functionize' },
  description: 'Recurring guest on the ADI Pod. Director of Engineering at Functionize.',
  url: 'https://adipod.ai/about/rahul/',
};
---

<BaseLayout title="Rahul Yadav" description="Rahul Yadav — recurring guest on the ADI Pod. Director of Engineering at Functionize." schema={personSchema}>
  <section style="padding: 2rem 0;">
    <p><a href="/about/">&larr; About</a></p>
    <h1>Rahul Yadav</h1>
    <p>Recurring guest and third host of the ADI Pod. Director of Engineering at Functionize. Brings enterprise AI transformation perspective and engineering leadership insights to discussions.</p>
  </section>
</BaseLayout>
```

- [ ] **Step 4: Build and verify**

```bash
cd /home/shimin/projects/adi_pod/site && npx astro build
```

Expected: Build succeeds. Verify pages exist:

```bash
ls dist/ && ls dist/about/ && ls dist/episodes/ | wc -l
```

Expected: index.html at root, about pages, 20+ episode directories.

- [ ] **Step 5: Commit**

```bash
cd /home/shimin/projects/adi_pod && git add site/src/pages/index.astro site/src/pages/about/
git commit -m "feat: add homepage and about pages with Person schema markup"
```

---

### Task 8: Preview, Verify Schema, and Prepare for Deployment

**Files:**
- No new files. Verification task.

- [ ] **Step 1: Full build**

```bash
cd /home/shimin/projects/adi_pod/site && npx astro build
```

Expected: Clean build, no errors.

- [ ] **Step 2: Verify episode page schema markup**

```bash
grep -l "PodcastEpisode" /home/shimin/projects/adi_pod/site/dist/episodes/*/index.html | wc -l
```

Expected: 20 (one per episode).

- [ ] **Step 3: Verify homepage schema markup**

```bash
grep "PodcastSeries" /home/shimin/projects/adi_pod/site/dist/index.html | head -1
```

Expected: JSON-LD block containing PodcastSeries.

- [ ] **Step 4: Verify sitemap**

```bash
cat /home/shimin/projects/adi_pod/site/dist/sitemap-index.xml
```

Expected: Valid sitemap XML referencing all pages.

- [ ] **Step 5: Verify robots.txt**

```bash
cat /home/shimin/projects/adi_pod/site/dist/robots.txt
```

Expected: Contains `Sitemap: https://adipod.ai/sitemap-index.xml`.

- [ ] **Step 6: Preview locally**

```bash
cd /home/shimin/projects/adi_pod/site && npx astro preview
```

Visit http://localhost:4321 and verify:
- Homepage loads with latest 5 episodes
- Episode listing shows all 20 episodes sorted by number
- Individual episode pages render transcript content with schema markup
- Navigation works between all sections
- Glossary/blog/topics show "coming soon" placeholders
- About pages render with host bios
- Footer links are correct

- [ ] **Step 7: Commit any fixes**

```bash
cd /home/shimin/projects/adi_pod && git add -A site/ && git status
```

If there are changes:
```bash
git commit -m "fix: address issues found during preview verification"
```

---

### Task 9: Cloudflare Pages Deployment Setup

**Files:**
- No code files. Configuration and deployment task.

- [ ] **Step 1: Install Wrangler CLI**

```bash
npm install -g wrangler
```

- [ ] **Step 2: Authenticate with Cloudflare**

```bash
wrangler login
```

This opens a browser for OAuth. Follow the prompts.

- [ ] **Step 3: Create Cloudflare Pages project**

```bash
cd /home/shimin/projects/adi_pod/site && wrangler pages project create adipod-site --production-branch main
```

- [ ] **Step 4: Deploy**

```bash
cd /home/shimin/projects/adi_pod/site && npx astro build && wrangler pages deploy dist --project-name adipod-site
```

Expected: Deployment URL returned (e.g., `https://adipod-site.pages.dev`).

- [ ] **Step 5: Verify deployment**

Visit the deployment URL and verify:
- Homepage loads
- Episode pages render
- Schema markup present in page source

- [ ] **Step 6: Configure custom domain**

In the Cloudflare dashboard:
1. Go to Pages > adipod-site > Custom domains
2. Add `adipod.ai`
3. Follow DNS configuration instructions (CNAME or proxied A record)

This step may require DNS propagation time (minutes to hours).

- [ ] **Step 7: Document the deployment process**

Add to `site/README.md` (or note for future reference):

```bash
# Build and deploy
cd site && npx astro build && wrangler pages deploy dist --project-name adipod-site

# Or: push to connected git repo for auto-deploy (configure in Cloudflare dashboard)
```

- [ ] **Step 8: Commit**

```bash
cd /home/shimin/projects/adi_pod && git add site/ && git commit -m "feat: configure Cloudflare Pages deployment"
```

---

## Summary

After completing all 9 tasks:

- **20 episode pages** live at adipod.ai/episodes/[slug]/ with PodcastEpisode schema
- **Episode listing** page at adipod.ai/episodes/
- **Homepage** with latest episodes and value prop
- **Glossary, blog, topics, segments** page shells ready for agent-generated content
- **About pages** with Person schema for all three hosts
- **PodcastSeries schema** on every page
- **Sitemap, robots.txt, Open Graph, Twitter Cards** all configured
- **Deployed to Cloudflare Pages** at adipod.ai

**Next subsystem:** Content collections structure + `site-content-generator` skill (generates glossary entries, blog posts, pillar pages, and segment hubs from transcript data).
