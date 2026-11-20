import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    server_path = Path(__file__).parent / "server.py"

    params = StdioServerParameters(
        command=sys.executable,
        args=[str(server_path)]
    )

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("Connected tools:")
            print([tool.name for tool in tools.tools])

            tests = [
                ("server_status", {}),
                ("create_note", {
                    "title": "MCP Test",
                    "content": "Noryx client integration works!"
                }),
                ("get_note", {"title": "MCP Test"}),
                ("get_all_notes", {}),
                ("find_notes", {"query": "integration"})
            ]

            for name, arguments in tests:
                result = await session.call_tool(
                    name,
                    arguments=arguments
                )

                print(f"\n{name}:")
                print(result.content)

                if result.isError:
                    print("Tool returned an error!")


if __name__ == "__main__":
    asyncio.run(main())