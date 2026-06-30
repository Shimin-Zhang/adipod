import { getCollection } from 'astro:content';

export async function episodesByNumbers(numbers: string[]) {
  const all = await getCollection('episodes');
  return numbers
    .map((n) => all.find((e) => e.data.episode === n))
    .filter((e): e is NonNullable<typeof e> => e !== undefined)
    .map((e) => ({
      number: e.data.episode,
      slug: e.data.slug,
      title: e.data.title,
    }));
}

export async function blogPostsForEpisode(episodeNumber: string) {
  const all = await getCollection('blog');
  return all
    .filter((p) => p.data.episodes?.includes(episodeNumber))
    .map((p) => ({
      slug: p.data.slug,
      title: p.data.title,
      description: p.data.description,
    }));
}

export async function glossaryTermsForEpisode(episodeNumber: string) {
  const all = await getCollection('glossary');
  return all
    .filter((t) => t.data.episodes?.includes(episodeNumber))
    .map((t) => ({
      slug: t.data.slug,
      term: t.data.term,
    }));
}

export async function blogPostsMentioningGlossaryTerm(slug: string) {
  const all = await getCollection('blog');
  const linkPath = `/glossary/${slug}/`;
  return all
    .filter((p) => (p.body || '').includes(linkPath))
    .map((p) => ({
      slug: p.data.slug,
      title: p.data.title,
    }));
}
