# MCP Demo

A minimal demo showing how the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) works, built with [FastMCP](https://github.com/jlowin/fastmcp).

MCP is a protocol that lets applications expose tools/functions to LLM clients in a standard way. This repo has two parts:

- [server.py](server.py) — defines an MCP server exposing a single tool, `add`, which adds two numbers.
- [call.py](call.py) — a client that connects to the server and calls the `add` tool.

## Requirements

- Python 3.10+
- [fastmcp](https://pypi.org/project/fastmcp/)

Set up a virtual environment and install it:

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install fastmcp
```

## Running the demo

With the virtual environment activated, run the client, which starts the server as a subprocess and calls its `add` tool:

```bash
python3 call.py
```

You should see the result of the tool call printed to the console.

When you're done, deactivate the virtual environment:

```bash
deactivate
```

## How it works

1. `server.py` creates a `FastMCP` server and registers `add` as a tool using the `@mcp.tool()` decorator.
2. `call.py` creates an MCP `Client` pointed at `server.py` and calls the `add` tool by name with arguments, over the MCP protocol.
3. The server receives the request, runs the `add` function, and returns the result to the client.
