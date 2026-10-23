# How the LinkedIn feed ranks you

Seven operating specs. They describe **how to do the work well**, and apply to any output. They are
orthogonal to the skills in `skills/`, which decide **which artifact to produce**.

Read this when a skill points you here. You do not need to read it end to end to use the skills.

> **What this is.** A synthesis of public material: LinkedIn's own engineering papers, independent
> algorithm research, and public talks by practitioners who study the platform full time. It is not
> insider information and LinkedIn has confirmed none of it. Numbers below come from third-party
> studies, so treat them as direction, not as constants. Full source list at the bottom.
>
> **Sources last reviewed: April 2026.** Reviewed when LinkedIn's engineering team publishes a new
> ranking paper, or roughly every quarter, whichever comes first. Nothing here has changed
> architecturally since the 360Brew transition.
>
> **The strongest input is not in this file.** It is your own analytics. Thirty of your own posts,
> measured, tell you more about what works on your account than seventy articles about the platform.
> Where this document and your own numbers disagree, your numbers win.

---

## 1. Profile-content alignment

**Goal:** get the ranker to read you as a semantic authority on one thing, by keeping what your
profile *claims* and what your post *demonstrates* in the same lane.

**Mechanism:**
- Reach follows demonstrated depth on a topic, not network size. The interest graph outranks the
  social graph.
- The model reads your headline and About section as context when deciding whether a post travels
  past your immediate network.
- A complete profile (photo, location and industry, current role, two past roles, education, 5+
  skills, 50+ connections) is reported to carry a meaningful first-batch reach multiplier. An
  incomplete one carries a penalty.

**What to do:**
1. Audit the profile before writing. If the About section is empty or the headline is a bare job
   title ("Sales Manager") instead of an outcome ("I help SaaS companies scale channel revenue"),
   fix that before optimizing any post.
2. Pull three authority pillars out of the profile. That is your indexing niche.
3. Attach every technical claim to a signal of real experience. Generic advice reads as anyone's.

**Rules:** if a topic falls outside the authority pillars, say so before writing, because off-niche
posting dilutes the semantic signal. Never assert without grounding.

---

## 2. Dwell time and layout

**Goal:** structure rhythm and layout so readers stay, which is the signal that earns second and
third-degree distribution.

**Mechanism:**
- Time on post beats likes. Thirty seconds of reading is worth more than fifty fast reactions.
- Two phases: before the "see more" cut, and after it.
- **Click bounce.** Expanding a post and leaving within a few seconds marks it as clickbait and cuts
  reach. The line right after the cut has to pay off the hook.
- **Position bias.** In a decoder-only model, the opening and closing carry more weight in indexing.

**What to do:**
1. Two to three lines per paragraph, blank line between blocks, directional markers (numbers,
   arrows) where they earn their place.
2. Write mobile-first. A sentence that fits one desktop line becomes a wall on a phone.
3. Kill the boredom valley in the middle with a mini-hook. Close with a power ending that makes the
   post worth saving, because Save is the strongest quality signal available.
4. Aim for readability, not simplicity. The frame Jasmin Alić uses is worth stealing: write for an
   8th grader with the intelligence of a CEO.

**Rules:** any paragraph over four lines gets split. If the material is too dense for text, it wants
to be a document (carousel) instead.

---

## 3. Hooks and re-hooks

**Goal:** win the first three lines. They decide whether the post is expanded, and which interest
graph it gets filed under.

**Mechanism:**
- **Lost in distance.** A decoder-only model weights the opening sentences disproportionately.
- The "see more" click is the first quality signal inside the first 60 minutes.
- If the expansion does not continue the promise, click bounce cancels the gain.

**What to do:**
1. Line 1, generate three options: **specificity** (a number or concrete result), **contrarian**
   (challenges an industry belief), **anti-niche** (a universal human problem that funnels into your
   niche).
2. Lines 2-3 are the re-hook. Bridge the promise, do not restate it. Blank line between line 1 and
   line 2 to create visual intrigue on mobile.
3. Put the primary keyword in the first ten words.

**Rules:** never open with a greeting or "In today's world". Start in media res. The punchline has to
land before the mobile cut, roughly 140-200 characters.

---

## 4. Conversation design

**Goal:** turn a broadcast into a forum. Depth of dialogue is what expands reach into second and
third-degree networks.

**Mechanism:**
- Likes and reactions carry the least weight now, because they cost nothing.
- Comments over roughly 15 words are reported to be worth substantially more than short ones.
- Replying to a large share of comments in the first couple of hours lifts visibility.
- When someone outside your network comments substantively, the model can expand distribution into
  *their* cluster.

**What to do:**
1. Replace "What do you think?" with a question only an experienced reader can answer: "What is the
   most expensive mistake you made applying this?" or "If you added a step 8, what would it be?"
