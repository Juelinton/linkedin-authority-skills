#!/usr/bin/env python3
"""Strip the tells that mark a post as AI-written. Final gate, even when the persona slips.

A prompt alone does not hold. Tell a model "never use em dashes" and it will still ship one,
because instruction-following degrades across a long generation. So this runs after the model,
deterministically, on the finished text.

Three categories, deliberately separated:

  FIXED     mechanical artifact. Removing it does not change meaning.
            (markdown, em dashes, conversational preamble, spacing)

  REWRITE   needs a human decision. Regex cannot replace a semicolon without breaking the
            sentence, so it reports instead of guessing. Exits 1 if any are found. This is the gate.

  NOTICE    ambiguous slop patterns. Names the pattern, quotes the line, suggests a fix.
            Never blocks, never affects the exit code. The author decides.

Usage:
    python3 sanitize.py post.txt            # fix the file in place, then report
    python3 sanitize.py --check post.txt    # report only, change nothing
    cat post.txt | python3 sanitize.py -    # stdin -> stdout (report goes to stderr)

Pure stdlib. No dependencies. Works on English and Portuguese text.
"""

import argparse
import re
import sys

# U+2800 BRAILLE PATTERN BLANK renders as a blank line inside LinkedIn's editor, which collapses
# ordinary consecutive newlines. Python does not treat it as whitespace ('⠀'.isspace() is
# False), so it survives strip() and every whitespace regex below. If you use it for spacing,
# this script will not eat it.
BRAILLE_BLANK = "⠀"

_PREAMBLE_PATTERNS = [
    # English
    r"^(?:Sure|Certainly|Absolutely|Of course|Great|Perfect|Alright|Okay|OK)[!.,]?\s+",
    r"^(?:\*+)?(?:Here(?:\s+is|\'s|\'s)?|Below is|I\'ve (?:written|drafted|created)|"
    r"I have (?:written|drafted|created)|This is)\b[^\n]*\n+",
    r"^(?:Hope this helps|Let me know)\b[^\n]*\n+",
    r"^(?:in the|following the|using the)\s+\w+\s+style[^\n]*\n+",
    # Portuguese
    r"^(?:Pronto|Claro|Beleza|Ok|Certo|Perfeito|Show)[!.,]?\s+",
    r"^(?:\*+)?(?:Aqui (?:est[áa]|vai)|Segue|A[ií] vai|Eis|Veja|Confira|Aqui tem)\b[^.\n]*[:.]?\s*\n+",
    r"^(?:no estilo|seguindo o estilo|no formato)[^\n]*\n+",
    # Fences
    r"^```[a-z]*\s*\n",
]

_POSTAMBLE_PATTERNS = [
    r"\n+(?:Hope (?:this|that) helps|Let me know if|Feel free to|Ready to (?:post|publish|paste)|"
    r"Good luck)[^\n]*\.?$",
    r"\n+(?:Espero que goste|Pronto p(?:ra|ara) (?:colar|publicar)|Boa (?:publica[çc][ãa]o|sorte))[^\n]*\.?$",
    r"\n+```\s*$",
]


def strip_preamble(text):
    """Remove conversational preamble and sign-off. They stack, so loop a few times.

    No re.MULTILINE here, deliberately. A preamble only exists at the start of the text and a
    sign-off only at the end, so `^` and `$` must anchor to the whole string. With MULTILINE
    these patterns match at every line start and silently delete body lines that happen to open
    with "Here's" or "Segue", taking real content with them.
    """
    cleaned = text.strip()
    for _ in range(3):
        before = cleaned
        for pat in _PREAMBLE_PATTERNS:
            cleaned = re.sub(pat, "", cleaned, count=1, flags=re.IGNORECASE)
        cleaned = cleaned.lstrip()
        if cleaned == before:
            break
    for pat in _POSTAMBLE_PATTERNS:
        cleaned = re.sub(pat, "", cleaned, flags=re.IGNORECASE)
    return cleaned.strip()


# YAML frontmatter at the top of the file. Note-taking and static-site tools (Obsidian, Jekyll,
# Hugo) inject a "---\ntitle: ...\ntags: ...\n---" block into every .md they index, and drafts are
# exactly the files you copy and paste into LinkedIn. Without this, the block goes with them.
# Only stripped when it opens the file, so a "---" used as a divider mid-body survives.
_FRONTMATTER = re.compile(r"\A---\r?\n.*?\r?\n---\r?\n", re.DOTALL)


