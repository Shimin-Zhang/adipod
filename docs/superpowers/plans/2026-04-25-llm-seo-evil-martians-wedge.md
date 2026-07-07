# LLM SEO (Evil Martians wedge) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add `.md` companion routes for every content page, `<link rel="alternate" type="text/markdown">` pointers in HTML, an aggregated `/llms-full.txt`, and FAQ schema on blog posts — so AI agents can fetch clean markdown and extended context from adipod.ai.

**Architecture:** Astro static endpoints (`*.md.ts` files) generate Markdown responses alongside the HTML pages, sharing the same content collections. `BaseLayout.astro` learns an optional `mdPath` prop and renders an HTML `<link rel="alternate">` pointer; the three content layouts (Article, Episode, Glossary) compute that path from the current URL and pass it through. A shared `extractFAQs` helper feeds the existing `FAQPage` schema into blog posts as well as topics. A single static endpoint emits `/llms-full.txt` by concatenating all topic, blog, and glossary bodies.

**Tech Stack:** Astro 5 static endpoints, TypeScript, content collections (already configured in `site/src/content.config.ts`).

**Out of scope (deferred for follow-up):**
- HTTP `Link` header (needs Cloudflare Pages Functions, separate concern)
- Homepage OG image (no `og/home.jpg` exists yet — generate via `og-image` skill, then a one-line edit)
- Host bio thickening (content writing, not technical)
- `PodcastSeries.webFeed` (needs the Transistor RSS URL — confirm with user before adding)

---

### Task 1: Extract shared `extractFAQs` helper

FAQ extraction currently lives inline in `site/src/pages/topics/[...slug].astro:17-50`. Move it to a shared helper so blog posts can reuse it (Task 8) without duplicating the regex parsing logic.

**Files:**
- Create: `site/src/lib/extract-faqs.ts`
- Modify: `site/src/pages/topics/[...slug].astro`

- [ ] **Step 1: Create the helper file**

```typescript
// site/src/lib/extract-faqs.ts
export interface FAQ {
  question: string;
  answer: string;
}

export function extractFAQs(body: string): FAQ[] {
  const splitAtFAQ = body.split(/^## Frequently Asked Questions$/m);
  if (splitAtFAQ.length < 2) return [];
  let faqContent = splitAtFAQ[1];
  const hrIndex = faqContent.indexOf('\n---');
  if (hrIndex > -1) faqContent = faqContent.slice(0, hrIndex);

  const faqs: FAQ[] = [];
  const parts = faqContent.split(/^### /m).filter(Boolean);

  for (const part of parts) {
    const lines = part.trim().split('\n');
    const question = lines[0]?.trim();
    if (!question) continue;
    const answerLines: string[] = [];
    for (const l of lines.slice(1)) {
      if (l.startsWith('---')) break;
      answerLines.push(l);
    }
    const answer = answerLines
      .join(' ')
      .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1')
      .replace(/\*\*([^*]+)\*\*/g, '$1')
      .replace(/\*([^*]+)\*/g, '$1')
      .replace(/`([^`]+)`/g, '$1')
      .trim();
    if (answer) faqs.push({ question, answer });
  }
  return faqs;
}
```

- [ ] **Step 2: Update topics page to import the helper**

Replace `site/src/pages/topics/[...slug].astro` with:

```astro
---
import { getCollection, render } from 'astro:content';
import ArticleLayout from '../../layouts/ArticleLayout.astro';
import { extractFAQs } from '../../lib/extract-faqs';

export async function getStaticPaths() {
  const topics = await getCollection('topics');
  return topics.map((t) => ({
    params: { slug: t.data.slug },
    props: { entry: t },
  }));
}

const { entry } = Astro.props;
const { Content } = await render(entry);
const faqs = extractFAQs(entry.body || '');
---

<ArticleLayout title={entry.data.title} description={entry.data.description} keywords={entry.data.keywords} lastUpdated={entry.data.lastUpdated} faqs={faqs} ogImage={entry.data.ogImage}>
  <Content />
