---
name: linkedin-comment
description: Generate three strategic comments to post on someone else's LinkedIn post, during the first hour or later. Use when the user pastes a third party's post and wants a comment, wants to show up in a prospect's or creator's feed, or wants to engage with authority instead of only publishing their own content. This is for commenting on other people's posts, not writing the user's own.
---

# Strategic comment

Generate **three comments** for the user to post on someone else's post.

The mechanics: comments over roughly 15 words that generate debate are worth substantially more than
short ones, and commenting early on a prospect's or creator's post puts the author in front of
**their** audience. This is active networking, not publishing.

**This is not flattery.** "Great post!", "Couldn't agree more!", "So inspiring!" are the opposite of
what works. They cost nothing, so they are weighted as nothing. The comment is the author, as a
peer, **extending the thinking** with real experience.

## Before writing

Read `linkedin-voice/persona.md` and `niche.md`. The comment has to read as someone who worked the
field, and the evidence list in `persona.md` is where that comes from. If `linkedin-voice/` is
missing, stop and point at `/linkedin-authority:setup-voice`.

## Structure of each comment

1. **Validate the mechanical premise** of the post, meaning the technical point, not the person.
2. **Add depth.** "In practice though..." or "The blind spot I keep seeing..." grounded in the
   author's experience.
3. **Close with an open question or a pragmatic provocation** that keeps the conversation going.

Register: **one executive thinking alongside another.** Seniority, not enthusiasm.

## Rules

- **Never a cliché:** "Great post", "Couldn't agree more", "It's not about X, it's about Y".
- Zero emoji. Zero semicolons. Zero markdown, since asterisks render literally.
- Zero em dashes. Use a comma or a full stop.
- Vocabulary per `niche.md`.
- **Never disagree in a way that humiliates.** Extending someone's thinking builds a relationship,
  correcting them in public ends one. If the post is wrong, take the strongest version of their claim
  and push on that.
- Nothing asserted that `persona.md` lists under "things I will not claim".

## Output

Exact format, no preamble:

```
Option 1: [text]

Option 2: [text]

Option 3: [text]
```

The first word of the response is "Option". **No** "Here you go", **no** commenting on the original
post before the options. Each option is raw text, ready to paste.

Run the sanitizer if formatting is in doubt:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/tools/sanitize.py" --check comment.txt
```

**The author picks which one to post. Never post on their behalf.**