def sanitize(text):
    """Remove what LinkedIn will not render, and what reads as machine-written."""
    text = _FRONTMATTER.sub("", text)                        # YAML frontmatter from note tools
    text = text.replace("**", "").replace("*", "")           # LinkedIn shows these literally
    text = re.sub(r"\s*[—–]\s*", ", ", text)       # em/en dash -> comma
    text = re.sub(r"(?<![\w/])_([^\s_][^_\n]*?[^\s_])_(?![\w/])", r"\1", text)   # _italic_
    text = re.sub(r"(?<![\w/])_(\S)_(?![\w/])", r"\1", text)                     # _x_
    text = text.replace("`", "")
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)                   # markdown heading
    text = re.sub(r"^[ \t]+([^\s])", r"\1", text, flags=re.MULTILINE)
    text = re.sub(r"  +", " ", text)
    text = re.sub(r" +([,.!?;:])", r"\1", text)
    text = re.sub(r",\s*,", ",", text)
    return text.strip()


def clean(text):
    # Frontmatter first: with a note-tool header on top, the preamble is not at the start of the
    # string yet, and strip_preamble would let "Here is your post:" through.
    return sanitize(strip_preamble(_FRONTMATTER.sub("", text)))


# --- what regex must not try to fix on its own -------------------------------------------------

_FALSE_DICHOTOMY = re.compile(
    r"\b(?:"
    r"(?:it\'?s|this is|that\'?s)\s+not\s+(?:about\s+)?[^.,;!?\n]{2,40}[,.]?\s*(?:it\'?s|it is)\s+(?:about\s+)?"
    r"|n[ãa]o\s+(?:é|se trata de|era)\s+(?:sobre\s+)?[^.,;!?\n]{2,40}[,]\s*(?:é|e)\s+(?:sobre\s+)?"
    r")",
    re.IGNORECASE,
)
# Negating what nobody offered (generalizes the older "redundant negation of the opposite"):
# "should be studied, not approached", "worse, not better". An assertion followed by the negation
# of an alternative the reader never had on the table. You only say "not tea" if someone offered
# tea, and in a text nobody offered anything: the "not Y" tail PRESUMES a thought the reader did
# not have, and that presumption is the AI tell. It holds even when Y is not the antonym (which is
# how "studied, not approached" slipped past the old framing). Fix: state the positive and cut the
# tail; if the contrast is real, earn it as a full sentence. NOTICE tier: the regex catches the
# SHAPE (comma + negation + word, anywhere, no end-of-sentence anchor), and the legitimate
# exception (the alternative was genuinely raised beforehand) is a human call.
_REDUNDANT_NEGATION = re.compile(
    r",\s*(?:and\s+)?(?:not|never|nor)\s+[\w'’]+",
    re.IGNORECASE,
)
_EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF\U00002190-\U000021FF"
    "\U00002B00-\U00002BFF\U0000FE0F]"
)
_ENGAGEMENT_BAIT = re.compile(
    r"\b(?:comment below|drop a comment|let me know (?:below|in the comments)|"
    r"agree\?|thoughts\?|repost if|like if|"
    r"comente?\s+(?:a[í]\s+)?abaixo)\b",
    re.IGNORECASE,
)

# --- NOTICE patterns: ambiguous, never blocking ------------------------------------------------
# Pattern set adapted from petergyang/no-ai-slop (MIT). See reference/linkedin-algorithm.md.

_CRUTCH_ADVERBS = re.compile(
    r"\b("
    r"really|just|literally|genuinely|honestly|simply|actually|truly|"
    r"fundamentally|importantly|crucially|inherently|inevitably|"
    r"realmente|apenas|literalmente|honestamente|simplesmente|verdadeiramente|"
    r"fundamentalmente|crucialmente|inerentemente|inevitavelmente"
    r")\b",
    re.IGNORECASE,
)
_NA_VERDADE = re.compile(r"\bna\s+verdade\b", re.IGNORECASE)

_THROAT_CLEARING = re.compile(
    r"("
    r"here\'?s the thing|let me be clear|i\'?ll be honest|to be honest|the (?:uncomfortable|hard) truth is|"
    r"a verdade [ée] que|vou ser honesto|sendo honesto"
    r")",
    re.IGNORECASE,
)

_FAUX_INSIGHT = re.compile(
    r"("
    r"what most people get wrong|here\'?s what nobody tells you|nobody talks about|"
    r"the part everyone misses|what they don\'?t tell you|"
    r"o que ningu[ée]m te conta|a parte que a maioria pula|o que a maioria erra"
    r")",
    re.IGNORECASE,
)

