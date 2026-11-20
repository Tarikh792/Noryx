
from mcp.server.fastmcp import FastMCP

from notes import (
    save_note,
    read_note,
    list_notes,
    search_notes
)


# Initialize MCP server
mcp = FastMCP("Noryx")


@mcp.tool()
def server_status() -> str:
    """Check whether the Noryx MCP server is running."""
    return "Noryx MCP Server is running successfully!"


@mcp.tool()
def create_note(title: str, content: str) -> str:
    """Create or update a note in local storage."""
    return save_note(title, content)


@mcp.tool()
def get_note(title: str) -> str:
    """Read a saved note by its title."""
    return read_note(title)


@mcp.tool()
def get_all_notes() -> list[str]:
    """List the titles of all saved notes."""
    return list_notes()


@mcp.tool()
def find_notes(query: str) -> dict[str, str]:
    """Search saved notes by title or content."""
    return search_notes(query)


if __name__ == "__main__":
    # Start server using standard MCP stdio transport
    mcp.run()