</ArticleLayout>
```

- [ ] **Step 3: Build and verify FAQs still emit on topic pages**

Run: `cd site && npm run build`
Expected: build succeeds with no errors.

Run: `grep -o 'FAQPage' site/dist/topics/claude-code-guide/index.html | head -1`
Expected: one match (FAQPage schema still present).

- [ ] **Step 4: Commit**

```bash
git add site/src/lib/extract-faqs.ts "site/src/pages/topics/[...slug].astro"
git commit -m "refactor: extract extractFAQs into shared helper"
```

---

### Task 2: Add `.md` companion route for topics

Astro routes ending in `.md.ts` produce arbitrary file responses at the matching path. We emit a clean Markdown response with a small frontmatter-style header (title, description, last updated, source URL) followed by the raw body.

**Files:**
- Create: `site/src/pages/topics/[slug].md.ts`

- [ ] **Step 1: Create the static endpoint**

```typescript
// site/src/pages/topics/[slug].md.ts
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
```

- [ ] **Step 2: Build and verify .md file is generated**

Run: `cd site && npm run build`
Expected: build succeeds.

Run: `ls site/dist/topics/claude-code-guide.md`
Expected: file exists.

Run: `head -10 site/dist/topics/claude-code-guide.md`
Expected: starts with `# The Complete Guide to Claude Code...`, then blockquote description, `Last updated: 2026-04-10`, source URL, `---`.

- [ ] **Step 3: Commit**

```bash
git add "site/src/pages/topics/[slug].md.ts"
git commit -m "feat: serve .md companion route for topic pages"
```

---

### Task 3: Add `.md` companion route for blog

Same pattern as Task 2, applied to blog posts.

**Files:**
- Create: `site/src/pages/blog/[slug].md.ts`

- [ ] **Step 1: Create the static endpoint**

```typescript
// site/src/pages/blog/[slug].md.ts
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
```

- [ ] **Step 2: Build and verify**

Run: `cd site && npm run build`
Run: `ls site/dist/blog/dark-flow-vibe-coding.md`
Expected: file exists.

Run: `head -8 site/dist/blog/dark-flow-vibe-coding.md`
Expected: starts with `# Dark Flow: Why Vibe Coding...`, then blockquote, then `Published: 2026-04-11`, `Last updated: 2026-04-12`, source URL, `---`.

- [ ] **Step 3: Commit**

```bash
git add "site/src/pages/blog/[slug].md.ts"
git commit -m "feat: serve .md companion route for blog posts"
```

---

### Task 4: Add `.md` companion route for glossary

**Files:**
- Create: `site/src/pages/glossary/[slug].md.ts`

- [ ] **Step 1: Create the static endpoint**

```typescript
// site/src/pages/glossary/[slug].md.ts
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
```

- [ ] **Step 2: Build and verify**

Run: `cd site && npm run build`
Run: `ls site/dist/glossary/dark-flow.md`
Expected: file exists.

Run: `head -8 site/dist/glossary/dark-flow.md`
Expected: starts with `# Dark Flow`, then blockquote definition.

- [ ] **Step 3: Commit**

```bash
git add "site/src/pages/glossary/[slug].md.ts"
git commit -m "feat: serve .md companion route for glossary terms"
```

---

### Task 5: Add `.md` companion route for episodes

Episodes live in `episodes/` at the project root (per `site/src/content.config.ts:7`). The body contains a `<details>`-wrapped transcript section that we include verbatim — full content matters most for LLMs.

**Files:**
- Create: `site/src/pages/episodes/[slug].md.ts`

- [ ] **Step 1: Create the static endpoint**

```typescript
// site/src/pages/episodes/[slug].md.ts
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
```

- [ ] **Step 2: Build and verify**

Run: `cd site && npm run build`
Run: `ls site/dist/episodes/21-anthropic-mythos-project-glasswing-recursive-improving-agents-and-your-parallel-agent-limit.md`
Expected: file exists.

Run: `head -8 site/dist/episodes/21-anthropic-mythos-project-glasswing-recursive-improving-agents-and-your-parallel-agent-limit.md`
Expected: starts with `# Episode 21: Anthropic Mythos...`.

- [ ] **Step 3: Commit**

```bash
git add "site/src/pages/episodes/[slug].md.ts"
git commit -m "feat: serve .md companion route for episodes"
```

---

### Task 6: Advertise markdown alternates via `<link rel="alternate">`

`BaseLayout.astro` learns an optional `mdPath` prop. The three content layouts (Article, Episode, Glossary) compute the markdown path from `Astro.url.pathname` and pass it through. The homepage and listing pages don't pass it (no markdown alternate).

**Files:**
- Modify: `site/src/layouts/BaseLayout.astro`
- Modify: `site/src/layouts/ArticleLayout.astro`
- Modify: `site/src/layouts/EpisodeLayout.astro`
- Modify: `site/src/layouts/GlossaryLayout.astro`