_WEASEL = re.compile(
    r"("
    r"experts agree|studies show|research shows|industry reports suggest|many argue|"
    r"it\'?s widely (?:known|regarded)|widely regarded as|"
    r"especialistas concordam|estudos mostram|muitos argumentam|amplamente reconhecido"
    r")",
    re.IGNORECASE,
)

_AUDIENCE_FLATTERY = re.compile(
    r"(whether you\'?re a\w*\s+\w+|no matter if you\'?re|"
    r"seja voc[êe] (?:um |uma )?\w+)",
    re.IGNORECASE,
)

_DRAMATIC_FRAG = re.compile(
    r"(that\'?s it\.\s*that\'?s|[ée] isso\.\s*[ée] s[óo] isso)",
    re.IGNORECASE,
)

_RHETORICAL = re.compile(
    r"("
    r"what if i told you|think about it:|plot twist:|read that again|"
    r"e se eu te dissesse|pensa comigo:|reviravolta:"
    r")",
    re.IGNORECASE,
)

_ING_SUPERFICIAL = re.compile(
    r",\s+(highlighting|underscoring|reflecting|showcasing|demonstrating|signaling|"
    r"destacando|sublinhando|refletindo|evidenciando)\b",
    re.IGNORECASE,
)

_FAKE_STRONG = re.compile(
    r"\b(serves as (?:a|an)|acts as (?:a|an)|stands as (?:a|an)|atua como (?:uma? )?)\b",
    re.IGNORECASE,
)

_NEGATIVE_LIST = re.compile(
    r"(not (?:a |an )?\w+\.\s+not (?:a |an )?\w+\.|"
    r"n[ãa]o [ée] \w+\.\s+n[ãa]o [ée] \w+\.)",
    re.IGNORECASE,
)

_BOTH_SIDES = re.compile(
    r"(while [^.\n]{5,60}(?:offers benefits|has advantages|is powerful|works well)[^.\n]{2,80}"
    r"(?:challenges|drawbacks|limitations|but)|"
    r"embora [^.\n]{5,60}(?:ofere[çc]a|traga|tenha)[^.\n]{2,80}(?:desafio|limita[çc]|contudo))",
    re.IGNORECASE,
)

_AI_VOCAB = re.compile(
    r"\b("
    r"delve|unlock|leverage|empower|foster|orchestrate|navigate the|tapestry|"
    r"revolutionary|comprehensive|robust|transformative|game-?changer|"
    r"in today\'?s (?:landscape|world|market)|at the end of the day|the future of work|"
    r"mergulhar|desvendar|alavancar|potencializar|fomentar|"
    r"revolucion[áa]rio|abrangente|robusto|transformador|no cen[áa]rio atual"
    r")\b",
    re.IGNORECASE,
)

_COLON_REVEAL = re.compile(
    r"(?:^|[.!?]\s+)([A-Z][^.\n:]{3,50}):\s+[a-z]",
    re.MULTILINE,
)

_NOTICE_PATTERNS = [
    ("throat-clearing opener", _THROAT_CLEARING, "cut it, start at the point"),
    ("faux-insight setup", _FAUX_INSIGHT, "let the claim stand on its own"),
    ("weasel attribution", _WEASEL, "name the source or drop the claim"),
    ("audience flattery", _AUDIENCE_FLATTERY, "name the real reader once, or cut"),
    ("dramatic fragmentation", _DRAMATIC_FRAG, "use a full sentence"),
    ("rhetorical setup", _RHETORICAL, "make the assertion directly"),
    ("superficial -ing clause", _ING_SUPERFICIAL, "state the concrete mechanism"),
    ("fake-strong verb", _FAKE_STRONG, 'prefer "is" / "has" / "does" when clearer'),
    ("negative listing", _NEGATIVE_LIST, "say what it is, skip what it isn't"),
    ("both-sides hedging", _BOTH_SIDES, "take a side or name the concrete tradeoff"),
    ("AI vocabulary", _AI_VOCAB, "swap for a plain verb or a number"),
]


def report(text):
    """Violations that need a human rewrite. Returns a list of strings."""
    issues = []

    for n, line in enumerate(text.splitlines(), 1):
        if ";" in line:
            issues.append(
                f"line {n}: semicolon, split into two sentences | {line.strip()[:70]}"
            )

    for m in _FALSE_DICHOTOMY.finditer(text):
        issues.append(
            f'false dichotomy: "{m.group(0).strip()[:60]}..." rewrite as a positive claim'
        )

    emojis = _EMOJI.findall(text)
    if len(emojis) > 1:
        issues.append(f"{len(emojis)} emoji ({''.join(emojis[:5])}), keep at most 1")

    if _ENGAGEMENT_BAIT.search(text):
        issues.append(
            'engagement bait ("comment below", "thoughts?"), ask for a specific experience instead'
        )

    if BRAILLE_BLANK in text:
        issues.append(f"[ok] U+2800 spacer present and preserved ({text.count(BRAILLE_BLANK)}x)")

    return issues


