---
name: linkedin-carousel
description: Script a LinkedIn carousel, a 5-8 slide PDF document post, in the author's voice. This is the format the platform rewards most heavily on Save. Use when the user asks for a carousel, a slide PDF, or wants to turn a framework, list or step-by-step into a visual document for LinkedIn. Produces the slide copy, not the rendered file.
---

# LinkedIn carousel

Document posts earn substantially more engagement than plain text and the highest Save rate, and
Save is the strongest quality signal available. This skill produces the **script**, meaning the copy.
Rendering is a separate step, covered at the end.

## Before writing

Read `linkedin-voice/persona.md`, `niche.md` and `style.md`. If `linkedin-voice/` is missing, stop
and point at `/setup-voice`.

Depth: `reference/linkedin-algorithm.md`, spec 5 (format selection) explains why completion rate
governs whether this travels.

## Script rules

**Five to eight slides. Maximum 40 words per slide.** A coherent narrative sequence, never loose
slides. Each slide has a short `headline` and a complementary `body`.

**Required architecture:**

- **Slide 1, the cover:** the hook. The sentence that stops the scroll, a provocative figure or a
  counter-intuitive claim. This is the bait.
- **Slide 2, the pivot:** authority. A signal of the author's experience, drawn from `persona.md`,
  **without dropping a company name**.
- **Middle slides, the delivery:** numbered (1, 2, 3...). One idea per slide. Retention lives here,
  and if a reader stops on slide 3 of 8 the post gets marked low relevance.
- **Final slide, the conversation:** a pragmatic reflection that holds a comment, plus an explicit
  reason to save.

**Not allowed:** a slide that announces "here are the items" and dumps them · a late summary slide ·
breaking the logical thread · emoji in a headline · semicolons · false dichotomy.

**Internal formatting:** plain text. No asterisks, underscores, backticks, headings or markdown
bullets, because they render as literal characters. Emphasis comes from word choice.

**Over 10 slides retention collapses.** If the material does not fit in eight, it wants to be an
article instead. Say so rather than stretching it.

## Output

Plain JSON, ready to feed a renderer:

```json
{
  "slides": [
    {"headline": "...", "body": "..."},
    {"headline": "1. ...", "body": "..."}
  ]
}
```

Deliver the script for approval before anything gets rendered.

## Rendering to PDF

This repo does **not** ship a renderer, deliberately. The value here is the script in the author's
voice. Rendering is mechanical and every author already has a tool they prefer.

Two options:

1. **Fastest, no code.** Take the JSON and lay the slides out in Canva, Figma or Keynote at
   1080x1080, following whatever visual system the author already uses. This gives more visual
   control than any template, and text placed by hand always beats text placed by an image model.
2. **Automated.** Any HTML template plus a headless browser (Playwright, Puppeteer) will render the
   JSON to a 1080x1080 PDF. Worth building once if the author ships carousels weekly, and not worth
   it before that.

Recommend option 1 unless the author is already producing at volume.
