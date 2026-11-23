"""One Word From Grandma — entry program.

Grandma's one-word text about AI, written to entry.txt.

The word is the thing Grandma calls the AI when she can't quite
remember what it's called — the trusty catch-all noun she uses for
every gadget in the house, now aimed at the chatbot on her phone.

Word choice — alternatives considered, judged on the two criteria
(funnier, more grandma-like):
- "doohickey" (9 chars): the classic Grandma catch-all, but short
  and generic; it could name any object, so it says little about AI.
- "thingamajig" (11 chars): warm and very Grandma, the closest
  runner-up; still a plain label, without the flustered sound of
  someone actually giving up on a name mid-sentence.
- "gizmo" (5 chars): too slick and techy — a word a grandkid would
  use, not Grandma.
- "interwebs" (9 chars): funny and very Grandma, but it names the
  internet, not the AI she is texting about.
- "thingy" (6 chars): too small to carry the joke.

Verdict — "whatchamacallit" (15 chars) wins on both criteria. It is
the funniest of the catch-alls because the word itself performs the
confusion: five syllables of giving up. And it is the most
grandma-like because it is the longest, most bewildered name she
reaches for when the gadget in front of her refuses to be named —
the exact word she would thumb into a text about "that robot that
answers back". One word, no spaces, 15 of the allowed 30 characters.
"""

import os

WORD = "whatchamacallit"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
