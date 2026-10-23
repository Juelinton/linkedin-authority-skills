# Style

Your taste. **This file overrides every technical rule in the repo.** Best practice that fights the
author's signature produces posts nobody believes.

Copy to `linkedin-voice/style.md` and edit, or run `/setup-voice`.

The defaults below are opinionated on purpose. They exist because a text that follows all of them
stops reading as machine-written. Turn off anything you disagree with, the skills follow this file.

---

## Hard rules

These are enforced by `tools/sanitize.py` and re-checked by every skill.

- [x] **No em dashes or en dashes** (— –) anywhere. The single most reliable tell of generated text.
      Use a comma or a full stop.
- [x] **No markdown in the final output.** Asterisks, underscores, backticks and headings render
      literally on LinkedIn. Emphasis comes from word choice, not syntax.
- [x] **No semicolons.** Split the sentence.
- [x] **No false dichotomies.** "It's not about X, it's about Y" is flagged as low originality.
- [x] **No preamble, no sign-off.** The first word delivered is the first word of the post.
- [x] **At most one emoji**, preferably none.
- [x] **No engagement bait.** No "comment below", no "thoughts?", no "agree?".

## Authority

- [x] **No credential-dropping.** Authority comes from the precision of the observation, not the CV.
      Wrong: "In twenty years running telecom operations, I've seen...". Right: "The pattern repeats
      with almost mathematical regularity."
- [ ] **Credentials allowed.** [Check this instead if your audience does not know you yet and the
      credential is the fastest way to earn a reading. Both choices are defensible, pick one.]

## Generosity

- [x] **Always concede value to the profile being criticized.** A piece that shuts the door on people
      who operate differently reads as a manifesto and loses the reader you wanted to convert.

## Hashtags

- **How many:** 3 to 5, at the end of the text.
- **Strategy:** repeat two anchor tags across pieces in the same thematic pillar and vary the third,
  so the platform associates your profile with the subject without the list looking like a stamp.

## Rhythm

[How your sentences move. Fill this in from your own writing rather than aspiration.

Examples:
- "Short sentences. Two per paragraph, never three."
- "Dense paragraphs, four to six sentences, board-memo register."
- "First person, past tense, concrete scenes before abstraction."]

## Words I have banned

[Grows over time. Every time a draft uses a word that makes you wince, add it here. This list is
what makes the output converge on your voice instead of drifting back to the average.]

-

## Formulations that are mine

[Phrases, framings and structures you have earned. The skills will reuse them instead of inventing
near-misses.]

-

## The spacer character

LinkedIn's editor collapses consecutive blank lines. `⠀` (U+2800, braille pattern blank) survives as
a visible blank line and is preserved by `tools/sanitize.py`.

- [ ] Use `⠀` between blocks for extra breathing room.
