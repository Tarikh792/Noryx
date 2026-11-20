# 🟣 Noryx — MCP Knowledge Management Server

**A modular Model Context Protocol server for connecting AI applications to structured knowledge and productivity tools.**

Noryx is a Python-based MCP server that enables compatible AI clients to create, read, list, and search notes through a standardized tool interface.

Built with the official MCP Python SDK, Noryx demonstrates practical MCP server development, tool registration, local data persistence, and client-server communication.

The project includes a custom Python MCP client and has been tested using MCP Inspector.

## ✨ Features

- **MCP Tool Integration** — Exposes Python functions as discoverable MCP tools.
- **Notes Management** — Create, update, retrieve, and list notes.
- **Knowledge Search** — Find notes using keyword-based search across titles and content.
- **Local Persistence** — Store notes in JSON format.
- **Client-Server Communication** — Supports the MCP standard input/output (stdio) transport.
- **Tool Discovery** — Compatible MCP clients can discover available tools.
- **MCP Inspector Integration** — Graphically inspect and execute tools.
- **Custom MCP Client** — Includes a Python client for integration testing.
- **Input Validation** — Rejects empty note titles and content.

## 🛠️ Available MCP Tools

| Tool | Description |
|---|---|
| `server_status` | Check server status |
| `create_note` | Create or update a note |
| `get_note` | Retrieve a note by title |
| `get_all_notes` | List all saved note titles |
| `find_notes` | Search notes by keyword |

All five tools have been registered successfully. The note creation and search functions have also been tested through MCP client communication.

## 🧠 How Noryx Works

Noryx acts as an intermediary between compatible AI applications and a local knowledge store.

```text
         MCP-Compatible AI Client
                   |
                   |
            MCP Protocol
             (stdio)
                   |
                   v
        +----------------------+
        |     NORYX SERVER     |
        |      Python MCP      |
        +----------------------+
                   |
           MCP Tool Registry
                   |
      +------------+------------+
      |            |            |
      v            v            v
  Create Note   Read Note    Search Notes
      |            |            |
      +------------+------------+
                   |
                   v
              notes.py
                   |
                   v
              notes.json
          Local JSON Storage
```

The server uses the MCP Python SDK to expose Python functions as tools. Client requests are routed through the MCP protocol and handled by the corresponding notes-management functions.

## 💻 Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python 3.11 |
| Protocol | Model Context Protocol (MCP) |
| SDK | Official MCP Python SDK 1.x |
| Server Framework | FastMCP |
| Transport | stdio |
| Storage | JSON |
| Integration Testing | Python MCP Client |
| Graphical Testing | MCP Inspector |

## 📁 Project Structure

```text
Noryx/
├── server.py
├── notes.py
├── test_client.py
├── requirements.txt
├── README.md
├── .gitignore
└── notes.json          # Generated locally, not committed
```

### Core Components

**`server.py`**

Initializes the MCP server and registers all five tools.

**`notes.py`**

Implements note creation, retrieval, listing, searching, and local JSON persistence.

**`test_client.py`**

Connects to the server through stdio and tests tool discovery and execution.

**`requirements.txt`**

Defines the compatible MCP SDK dependency.

## 🚀 Getting Started

### Prerequisites

- Python 3.11
- pip
- Node.js and npm (optional, for MCP Inspector)

### 1. Clone the Repository

```bash
git clone https://github.com/Tarikh792/Noryx.git
cd Noryx
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

For macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

The project uses MCP SDK 1.x because its implementation relies on the `FastMCP` interface.

```text
mcp[cli]>=1.0,<2
```

### 4. Test Notes Management

```bash
python notes.py
```

This creates a sample note and verifies that saving, reading, listing, and keyword searching work correctly.

### 5. Run the MCP Client Integration Test

```bash
python test_client.py
```

The client automatically starts the server, initializes an MCP session, discovers the available tools, and executes test operations.

Expected tool names:

```text
server_status
create_note
get_note
get_all_notes
find_notes
```

## 🔌 Testing with MCP Inspector

MCP Inspector provides a graphical interface for testing MCP servers.

Start it with:

```bash
npx @modelcontextprotocol/inspector
```

Configure the server with:

| Field | Value |
|---|---|
| Server Name | Noryx |
| Transport | STDIO |
| Command | Path to your virtual environment's Python executable |
| Arguments | Absolute path to `server.py` |

Connect to the server and open the Tools section.

Select `create_note` and use the following example:

**Title:**

```text
AI Engineering
```

**Content:**

```text
Noryx is a Python MCP knowledge management server.
```

Execute the tool, then use `get_note` or `find_notes` to retrieve the saved information.

## 🧪 Example MCP Tool Operations

### Create a Note

**Tool:** `create_note`

```json
{
  "title": "AI Engineering",
  "content": "Noryx provides knowledge management through MCP tools."
}
```

**Expected result:**

```text
Note 'AI Engineering' saved successfully.
```

### Read a Note

**Tool:** `get_note`

```json
{
  "title": "AI Engineering"
}
```

### List All Notes

**Tool:** `get_all_notes`

```json
{}
```

### Search Notes

**Tool:** `find_notes`

```json
{
  "query": "knowledge"
}
```

Returns matching note titles and content.

## 🔐 Security & Design Decisions

Noryx uses a limited set of predefined tools rather than exposing arbitrary shell commands or unrestricted filesystem operations.

- Notes are stored in a dedicated local JSON file.
- Input validation prevents empty titles and content.
- Tool execution is limited to explicitly registered functions.
- Local note data is excluded from Git version control.
- No external database or paid API key is required.
- MCP communication uses stdio for local client integration.

This version is intended for trusted local development and testing, not as a publicly exposed multi-user service.

## ⚠️ Current Limitations

Noryx is a Version 1 MCP server.

- Keyword-based search only; semantic vector search is not implemented.
- Notes use their titles as identifiers; duplicate titles overwrite existing content.
- Storage is a single JSON file rather than a database.
- No built-in user authentication or multi-user permissions.
- No version history or recovery for overwritten notes.
- The server currently operates through local stdio transport.
- Integration with a specific AI chat application is not bundled with the project.

## 🗺️ Future Improvements

- Semantic knowledge retrieval
- SQLite database storage
- Note deletion and version history
- Tag-based organization
- MCP resource templates
- Multi-user authentication
- Remote MCP deployment
- Expanded AI client integrations

## 👨‍💻 Author

**Syed Ali Tarikh**

AI Engineering | Generative AI | Agentic Systems

GitHub: [@Tarikh792](https://github.com/Tarikh792)

---

**Noryx — Knowledge. Connected.**

*Built to explore standardized AI tool integration through the Model Context Protocol.*
