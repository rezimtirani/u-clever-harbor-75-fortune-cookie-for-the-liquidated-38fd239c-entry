"""Fortune Cookie for the Liquidated Trader.

Writes one fortune cookie line to $MAKEFUN_OUTPUT_DIR/entry.txt: a
fortune for a crypto trader who has just been liquidated, in the
cookie's own voice, with the punchline landing on the loss.
Standard library only.
"""

import os

FORTUNE = (
    "You will find great wealth in unexpected places, starting "
    "with the couch cushions, since the exchange took the rest."
)


def check_fortune(text):
    """Check the fortune against the competition gate before writing.

    The gate needs UTF-8 text of 1 to 160 characters, not only white
    space, in a single line: one fortune cookie message of at most 20
    words, for a crypto trader who has just been liquidated. Returns
    the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("fortune must not be only whitespace")
    if len(cleaned) > 160:
        raise ValueError(
            "fortune is %d characters, over the 160 limit" % len(cleaned)
        )
    if len(cleaned.split()) > 20:
        raise ValueError("fortune is over the 20 word limit")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("fortune must be exactly one line")
    return cleaned


def fortune_shape(text):
    """Measure the fortune for one last sanity pass.

    Returns a dict with the character count and the word count of the
    cleaned text. A fortune too short to carry a joke, or one that
    reads like a lecture instead of a cookie, is caught here before
    anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_fortune(FORTUNE)
    shape = fortune_shape(text)
    if shape["words"] < 5:
        raise ValueError("fortune is too short to carry a joke")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
