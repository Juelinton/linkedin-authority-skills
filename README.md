# LinkedIn Authority Skills

Seven Claude Code skills for writing LinkedIn content that does not read as machine-written, plus a
deterministic sanitizer that strips the tells even when the model slips.

The point is not to generate posts. Anything generates posts. The point is that the output sounds
like **you**, because you spend five minutes teaching it who you are and it refuses to invent the
rest.

---

## The sanitizer

Start here, because it is useful on its own and needs nothing installed.

```bash
python3 tools/sanitize.py post.txt
```

Pure stdlib Python. No dependencies. Works on English and Portuguese.

A prompt alone does not hold. Tell a model "never use em dashes" and it will still ship one on
paragraph nine, because instruction-following degrades across a long generation. So this runs after
the model, deterministically, on the finished text. It does three things and keeps them separate:

**FIXED**, mechanical artifacts where removal cannot change meaning. Em and en dashes, asterisks,
backticks, `_italic_`, markdown headings that LinkedIn renders as literal `##`, conversational
preamble, sign-offs, spacing.

**REWRITE**, things a regex must not touch. It cannot replace a semicolon without breaking the
sentence, so it reports and exits 1 instead of guessing. This is the gate.

**NOTICES**, ambiguous slop patterns. It names the pattern, quotes the line, suggests a fix, and
never blocks. Throat-clearing openers, faux-insight setups, colon reveals, weasel attribution,
both-sides hedging, audience flattery, and a dozen more.

```bash
python3 tools/sanitize.py --check post.txt   # audit only, change nothing
cat post.txt | python3 tools/sanitize.py -   # stdin to stdout
```

It preserves `⠀` (U+2800), the braille blank many LinkedIn writers use to keep the editor from
collapsing their blank lines.

---

## The skills

| Skill | What it does |
|---|---|
| `/setup-voice` | Interviews you and builds your voice profile. **Run this first.** |
| `/topic-score` | Scores a topic 0-10 before you spend an afternoon on it. Blunt on purpose. |
| `/linkedin-post` | A feed post in one of seven style variants, plus outlier mode |
| `/linkedin-article` | Long-form, 800-2500 words, built for search and for the reader who stays |
| `/linkedin-carousel` | Slide script for a document post, the PDF carousel readers save and come back to |
| `/linkedin-comment` | Three comments for someone else's post, written as a peer |
| `/linkedin-dm` | Three DMs, with the ask deliberately held back until the relationship earns it |

---

## Install

The repo is a Claude Code plugin marketplace. Inside Claude Code, run:

```
/plugin marketplace add Juelinton/linkedin-authority-skills
/plugin install linkedin-authority@juelinton-skills
```

The skills load with the plugin's name as a prefix, so `/setup-voice` runs as
`/linkedin-authority:setup-voice`. The sanitizer and the reference ship inside the plugin, and the
skills find them on their own.

Then, in the project directory where you want to write:

```
/linkedin-authority:setup-voice
```

To try it from a clone first, start Claude Code with `claude --plugin-dir ./linkedin-authority-skills`.

---

## How it works

Every skill reads three files from `linkedin-voice/` in your project root:

| File | What it holds |
|---|---|
| `persona.md` | Who is writing. Your pillars, and the lived experience every credibility signal draws on. |
| `niche.md` | Who you write for, what they already believe, and the enemy your content fights. |
| `style.md` | Your taste. **This file overrides every technical rule in the repo.** |

`/setup-voice` writes them by interview. You can also copy the templates from `voice/` and fill them
in by hand. A filled reference profile sits in `voice/example/`, worth reading for the level of
specificity, which is the difference between output that sounds like you and output that sounds like
LinkedIn.

Two design decisions worth stating, because they are what make this different from a prompt library:

**Personal taste beats best practice.** `style.md` wins every conflict. Advice that fights the
author's signature produces posts nobody believes, and the whole system is built to lose that
argument on purpose.

**Nothing gets invented.** `persona.md` has a section for where your experience runs out. The skills
will ask you rather than fabricate a statistic or a war story. This is the single most important
constraint here, since a fabricated credential in public is worse than a boring post.

---

## The reference

`reference/linkedin-algorithm.md` is a synthesis of how the feed appears to rank, in seven operating
specs: profile alignment, dwell time, hooks, conversation design, format selection, anti-slop and
semantic SEO. The skills pull from it as needed and you do not have to read it to use them.

It is compiled from about 70 public sources: LinkedIn's own engineering papers on arXiv, independent
algorithm research, and public work by practitioners who study the platform full time. Sources are
credited at the bottom of that file. Everything came from freely published material. LinkedIn has
confirmed none of it, and the numbers are third-party, so read them as direction.

**Sources last reviewed April 2026, links checked October 2026.** Reviewed when LinkedIn engineering
publishes a new ranking paper, or roughly quarterly.

Your own analytics beat this document. Thirty of your own measured posts
tell you more about your account than seventy articles about the platform. Where they disagree, your
numbers win.

---

## What this will not do

- **It will not post for you.** Every skill delivers text for your approval. Nothing here touches an
  API or a logged-in session, by design.
- **It will not make you interesting.** It removes the machine tells and enforces your structure. The
  substance is yours, and if `persona.md` is thin the output will be too.
- **It will not survive being used lazily.** Fill the profile properly or you get competent generic
  text, which is the one outcome not worth the tokens.

---

## Credits

The anti-slop pattern set is adapted from [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) (MIT), with its license reproduced in `THIRD_PARTY_NOTICES.md`.

The writing specs draw on the public work of **Richard van der Blom** (Just Connecting), **Jasmin
Alić** and **Michelle J Raymond**, alongside LinkedIn's own published research. Full list in
`reference/linkedin-algorithm.md`.

Built by [Juelinton Silveira](https://www.linkedin.com/in/juelinton/). If you use this, I would like to see what you make
with it.

MIT licensed. Fork it, gut it, make it yours. That is the point.
