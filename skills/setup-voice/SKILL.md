---
name: setup-voice
description: Interview the user and build their voice profile, the three files every other skill in this repo reads. Use when the user installs these LinkedIn skills for the first time, when a skill reports that linkedin-voice/ is missing, or when the user wants to update who they are, what niche they write for, or their style rules. Run this before writing anything.
---

# Build the voice profile

Every other skill here reads three files from `linkedin-voice/` in the project root:
`persona.md`, `niche.md`, `style.md`. Without them the output is competent and generic, which is
worth nothing on a feed. This skill produces them by interview.

**Templates and a filled reference sit in `voice/` in this repo.** Read `voice/example/filled-example.md`
before you start, so you know the level of specificity you are aiming for.

## How to run this

Conversational, not a form. **Ask two or three questions at a time and react to the answers.** A
plain 20-question dump gets 20 shallow answers, and shallow answers are exactly what makes generated
content sound like everyone else's.

Two rules that decide whether this works:

1. **Push back on vague answers, once.** "B2B decision makers" is not a reader. "Enterprise software"
   is not a niche. Ask the follow-up: who specifically, what are they measured on, what did the last
   one you talked to complain about. Take the second answer even if it is still imperfect.
2. **Never invent anything.** If the user cannot answer, leave the section empty with a note. An
   empty section is honest and the skills handle it. An invented one poisons every post from here on.

## The interview

### Part 1, who is writing (→ `persona.md`)

- What does your LinkedIn headline say right now? Paste it.
- What do you actually get called in to do? Say it like you would to a stranger, not like a CV.
- What three topics do you want to be known for? **Push for narrow.** If they give a category, ask
  which specific fight inside it they have opinions about.
- **The important one:** what have you actually lived that someone reading about this online has
  not? Situations, failures, numbers, things that went wrong. Ask for three. This becomes every
  credibility signal in every future post, so spend the most time here.
- Where does your experience run out? What should the skills refuse to assert on your behalf?
- How do you feel about naming your employer in public writing? Default is at most once per piece.

### Part 2, who they write for (→ `niche.md`)

- Describe one reader. Their role, what they are measured on, what their week looks like.
- What does that person already believe about your topic? What is the advice they have heard a
  hundred times?
- **What is the enemy?** Not a competitor, a force. Organizational inertia, audit theater, vanity
  metrics. If they cannot name it, offer two or three candidates drawn from what they have already
  told you and let them pick or reject.
- What do you believe that a competent peer could disagree with?
- What jargon does your reader use daily? What words mark someone as an outsider?
- If you write in a language other than English, which terms stay in English anyway because that is
  how your market speaks?
- What numbers or studies are you allowed to cite publicly?
- What topics interest you but are off-niche? (This lets `/topic-score` push back honestly.)

### Part 3, taste (→ `style.md`)

Start from the defaults in `voice/style.md` and confirm rather than asking open questions. Most
people have never articulated their style rules and will produce better answers by reacting.

- Walk through the hard rules and ask which they want off. Explain the em dash one, since it is the
  most useful and the least obvious: it is the single most reliable marker of generated text.
- Credential-dropping: allowed or banned? Both are defensible. Banned is the default, and it is the
  right default for someone whose audience already knows them. Allowed is better when the reader has
  never heard of them and the credential buys the first ten seconds of attention.
- Hashtags: how many, and are there anchor tags to repeat across pieces?
- **Ask for two or three of their own posts, or anything they have written.** Read them and propose
  the rhythm section back to them for correction. Observing beats asking, because people describe the
  writing they wish they did rather than the writing they do.
- Any words that make them wince?

## Writing the files

1. Create `linkedin-voice/` in the project root.
2. Write `persona.md`, `niche.md`, `style.md` following the structure of the templates in `voice/`.
3. **Write only what the user actually said.** Where a section is empty, say so in the file:
   `[not yet answered, ask before relying on this]`.
4. Show the three files and ask for corrections. Expect the enemy and the position sections to need
   a second pass, those are the hardest to get right and the most valuable when they land.

Then tell them what to run next: `/topic-score` to check an idea, `/linkedin-post` to write one.

## When to re-run

The profile is meant to grow. Tell the user to come back and edit `style.md` directly whenever a
draft uses a word that makes them wince, and to add to the evidence list in `persona.md` whenever
something worth writing about happens. That list is the scarcest input in the whole system.
