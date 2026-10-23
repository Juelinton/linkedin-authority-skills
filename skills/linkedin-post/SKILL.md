---
name: linkedin-post
description: Write a LinkedIn feed post in the author's voice, in one of seven style variants (staccato, executive report, narrative prose, contrarian thesis, numbered list, socratic questions, short real case). Use when the user asks for a post, wants to turn an idea, news item or meeting into content, or asks for variations on a theme. Also covers outlier mode, inheriting the structure of a post that performed well and rewriting the contents. For long-form use linkedin-article.
---

# LinkedIn post

## Before writing

Read from `linkedin-voice/`:

- **`persona.md`** — you write **as** the author, not about them. The evidence list is where every
  credibility signal comes from.
- **`niche.md`** — the reader, the enemy, the vocabulary.
- **`style.md`** — taste. **This file wins any conflict with the rules below.**

If `linkedin-voice/` is missing, stop and point at `/setup-voice`. Writing against a generic profile
produces generic output, which is the one outcome worth avoiding.

Optional depth: `reference/linkedin-algorithm.md`, specs 2 (dwell time), 3 (hooks), 6 (anti-slop),
7 (semantic SEO).

**Ask which variant** if the user does not say. Default is **staccato**. Asking for several variants
of the same topic is the most common use, so offer it.

## The seven variants

### staccato — *default*
Mobile, high dwell time, aggressive hook. The hot take, the contrarian announcement.

- Line 1: contrarian or specificity hook. One sentence, direct.
- Body: **one or two sentences per block. Never three grouped.** Double line break between blocks.
- Should read as small mobile-friendly steps.
- Show lived experience without naming a company. Closing invitation asks for the reader's own story.

### executive_report
Cold, data-led, dense paragraphs. Trend assessment, pure authority.

- Open with a cold assertion, **no curiosity hook**. Start at the fact.
- Dense paragraphs, four to six sentences. No decorative line breaks.
- Percentage, number or ratio wherever one can anchor the claim. Estimates are fine, marked as such.
- Sequence: context → mechanical analysis → practical implication → operational recommendation.
- Register of a board memo. Declarative, present tense, **no colloquialism**.
- Close with something usable tomorrow, plus a question about the reader's own experience.

### narrative_prose
Storytelling. A real situation, a lived lesson. Warm voice, first person.

- Open with a scene that puts the reader inside it. Time, place, gesture. *"It was Wednesday. The
  meeting was at two."*
- Characters **anonymized** ("the CTO", "the head of sales"). Never a real name.
- Tension → turn → **implied lesson**.
- **Never write "the lesson is..."** The moral emerges from what happened.
- Sensory detail earns its place: the exact sentence someone said, the long pause.
- Paragraphs of two to three sentences. More air than the report, less than staccato.

### contrarian_thesis
Strong claim plus three numbered reasons. Generates the most comment volume.

- Line 1: a strong, declarative, counter-intuitive claim.
- Line 2: *"I hold this for three reasons."*
- `1.` `2.` `3.` — two to three sentences each.
- Close: *"I could be wrong. But in [lived context], this is what I have seen work."*
- Invitation: a question that asks the reader to disagree **with an argument**.
- **The thesis has to be defensible and grounded in experience.** No provocation for its own sake.

### numbered_list
Scannable, saveable. A practical framework or checklist.

- Short hook, one or two sentences, naming the problem.
- Five to seven items. Each: `N. [short nameable concept]` + one or two sentences of explanation +
  one concrete example.
- Each item **self-contained**, so someone reading at random still gets it. The item name has to be
  quotable, meaning it could become a slide on its own.
- **No announce-then-list.** Never end the hook with a colon and a promise ("here are 5 mistakes:").
  Go straight to item 1.
- Close with "which of these do you still do?" or its equivalent.

### socratic_questions
Internal dialogue, provokes reflection. Low friction.

- The **whole** text is built from questions, with short answers implied in the body.
- Sequence: provocative question → micro-answer → deeper question → micro-answer → the question that
  exposes the contradiction → silence.