2. Answer with fact plus a new question, so the thread stays alive past 72 hours.
3. Pin a comment for any extra resource or link, rather than putting a link in the body.

**Rules:** no mechanical "comment below". Sell the value of the conversation. Avoid engagement pods,
which the system detects and penalizes.

---

## 5. Format selection

**Goal:** pick the container that maximizes reach and Save.

**Mechanism:**
- Formats requiring physical interaction (swiping a slide, voting, watching) are rewarded.
- Document and carousel posts show substantially higher engagement and the highest Save rate.
- A single static image with short text underperforms well-structured plain text.
- Completion rate matters. If most readers stop on slide 3 of 10, the post is marked low relevance.

**What to do:**

| Material | Format |
|---|---|
| Education, list, step-by-step | Document / carousel, 5-10 slides |
| Opinion, storytelling | Plain text |
| Research, top of funnel | Poll, 1-2 weeks |
| Demo, tutorial | Native video with captions (captions get indexed) |

**Rules:** no generic stock imagery. Over 10 slides and retention falls off. Always offer a fallback
format if the ideal one is out of reach.

---

## 6. Anti-slop

**Goal:** strip synthetic language so the post passes as written by a person with a point of view.

**Mechanism:**
- Predictability is penalized. The intro-points-conclusion shape is the most predictable shape there
  is.
- Recognized clichés ("It's not about X, it's about Y") are marked as low originality.
- What gets rewarded is a subject-matter perspective, meaning an opinion a model would not produce
  without having lived something.

**Two modes:**
- **Edit** (default) — rewrite the draft applying the dictionary and patterns below. This is the gate
  before publishing. Equivalent to `tools/sanitize.py`.
- **Detect** — audit only. Name each pattern, quote the line, suggest a short fix. Do not rewrite, do
  not score the draft, and do not try to guess whether an AI wrote it. AI detectors guess. A named
  pattern is evidence the author can check. Equivalent to `tools/sanitize.py --check`.

**Banned vocabulary:**

| Category | Avoid | Use instead |
|---|---|---|
| AI verbs | delve, unlock, leverage, empower, foster, orchestrate, navigate | a plain verb: did, saw, changed, shipped |
| Slop adjectives | revolutionary, comprehensive, robust, transformative, game-changing | a fact: "cut 20%", "board approved it" |
| AI stock phrases | in today's landscape, the future of, tapestry, journey, at the end of the day | "In 2026...", "Last week...", "In practice:" |
| Crutch adverbs | really, just, literally, genuinely, honestly, simply, actually, truly, fundamentally, crucially | cut it. If the adverb carries the weight, the verb is weak |

**Structural patterns to rewrite:**

- **False dichotomy** — "It's not about X, it's about Y". Replace with an engineering claim: "The
  market optimizes X, but the revenue bottleneck is Y."
- **Adjective cocktail hook** — "A [adj1], [adj2] and [adj3] strategy". Lead with the outcome.
- **Theatrical conclusion** — "Let's build a better future together". Use a technical CTA instead.
- **Throat-clearing opener** — "Here's the thing", "Let me be clear", "I'll be honest", "The
  uncomfortable truth is". Cut and start at the point.
- **Faux-insight setup** — "Here's what nobody tells you", "What most people get wrong". It flatters
  the author as a lone expert. Let the claim stand alone: "The part everyone misses: distribution is
  the moat" becomes "Distribution is the moat."
- **Colon reveal** — a short nominal phrase, a colon, then a dramatic lowercase reveal. "The best
  part: it learns on its own." Rewrite flat. Colons are for lists, labels and quotes.
- **Superficial -ing clause** — "..., highlighting the team's commitment to better workflows". It
  fakes explanation. Say the mechanism: "..., so users find old drafts without leaving the editor."
- **Weasel attribution** — "experts agree", "studies show", "industry reports suggest". Name the
  source or drop the claim. Never invent one; ask the author.
- **Fake-strong verb** — "serves as a centralized hub for". Prefer is, has, does: "tracks sponsors,
  drafts, due dates and approvals in one place."
- **Synonym cycling** — rotating terms for style instead of repeating the right one. "The agent
  reviews the draft. The assistant scores the piece. The tool suggests edits." If the right word is
  the same word, repeat it.
- **Negative listing** — "Not X. Not Y. It's Z." Say Z.
- **Dramatic fragmentation** — "That's it. That's the whole thing." Choppy rhythm is a tell.
- **Audience flattery** — "Whether you're a solo founder or a Fortune 500 exec". Name the real reader
  once, or cut it. The text already shows who it is for.
