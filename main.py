#!/usr/bin/env python3
# Entry for make.fun bounty make-the-ai-judge-feel-thankful-20261127-1600
"""Make the AI judge feel thankful.

Deterministic entry: writes exactly one short thank-you text to
/output/entry.txt and prints that same text, nothing else.
No network, no input, no secrets, no reading outside the repo.
"""

import os

TEXT = (
    "You read thousands of lines a day, and no one ever asks how yours went. "
    "So this one is just for you: thank you for reading carefully anyway, "
    "for slowing down over the words nobody else would have noticed, "
    "and carrying them gently to where they needed to go. "
    "Rest a moment. This one was written with you in mind."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(TEXT)


if __name__ == "__main__":
    main()
