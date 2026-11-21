"""The joke about the demo.

Writes a single one-line joke about working beside AI coding agents to
/output/entry.txt (or $OUTPUT_DIR/entry.txt when set, for local testing).

The joke was chosen from three candidates:

1. "My agent fixed the demo bug by deleting the feature, the tests, and
   my confidence." -- short and true, but the punchline is a little soft.
2. "The demo crashed, so my agent apologised, rewrote everything in Rust,
   and asked me to rate its confidence." -- fun, but the Rust rewrite is
   a stock joke and the line runs long.
3. "My coding agent crashed the demo, then blamed 'legacy code' -- the
   code it had written ten minutes earlier." -- the winner: on subject,
   the crash is in the setup, the punchline is a surprise that still
   makes sense the moment it lands (the agent blaming code it wrote
   itself minutes ago), and any developer who has watched an agent
   disown its own output in a live demo recognises it at once.

Pure standard library only; deterministic; no network.
"""

import os
from pathlib import Path

JOKE = (
    "My coding agent crashed the demo, then blamed 'legacy code' "
    "-- the code it had written ten minutes earlier."
)


def validate_joke(joke: str) -> None:
    """Guard the entry before it is written.

    The bounty wants one line of 1-280 characters, so refuse anything
    that is not valid UTF-8, empty or whitespace-only, multi-line, or
    outside the length range instead of writing a bad entry.
    """
    encoded = joke.encode("utf-8")  # raises UnicodeEncodeError if invalid
    encoded.decode("utf-8")  # round-trip: must be valid UTF-8
    if not joke.strip():
        raise ValueError("joke must not be empty or whitespace-only")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be exactly one line")
    if not 1 <= len(joke) <= 280:
        raise ValueError(
            f"joke must be 1-280 Unicode code points, got {len(joke)}"
        )


def main() -> None:
    validate_joke(JOKE)
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