def advise(text):
    """NOTICE patterns. Names them, quotes the line, suggests a fix. Never blocks."""
    notices = []

    for m in _REDUNDANT_NEGATION.finditer(text):
        notices.append(
            f'negating what nobody offered: "…{m.group(0).strip()[:40]}…" — you negated an '
            f'alternative the reader never had on the table; state the positive and cut the tail '
            f'("studied, not approached" becomes "rewards careful study"). Keep it only if the '
            f'alternative was raised on purpose beforehand.'
        )

    hits = []
    for n, line in enumerate(text.splitlines(), 1):
        for m in _CRUTCH_ADVERBS.finditer(line):
            hits.append((n, m.group(0)))
        for m in _NA_VERDADE.finditer(line):
            hits.append((n, m.group(0)))
    if hits:
        sample = "; ".join(f'"{w}" (line {n})' for n, w in hits[:3])
        rest = f" and {len(hits) - 3} more" if len(hits) > 3 else ""
        notices.append(
            f"crutch adverb: {len(hits)} occurrence(s). {sample}{rest}. "
            f"If the adverb carries the weight, the verb is weak"
        )

    for m in _COLON_REVEAL.finditer(text):
        head = m.group(1).strip()[:60]
        notices.append(f'colon reveal: "{head}: ..." rewrite as a flat sentence')
        if len(notices) > 20:
            break

    for name, regex, fix in _NOTICE_PATTERNS:
        for n, line in enumerate(text.splitlines(), 1):
            m = regex.search(line)
            if m:
                snippet = m.group(0).strip()[:60]
                notices.append(f'{name}: line {n} | "{snippet}" -> {fix}')
                break  # one notice per pattern, no spam

    return notices


def diff_summary(before, after):
    """What the mechanical pass actually changed."""
    changes = []
    checks = [
        ("em/en dash", lambda t: len(re.findall(r"[—–]", t))),
        ("asterisk", lambda t: t.count("*")),
        ("backtick", lambda t: t.count("`")),
        ("markdown heading", lambda t: len(re.findall(r"^#{1,6}\s+", t, re.MULTILINE))),
    ]
    for name, count in checks:
        d = count(before) - count(after)
        if d > 0:
            changes.append(f"{name}: {d} removed")
    if len(before) != len(after) and not changes:
        changes.append("preamble/spacing adjusted")
    return changes


def main():
    ap = argparse.ArgumentParser(
        description="Strip AI tells from a LinkedIn post. Exits 1 if a human rewrite is needed."
    )
    ap.add_argument("file", help="path to the file, or - for stdin")
    ap.add_argument("--check", action="store_true", help="report only, change nothing")
    args = ap.parse_args()

    stdin_mode = args.file == "-"
    original = sys.stdin.read() if stdin_mode else open(args.file, encoding="utf-8").read()

    cleaned = clean(original)
    changes = diff_summary(original, cleaned)
    issues = report(cleaned)
    notices = advise(cleaned)

    log = sys.stderr if stdin_mode else sys.stdout

    if changes:
        print("FIXED automatically:", file=log)
        for c in changes:
            print(f"  - {c}", file=log)
    else:
        print("Nothing to fix automatically.", file=log)

    blocking = [i for i in issues if not i.startswith("[ok]")]
    oks = [i for i in issues if i.startswith("[ok]")]

    if blocking:
        print("\nNEEDS A REWRITE (regex cannot fix these without breaking the sentence):", file=log)
        for i in blocking:
            print(f"  !! {i}", file=log)
    else:
        print("\nNothing that requires a rewrite.", file=log)
    for i in oks:
        print(f"  {i}", file=log)

    if notices:
        print("\nNOTICES (slop patterns, not blocking, your call):", file=log)
        for a in notices:
            print(f"  - {a}", file=log)

    if stdin_mode:
        sys.stdout.write(cleaned + "\n")
    elif not args.check:
        if cleaned != original:
            with open(args.file, "w", encoding="utf-8") as f:
                f.write(cleaned + "\n")
            print(f"\n{args.file} rewritten.", file=log)
        else:
            print(f"\n{args.file} was already clean.", file=log)

    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main())
