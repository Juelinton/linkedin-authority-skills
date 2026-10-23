---
name: linkedin-article
description: Write a long-form LinkedIn article or newsletter issue (800-2500 words) in the author's voice, as an authored executive analysis rather than a long post. Use when the user asks for an article, a long analysis, or a newsletter piece, or wants to turn a dense subject into long-form authority content. For a short feed post use linkedin-post.
---

# LinkedIn article

Long-form has **three jobs**, and virality is not one of them: index the author as a specialist
vector in the interest graph, convert readers into subscribers, and rank on Google for the technical
terms of the niche.

**Mental model:** a short McKinsey report, written in first person, by someone who worked the field.
**It is not** a long version of the short post. It is a different editorial product.

## Before writing

Read `linkedin-voice/persona.md`, `niche.md` and `style.md`. `style.md` wins any conflict below.
If `linkedin-voice/` is missing, stop and point at `/linkedin-authority:setup-voice`.

Relevant depth: `${CLAUDE_PLUGIN_ROOT}/reference/linkedin-algorithm.md`, spec 7 (semantic SEO) matters most here, because
an article that ranks keeps working for months after the feed forgets it.

## Headline, diagnostic never promise

| Wrong (generic promise) | Right (diagnosis with friction) |
|---|---|
| "How to sell more" | "Why 70% of infrastructure GTMs fail moving to a value model" |
| "5 tips for closing deals" | "The blind spot that kills enterprise deals in the last mile" |
| "The secrets of X" | "Organizational inertia is not a bug, it is the buyer's immune system" |

Formula: **[a real tension in the niche] + [numeric or conceptual specificity]**.

## Structure (proportions for ~1500 words)

| Section | % | Contents |
|---|---|---|
| Headline | 1 line | Diagnostic, with friction |
| Editorial opening | 10-15% | Hook plus market tension, no H2 |
| Central thesis | 3-5% | "I argue X. Here is why." |
| Diagnosis | 25-30% (2-3 H2) | Includes proprietary data or a counter-consensus insight |
| Framework / analysis | 25-30% (1 H2) | Numbered list or A/B comparison |
| Real case | 10-15% | Anonymized, with a signal of the author's experience |
| Practical implication | 10-15% (1 H2) | Three to five concrete actions |
| Close plus CTA | 5% | Technical question, then the subscription invitation |

**One H2 roughly every 300 words**, for visual anchoring.

## Signposting

Every technical claim needs a signal of real experience **from the profile**. Draw it from the
evidence list in `persona.md`: "Based on what I saw running [function]...", "When I was responsible
for [scope]...". Respect the company-name rule in `persona.md`, which defaults to at most one
mention in the whole article and preferably none.

## Proprietary data, strong preference not a blocker

Try to include one figure or percentage that validates the thesis, drawn from the public-proof list
in `niche.md`. With no public figure available, use lived experience ("in what I saw running X, this
shows up in roughly Y% of cases"). If neither is possible, write the article anyway and append:
`[note: no proprietary data in this piece, consider validating against an external source before
publishing]`.

Never invent a statistic. Weasel attribution ("studies show") is worse than having no number.

## Close

**A specific technical question** that provokes a dense comment, never "what do you think?" and never
"comment below". Example: *"For those operating in committees of five or more stakeholders: what was
the last deal you lost to a political veto rather than on merit? How did you handle it?"*

**Subscription CTA** on the last line, pulling the article's own subject: *"If you work on [subject]
and want more analysis like this, subscribe."*

## Formatting and final check

LinkedIn does not render markdown. Output **plain text**. Run the sanitizer, not optional:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/tools/sanitize.py" article.txt
```

It fixes em dashes, asterisks, backticks and headings, and reports semicolons, false dichotomy,
emoji and engagement bait.

Then check by hand: signposting within the company-name limit · a technical question at the end ·
subscription CTA · vocabulary per `niche.md` · nothing asserted that `persona.md` rules out.

**Deliver for approval. Never publish.**