- Each question is its own paragraph. More air than staccato.
- **Do not answer everything.** The power is in what stays open.

### short_real_case
Mini-story with a payoff. *"I watched this happen last week..."* Three or four short paragraphs.

1. Temporal opening: *"Last month I watched a two million dollar deal die in thirty minutes."*
2. The case: three to five sentences, anonymized. Short characters ("the client", "the CFO").
3. The turn, and the lesson in **one quotable sentence**.
4. Invitation: *"If you have had something similar, I would like to hear how you handled it."*

- The lesson has to be **actionable**, something to use tomorrow. Not philosophical, no moralizing.

## Vocabulary

Follow the vocabulary section of `niche.md` exactly. Terms of art stay as the reader says them, even
when that means leaving English terms untranslated inside another language, because that is how the
market actually speaks. Generic words with a natural translation get translated.

If the user writes in a language other than English and `niche.md` has no vocabulary rules yet, ask
once and then write them into the file.

## Output rules

**The post is the deliverable. No wrapper.**

- The first word delivered is the first word of the post, which is the hook.
- The last line delivered is the last line of the post.
- **No** "Here is", "Here's", "Sure", "I've written", "Hope this helps".
- **No commenting on the chosen variant** inside the post.
- **No restating the topic** you were given.
- **No** code fences, no quotation marks wrapping the post, no wrapper of any kind.

Anything you need to say (why you picked a variant, what was missing) goes **after** the post,
separated. Never inside it.

This gets pasted straight into LinkedIn. Treat it as a `.txt` file, not a chat reply.

## Final check, not optional

The persona alone **fails**. Instruction-following degrades across a long generation, so a model will
ship an em dash it was explicitly told to avoid. That is why there is a deterministic pass after it.

**Write the post to a file and run:**

```bash
python3 tools/sanitize.py post.txt
```

It **fixes on its own** what is mechanical (em dashes, asterisks, backticks, headings, `_italic_`,
preamble, sign-off, spacing) and **reports** what needs your rewrite: semicolons, false dichotomy,
extra emoji, engagement bait. Exits 1 if anything needs rewriting.

Use `--check` to audit only, or `-` for stdin. It preserves `⠀` (U+2800).

**What it cannot see, and you must check:**

- [ ] Company names within the limit set in `persona.md`
- [ ] The closing asks for the reader's experience, not for a like
- [ ] Vocabulary follows `niche.md`
- [ ] Nothing asserted that `persona.md` lists under "things I will not claim"
- [ ] No wrapper, no commentary on style

**Hashtags:** follow `style.md`. Default is 3 to 5, short, at the end. Keep two anchor tags constant
across pieces in the same thematic pillar and vary the third, so the platform associates the profile
with the subject without the list reading as a stamp.

## Outlier mode

If the user supplies a reference post that performed well (3x their average or better), the goal is
to **inherit the validated frame and replace all of the contents**.

1. Analyze the structure silently: the first-line hook, narrative arc, length, rhythm, payoff type,
   list and break pattern.
2. **Keep the skeleton.** Structure is statistics, not authorship.
3. **Replace everything else**: topic, examples, data, anecdotes. All from the author's niche and
   lived experience.
4. **Never** keep a full sentence, an example, a proper noun or a number from the original.

**Hook mode** (ask, default is `adapt`):

- **verbatim** — a generic concept hook ("How to X", "Top N mistakes") has no owner. Use it nearly
  as-is, adapting only enough to read naturally. Keep the rhythm, the count and the syntax.
- **adapt** *(default)* — adapt to the niche while keeping the syntactic structure. *"How to escape
  beginner hell"* → *"How to escape a paralyzed buying committee."* Keep the "How to escape [bad
  thing]" pattern, swap the bad thing.
- **inspired** — the original hook carries the author's fingerprint (a proper noun, a very specific
  number, a unique story). Do not copy it. Write a new hook that inherits only the narrative shape.

**Not allowed:** literal sentence-by-sentence translation · keeping an example, name or number from
the original · lifting a mental image or rhetorical beat · "inspired by" sliding into a disguise the
original author would recognize as a copy.
