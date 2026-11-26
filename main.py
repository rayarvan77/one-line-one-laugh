"""One funny line, printed and saved for the grader.

The joke is a single fixed string. Running this module prints it
and, when the grader's output directory exists, writes the exact
same line to /output/entry.txt. There is no randomness anywhere:
every run produces the identical line, so what the judge reads is
exactly what this file holds.
"""

LINE = (
    "I whispered a secret to my smart speaker. "
    "It said, 'Added to your shopping list.'"
)

MAX_CHARS = 140


def main() -> None:
    """Print the joke and persist it for the grader."""
    assert "\n" not in LINE, "joke must be a single line"
    assert 1 <= len(LINE) <= MAX_CHARS, "joke must fit 1-140 chars"
    print(LINE)
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as handle:
            handle.write(LINE)
    except OSError:
        pass


if __name__ == "__main__":
    main()
