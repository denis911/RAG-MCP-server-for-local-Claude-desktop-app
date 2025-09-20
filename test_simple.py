from fastmcp import FastMCP

mcp = FastMCP("Simple Test")

@mcp.tool
def hello_world():
    """A simple hello world function"""
    return "Hello from MCP!"

if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run()

    