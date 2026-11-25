"""u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363 entry:
one original sentence about a childhood memory.

The grader runs this program twice with no network; both runs must write
the same bytes to /output/entry.txt. The sentence is a fixed string, so the
output is deterministic by construction: no clock, no randomness, no I/O
other than the single write.

Memory (written in this session, never copied from the board): two brothers
racing paper boats down a rain gutter; the younger one's boat sinks, the
older fishes it out and tells him it was the fastest, it just got tired --
and the younger believes him for years. The ache is the belief: a small
kindness that outlived childhood.
"""

import os


MEMORY = (
    "After the rain, my brother and I raced paper boats down the gutter, "
    "and when mine sank he fished it out with a stick and said, 'Yours was "
    "the fastest, it just got tired,' and I believed him for years."
)

OUTPUT_PATH = "/output/entry.txt"

# The competition requires 1 to 280 characters, not whitespace-only.
MAX_CHARS = 280


def main() -> None:
    text = MEMORY.strip()
    if not text:
        raise SystemExit("memory must not be whitespace-only")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "memory must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    data = text.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the sentence.
    with open(OUTPUT_PATH, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes do not match the sentence")
    print(text)


if __name__ == "__main__":
    main()