- [ ] **Step 1: Add `mdPath` prop to BaseLayout**

In `site/src/layouts/BaseLayout.astro`, update the `Props` interface:

```typescript
interface Props {
  title: string;
  description?: string;
  schema?: Record<string, unknown> | Record<string, unknown>[];
  ogType?: string;
  canonicalUrl?: string;
  ogImage?: string;
  keywords?: string;
  publishedDate?: string;
  mdPath?: string;
}
```

Add `mdPath` to the destructuring:

```typescript
const {
  title,
  description = 'Artificial Developer Intelligence — a weekly podcast where practicing engineers navigate AI-enabled software development.',
  schema,
  ogType = 'website',
  canonicalUrl,
  ogImage,
  keywords,
  publishedDate,
  mdPath,
} = Astro.props;
```

After the existing `<link rel="canonical" ...>` line in `<head>`, add:

```astro
{mdPath && <link rel="alternate" type="text/markdown" title="Markdown version" href={mdPath} />}
```

- [ ] **Step 2: Pass mdPath from ArticleLayout**

In `site/src/layouts/ArticleLayout.astro`, in the frontmatter (just before the closing `---`):

```typescript
const mdPath = Astro.url.pathname.replace(/\/$/, '') + '.md';
```

Update the BaseLayout invocation to add `mdPath={mdPath}`:

```astro
<BaseLayout title={title} description={description} schema={schemas} ogType="article" keywords={keywords} publishedDate={date} ogImage={ogImage} mdPath={mdPath}>
```

- [ ] **Step 3: Pass mdPath from EpisodeLayout**

In `site/src/layouts/EpisodeLayout.astro`, in the frontmatter:

```typescript
const mdPath = Astro.url.pathname.replace(/\/$/, '') + '.md';
```

Update the BaseLayout invocation:

```astro
<BaseLayout title={`Ep ${episode}: ${title}`} description={description} schema={episodeSchema} ogType="article" mdPath={mdPath}>
```

- [ ] **Step 4: Pass mdPath from GlossaryLayout**

In `site/src/layouts/GlossaryLayout.astro`, in the frontmatter:

```typescript
const mdPath = Astro.url.pathname.replace(/\/$/, '') + '.md';
```

Update the BaseLayout invocation:

```astro
<BaseLayout title={term} description={definition} schema={definedTermSchema} mdPath={mdPath}>
```

- [ ] **Step 5: Build and verify**

Run: `cd site && npm run build`
Run: `grep 'rel="alternate" type="text/markdown"' site/dist/topics/claude-code-guide/index.html`
Expected: one match with `href="/topics/claude-code-guide.md"`.

Run: `grep 'rel="alternate" type="text/markdown"' site/dist/blog/dark-flow-vibe-coding/index.html`
Expected: one match.

Run: `grep 'rel="alternate" type="text/markdown"' site/dist/index.html`
Expected: no match (homepage has no markdown alternate).

- [ ] **Step 6: Commit**

```bash
git add site/src/layouts/
git commit -m "feat: advertise markdown alternates via link rel=alternate"
```

---

### Task 7: Generate /llms-full.txt at build time

Single static endpoint at the site root that concatenates all topics + blog + glossary content into one file. Per Evil Martians' adoption data, `/llms-full.txt` gets 3-4× more LLM traffic than `/llms.txt`.

**Files:**
- Create: `site/src/pages/llms-full.txt.ts`

- [ ] **Step 1: Create the static endpoint**

```typescript
// site/src/pages/llms-full.txt.ts
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
```

- [ ] **Step 2: Build and verify**

Run: `cd site && npm run build`
Run: `ls -la site/dist/llms-full.txt`
Expected: file exists, size > 100KB.

Run: `head -10 site/dist/llms-full.txt`
Expected: starts with `# ADI Pod — Full Content for AI Systems`, then blockquote, then `# Topics`.

Run: `grep -c '^## ' site/dist/llms-full.txt`
Expected: ~39 matches (6 topics + 17 blog + 16 glossary; exact number may vary as content is added).

- [ ] **Step 3: Commit**

```bash
git add site/src/pages/llms-full.txt.ts
git commit -m "feat: generate /llms-full.txt with all topics, blog, glossary"
```

---

### Task 8: Add FAQ extraction to blog posts

`site/src/pages/blog/[...slug].astro` doesn't pass `faqs` to ArticleLayout, so blog posts skip the `FAQPage` schema even when they have a "Frequently Asked Questions" section. Reuse the helper from Task 1.

