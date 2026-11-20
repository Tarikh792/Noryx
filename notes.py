
import json
from pathlib import Path

# Local storage file
NOTES_FILE = Path(__file__).parent / "notes.json"


def load_notes() -> dict:
    """Load saved notes from JSON storage."""
    if not NOTES_FILE.exists():
        return {}

    try:
        with NOTES_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            return {}

        return data

    except (json.JSONDecodeError, OSError):
        return {}


def save_note(title: str, content: str) -> str:
    """Create or update a note."""

    title = title.strip()
    content = content.strip()

    if not title or not content:
        return "Error: Title and content cannot be empty."

    notes = load_notes()
    notes[title] = content

    NOTES_FILE.write_text(
        json.dumps(
            notes,
            indent=2,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )

    return f"Note '{title}' saved successfully."


def read_note(title: str) -> str:
    """Read a note by title."""

    notes = load_notes()

    return notes.get(
        title,
        f"Note '{title}' not found."
    )


def list_notes() -> list[str]:
    """Return all saved note titles."""

    notes = load_notes()

    return sorted(notes.keys())


def search_notes(query: str) -> dict[str, str]:
    """Search saved notes by keyword."""

    query = query.strip().lower()

    if not query:
        return {}

    notes = load_notes()

    return {
        title: content
        for title, content in notes.items()
        if query in title.lower()
        or query in content.lower()
    }


# Run directly to test local storage
if __name__ == "__main__":
    print(save_note(
        "AI Engineering",
        "Noryx is a Python MCP server."
    ))

    print("All notes:", list_notes())

    print("Read note:", read_note("AI Engineering"))

    print("Search results:", search_notes("MCP"))
