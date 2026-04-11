---
term: "Workflow Automation Convexity"
definition: "The observation that AI-driven automation follows a convex payoff curve -- producing minimal impact on jobs during a long initial phase, then triggering sudden, near-complete displacement once AI can handle entire connected workflows rather than isolated tasks."
slug: "workflow-automation-convexity"
episodes: ["14"]
aliases: ["automation convexity"]
---

## Context

The concept draws on Philip Trammell's [Workflows and Automation](https://philiptrammell.com/static/Workflows_and_Automation.pdf) paper and was discussed on [Episode 14](/episodes/14-crabby-rathbun-model-councils-why-you-want-more-tech-debt) of the ADI Pod during a broader, economics-flavored segment on AI job displacement, comparative advantage, and the Jevons paradox.

In finance and options pricing, convexity describes a payoff that is not proportional to the input -- small moves produce little effect, but past a threshold the response accelerates sharply. Applied to automation, the insight is structural: most real-world work is organized as chains of interdependent tasks, not standalone units. Automating 9 out of 10 steps in a workflow still requires a human for the remaining step, so the workflow cannot run autonomously and headcount barely changes. Once the final step is also automated, the entire chain can execute without human involvement, and the labor impact arrives all at once.

## Why It Matters

Linear forecasts of AI job displacement -- "AI can do X% of tasks, so X% of jobs will go away" -- miss this dynamic. Optimistic accounts like David Oks' [Why I'm not worried about AI job loss](https://davidoks.blog/p/why-im-not-worried-about-ai-job-loss) lean on comparative advantage to argue humans will always find new roles, but Trammell's convexity framing shows that reallocation logic breaks down once full workflows, not just tasks, become automatable. Job losses can appear negligible for years and then arrive abruptly once capability gaps close. Partial automation often creates more work (coordinating human-AI handoffs, reviewing AI output, handling edge cases) rather than less.

For engineering teams, the practical implication is that automating individual tasks -- code generation, test writing, documentation -- does not automatically translate into fewer engineers. The gains arrive when AI can own a connected workflow end to end: from ticket to shipped, tested, monitored feature. Until that threshold is crossed, the main effect is a reshuffling of what developers spend their time on, not a reduction in headcount.

## Related Concepts

- [Cognitive debt](/glossary/cognitive-debt) -- the hidden cost that accumulates when AI handles tasks humans no longer fully understand
- [The middle loop](/glossary/the-middle-loop) -- the oversight layer that exists precisely because current automation is partial, not end-to-end