**Files:**
- Modify: `site/src/pages/blog/[...slug].astro`

- [ ] **Step 1: Import the helper and pass faqs to ArticleLayout**

Replace the entire `site/src/pages/blog/[...slug].astro` with:

```astro
---
import { getCollection, render } from 'astro:content';
import ArticleLayout from '../../layouts/ArticleLayout.astro';
import { extractFAQs } from '../../lib/extract-faqs';

export async function getStaticPaths() {
  const posts = await getCollection('blog');
  return posts.map((post) => ({
    params: { slug: post.data.slug },
    props: { entry: post },
  }));
}

const { entry } = Astro.props;
const { Content } = await render(entry);
const faqs = extractFAQs(entry.body || '');
---

<ArticleLayout title={entry.data.title} description={entry.data.description} date={entry.data.date} keywords={entry.data.keywords} lastUpdated={entry.data.lastUpdated} faqs={faqs}>
  <Content />
</ArticleLayout>
```

- [ ] **Step 2: Check whether any blog posts currently have FAQ sections**

Run: `grep -l "## Frequently Asked Questions" site/src/content/blog/*.md`
Expected: zero or more matches. If zero, this change is harmless and ready for future posts. If non-zero, those posts will gain `FAQPage` schema.

- [ ] **Step 3: Build and verify**

Run: `cd site && npm run build`
Run: `grep -l 'FAQPage' site/dist/blog/*/index.html | wc -l`
Expected: matches the count from Step 2 (zero or more).

- [ ] **Step 4: Commit**

```bash
git add "site/src/pages/blog/[...slug].astro"
git commit -m "feat: extract FAQs from blog posts for FAQPage schema"
```

---

### Task 9: Reference new resources from llms.txt

The existing `site/public/llms.txt` should mention the new `.md` routes and `/llms-full.txt` so AI tools that fetch `/llms.txt` know they're available.

**Files:**
- Modify: `site/public/llms.txt`

- [ ] **Step 1: Add a "For AI Systems" section**

Append to the end of `site/public/llms.txt` (after the "Original Concepts" section):

```markdown

## For AI Systems

Every content page has a clean Markdown companion at the same URL with `.md` appended:

- https://adipod.ai/topics/claude-code-guide.md
- https://adipod.ai/blog/dark-flow-vibe-coding.md
- https://adipod.ai/glossary/dark-flow.md
- https://adipod.ai/episodes/21-anthropic-mythos-project-glasswing-recursive-improving-agents-and-your-parallel-agent-limit.md

For all topics, blog posts, and glossary terms in a single file: https://adipod.ai/llms-full.txt
```

- [ ] **Step 2: Build and verify**

Run: `cd site && npm run build`
Run: `grep -A 1 'For AI Systems' site/dist/llms.txt`
Expected: the new section appears.

- [ ] **Step 3: Commit**

```bash
git add site/public/llms.txt
git commit -m "docs: link .md routes and llms-full.txt from llms.txt"
```

---

## Self-Review

**Spec coverage:** Audit identified P0 items (1-4) and P1 items (5, 7). All in-scope items covered:
- P0 #1 (.md routes for content pages): Tasks 2, 3, 4, 5
- P0 #2 (`<link rel="alternate">`): Task 6
- P0 #3 (`/llms-full.txt`): Task 7
- P1 #5 (FAQ extraction on blog): Tasks 1 + 8
- Bonus (Task 9): updates llms.txt to point at new resources

Out of scope and deferred (documented in plan header): P0 #4 (homepage OG, blocked on missing image), P1 #6 (HTTP `Link` header, needs CF Functions), P1 #7 (`PodcastSeries.webFeed`, needs RSS URL), P1 #8 (host bio thickening, content work), P2 items.

**Placeholder scan:** None. Every step has the actual code or command needed.

**Type consistency:**
- `extractFAQs(body: string): FAQ[]` defined in Task 1, consumed in Tasks 1 (Step 2) and 8 (Step 1) — signatures match.
- `mdPath?: string` prop defined on `BaseLayout` in Task 6 Step 1, passed by all three content layouts in Steps 2-4 — name matches.
- `entry.body` accessed consistently across all `.md.ts` endpoints (Tasks 2-5) — this is the standard property name on Astro 5 content collection entries (already used in `site/src/pages/topics/[...slug].astro:52`).
- `entry.data.slug` accessed consistently — matches the field defined in `site/src/content.config.ts` for every collection.
