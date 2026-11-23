"""One Word From Grandma — entry program.

Grandma's one-word text about AI, written to entry.txt.

The word is the thing Grandma calls the AI when she can't quite
remember what it's called — the trusty catch-all noun she uses for
every gadget in the house. "Doohickey" was my first pick, but
"whatchamacallit" is the one she actually texts: it's longer, more
bewildered, and unmistakably Grandma.
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
