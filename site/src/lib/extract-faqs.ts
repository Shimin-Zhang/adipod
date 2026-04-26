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