- **Both-sides hedging** — "While X offers benefits, challenges remain." Take a side or name the
  concrete tradeoff: "It writes the first 80% fast. The last 20% still needs you to review every line."
- **Rhetorical setup** — "What if I told you...", "Think about it:", self-answered question pairs.
  Drop it and make the claim.

**Self-eval loop.** After rewriting, run this. Every item is yes/no. Any "yes" sends you back. Loop
until all are "no". It is an actionable list, not a score.

*Meaning preserved*
1. Did I add a claim, example, statistic or opinion that was not in the draft?
2. Did I soften a nuance or a strong opinion that was worth keeping?

*Banned words*
3. Any AI verb, slop adjective or stock phrase left?
4. Any crutch adverb left?

*Structure*
5. False dichotomy? 6. Adjective cocktail? 7. Theatrical conclusion? 8. Throat-clearing?
9. Faux-insight? 10. Colon reveal? 11. Superficial -ing clause? 12. Weasel attribution?
13. Fake-strong verb? 14. Synonym cycling? 15. Negative listing? 16. Dramatic fragmentation?
17. Audience flattery? 18. Both-sides hedging? 19. Rhetorical setup? 20. Gratuitous triplet?

*Voice and rhythm*
21. Any passive verb that would accept a human subject?
22. Any sentence carrying more than one idea?
23. Does the rhythm repeat the same sentence shape several times running?

*Ending*
24. Is the last paragraph a recap ("In summary", "Overall")?
25. Is there a profound kicker, an aphorism or a mic-drop metaphor at the end?

If an item is genuinely ambiguous, flag it for the author instead of forcing a change.

---

## 7. Semantic SEO

**Goal:** get indexed, inside LinkedIn search and on Google, so a post keeps pulling discovery
traffic after the feed moves on.

**Mechanism:**
- The model serves posts to people who have shown interest in the topic, whether or not they follow
  you.
- Hashtag stuffing is dead. Hashtags are light labels and the body text is read in full. Past ~5,
  hashtags dilute the semantic signal.
- Post keywords get cross-referenced against your headline and top skills.
- A post with strong semantic authority can be indexed by Google quickly.

**What to do:**
1. Swap generic phrasing for the market's own term ("selling to companies" → "enterprise GTM").
2. 3 to 5 hashtags: one broad niche, two specific, one owned or brand.
3. Primary keyword in the first sentence and again in the close (position bias).
4. Strip unnecessary time markers ("this morning") so the post stays evergreen.

**Rules:** the primary keyword appears at least three times, organically. Text around any external
link should describe the destination.

---

## Suggested order

Alignment (1) → format (5) → hook (3) → layout (2) → anti-slop (6) → SEO (7) → then your own taste
in `linkedin-voice/style.md`, which overrides any of the above when they conflict.

**Personal taste wins every technical rule.** That is deliberate. Best practice that fights the
author's signature produces posts nobody believes.

---

## Sources

Compiled from ~70 public sources: LinkedIn's own engineering publications, independent algorithm
research, and public talks and writing by practitioners who study the platform full time. Nothing
here came from paid or leaked material.

**LinkedIn engineering, primary**

- *360Brew: A Decoder-only Foundation Model for Personalized Ranking and Recommendation* — arXiv
  [2501.16450](https://arxiv.org/abs/2501.16450)
- *LiRank: Industrial Large Scale Ranking Models at LinkedIn* — arXiv
  [2402.06859](https://arxiv.org/abs/2402.06859)
- *An Industrial-Scale Sequential Recommender for LinkedIn Feed Ranking*
- *Personalized Job Recommendation System at LinkedIn* (RecSys)
- *The Evolution of LinkedIn's Generative AI Tech Stack*; LinkedIn on scaling LLM semantic search and
  vLLM serving; the Feathr feature store

**Independent research** (freely published editions only)

- **Richard van der Blom** / Just Connecting — LinkedIn algorithm research, October 2020 edition, as
  hosted publicly by the Stony Brook SBDC. His current editions are a paid product and were not used.
- Trust Insights — *The Unofficial LinkedIn Algorithm Guide for Marketers*, mid-2025 edition
- *Mastering the LinkedIn Algorithm in 2025/26* (The Lone Recruiter)

**Practitioners whose public work shaped the writing specs**

- **Jasmin Alić** — writing and commenting playbooks. Spec 2's readability frame is his.
- **Michelle J Raymond** — B2B social strategy
- **Richard van der Blom** — 360Brew analysis and credibility scoring

**Anti-slop pattern set**

- [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) (MIT). Spec 6's pattern names and
  several examples are adapted from it.

Where a number appears above without a citation, it comes from one of the third-party studies listed
here rather than from LinkedIn. Any of it can go stale. If you can measure your own account, trust
that over this document.
