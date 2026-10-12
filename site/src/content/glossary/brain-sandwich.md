---
term: "Brain Sandwich"
definition: "A rule for AI-assisted work: use your brain before you prompt (understand the problem and roughly where you're going), let the AI do the middle, then use your brain again before anyone else sees the result. If you can't explain what changed and why, it isn't ready."
slug: "brain-sandwich"
episodes: ["42"]
aliases: ["brain-AI-brain", "brain AI brain", "AI lasagna"]
---

## Context

The term comes from Matheus Lima's post [The Brain Sandwich](https://terriblesoftware.org/2026/10/02/the-brain-sandwich/) on his blog Terrible Software, which Shimin brought to the return of Technique Corner in [Episode 42](/episodes/42-ai-safetys-conflict-of-interest-gemini-4-argon-the-brain-sandwich-agent-trading/). Lima credits the idea to Emily, one of his strongest engineers, from a 1:1 about what AI is doing to engineering work. The top slice: read and understand the problem before involving AI. You don't need a full implementation plan, just "a rough idea of where you're going." The filling: delegate the build, "with no shame." The bottom slice: review the output before sharing it, because "if you can't explain what's changing and why, it's not ready for someone else to take a look."

## Why It Matters

The show keeps arguing for AI that augments your thinking rather than replacing it. The sandwich is the shortest way to say that to someone else, and Shimin's case for it is that it covers several of the show's pet peeves at once. The bottom slice is what stops [slop grenades](/glossary/slop-grenade) and 40,000-line PRs nobody read.

The top slice is the one people skip, and it matters most for code review. Dan doesn't trust same-model review: when Opus reviews Opus's code, the reviewer shares the writer's blind spots, and he gets better results from a different provider's model. Shimin's extension is that if the writer and the reviewer make the same wrong assumption, only the human who thought about the problem first can catch it. So all three layers have to be there, even when an AI does the first pass of review.

Shimin thinks the real process is closer to a lasagna: alternating layers of human thinking and AI, wrapped in the harness, which plays the tomato sauce. The same episode supplied a formal version of the bottom slice. Scott Aaronson [writes](https://scottaaronson.blog/?p=10062) that math papers now arrive with statements like "our main result came entirely from GPT-6, but we understood it and take responsibility for it." That's a disclosure norm built around the last slice: the AI can do the work, but a person has to understand it and own it.

## Example

Dan's Vibe and Tell in the same episode was the sandwich in hardware. He wanted Halloween ghouls whose eyes follow trick-or-treaters, and he knew from Home Assistant that a millimeter-wave radar could do it. Claude picked the microcontrollers and wrote all the code, which Dan never wanted to read. When the eyes misbehaved, the fix came from the bottom slice: Dan read the radar's datasheet and found he'd mounted it 90 degrees off. The model couldn't have caught that. It never saw the board.

## Related Concepts

- [Cognitive surrender](/glossary/cognitive-surrender) -- what you get when both slices of bread go missing and the AI's answer becomes the decision
- [Slop grenade](/glossary/slop-grenade) -- the result of skipping the bottom slice and forwarding unread output
- [Verification debt](/glossary/verification-debt) -- the cost that builds up when the bottom slice gets skipped on code
- [Metacognitive decoupling](/glossary/metacognitive-decoupling) -- why the bottom slice is harder than it looks: fluent output feels understood when it isn't
