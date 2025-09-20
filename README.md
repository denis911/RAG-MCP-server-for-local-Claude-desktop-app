# FAQ-RAG MCP Server for Claude Desktop

A Model Context Protocol (MCP) server that provides FAQ search functionality using RAG (Retrieval-Augmented Generation) to Claude Desktop. This project enables Claude to search through your FAQ documents and provide relevant answers based on semantic similarity.

Inspiration is coming from here: https://www.youtube.com/watch?v=rnljvmHorQw

FAQ data and the code is taken from here: https://www.youtube.com/watch?v=W2EDdZplLcU

## 🚀 Features

- **FAQ Search**: Search through hundreds of FAQ entries with semantic relevance ranking
- **Real-time Integration**: Works directly with Claude Desktop through MCP protocol  
- **Easy Setup**: Simple configuration with minimal dependencies
- **Windows Compatible**: Tested and optimized for Windows 10/11

## 📋 Prerequisites

- Python 3.8 or higher
- Windows 10/11 (Mac/Linux should work but not tested)
- Claude Desktop application

## 🛠️ Installation & Setup

### Step 1: Download Claude Desktop

1. Go to [Claude.ai](https://claude.ai) and download Claude Desktop
2. Install Claude Desktop on your Windows machine
3. Create an account and sign in

### Step 2: Clone/Download This Repository

**Option A: Manual Download (Recommended)**
1. Download all files from this repository
2. Create a folder: `C:\mcp_projects\claude_desktop_FAQ_RAG_MCP\`
3. Place all files in this folder

**Option B: Git Clone**
```bash
git clone <this-repository-url>
cd claude_desktop_FAQ_RAG_MCP
```

### Step 3: Install Python Dependencies

```bash
pip install fastmcp minsearch toyaikit
```

**Or install globally:**
```bash
pip install --user fastmcp minsearch toyaikit
```

**Note:** The `requests` library is imported in `main.py` but not actually used since we load documents locally.

### Step 4: Test Your MCP Server

First, test that your server runs correctly:

```bash
cd C:\mcp_projects\claude_desktop_FAQ_RAG_MCP
python main.py
```

You should see output like:
```
Starting MCP server 'Search FAQ'...
INFO: Started server process [XXXX]
```

If successful, press `Ctrl+C` to stop the server.

### Step 5: Configure Claude Desktop

1. **Find your Claude Desktop config directory:**
   - Press `Win + R`
   - Type `%APPDATA%\Claude` and press Enter

2. **Create configuration file:**
   - Find a file named `claude_desktop_config.json` in the Claude folder
   - Add the following content:

```json
{
  "mcpServers": {
    "FAQ-RAG-MCP-server": {
      "command": "python",
      "args": ["C:\\mcp_projects\\claude_desktop_FAQ_RAG_MCP\\main.py"],
      "cwd": "C:\\mcp_projects\\claude_desktop_FAQ_RAG_MCP",
      "env": {
        "PYTHONPATH": "C:\\mcp_projects\\claude_desktop_FAQ_RAG_MCP"
      }
    }
  }
}
```

**⚠️ Important:** Replace the paths with your actual installation directory if different.

### Step 6: Restart Claude Desktop

1. **Completely close Claude Desktop** (don't just close the window)
   - Use Task Manager (`Ctrl + Shift + Esc`)
   - Look for "Claude" processes and end them
   - Or right-click the Claude icon in system tray and "Exit"

2. **Start Claude Desktop fresh**

3. **Wait 15-30 seconds** for the MCP server to initialize

### Step 7: Test the Connection

1. Look for a **hammer/tools icon** or "Search and tools" button in Claude Desktop
2. Click on it to see available tools
3. You should see "FAQ-RAG-MCP-server" listed
4. Test by asking Claude to search your FAQ database

## 🔧 Troubleshooting

### Problem: "No tools available" or tools button doesn't appear

**Solutions:**
1. **Check configuration file location:** Ensure `claude_desktop_config.json` is in `%APPDATA%\Claude\`
2. **Verify JSON syntax:** Use a JSON validator to check for syntax errors
3. **Try full Python path:**
   ```bash
   where python
   ```
   Use the full path in your config:
   ```json
   "command": "C:\\Users\\YourName\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
   ```
4. **Check file paths:** Ensure all paths in config are correct and use double backslashes (`\\`)

### Problem: MCP server starts but disconnects immediately

**Solutions:**
1. **Test server manually first:**
   ```bash
   python main.py
   ```
2. **Check for missing dependencies:**
   ```bash
   pip show fastmcp minsearch toyaikit
   ```
3. **Verify documents.json exists** in the same directory as main.py

### Problem: "Request timed out" errors

**Solutions:**
1. **Reduce document loading time** - The FAQ database might be too large
2. **Use the simple test server first:**
   ```bash
   python test_simple.py
   ```
3. **Check antivirus software** - It might be blocking the connection

### Problem: Permission denied or file not found errors

**Solutions:**
1. **Run Command Prompt as Administrator**
2. **Check file permissions** on your project directory
3. **Use absolute paths** instead of relative paths in configuration

## 📁 File Structure

```
claude_desktop_FAQ_RAG_MCP/
├── main.py                    # Main MCP server with SearchTools integration
├── search_tools.py           # FAQ search functionality and index management
├── test_simple.py            # Simple test server for troubleshooting
├── documents.json            # FAQ database (1000+ questions)
├── claude_desktop_config.json # Example configuration file
└── README.md                 # This file
```

## 🎯 Usage Examples

Once connected, you can interact with your FAQ database through Claude:

### Example 1: Technical Questions
**You ask:** "How to install Kafka on Windows?"

**Claude searches your FAQ and responds with:** 5 relevant answers from your database, ranked by relevance, covering Docker setup, Python integration, and troubleshooting.

### Example 2: Learning Resources
**You ask:** "What's the easiest way to learn DBT?"

**Claude provides:** Information combining internet search results, FAQ database answers, and its own knowledge for a comprehensive learning path.

### Example 3: Troubleshooting
**You ask:** "I'm getting a Docker permission error"

**Claude searches:** Your FAQ database for similar issues and provides specific solutions from other users' experiences.

## 🎉 Benefits

- **Instant Access**: Search hundreds of FAQ entries instantly
- **Contextual Answers**: Get relevant answers ranked by similarity
- **Local Processing**: Your data stays on your machine
- **Extensible**: Easy to add more documents or modify search logic
- **Integration**: Works within Claude Desktop interface


## 📝 Technical Details

- **Framework**: FastMCP for MCP protocol implementation
- **Search Engine**: MinSearch with AppendableIndex for document indexing and retrieval
- **Integration**: toyaikit.tools for wrapping SearchTools methods as MCP tools
- **Transport**: Default MCP transport (stdio) for reliable Claude Desktop communication
- **Data Storage**: JSON-based FAQ storage with course categorization and metadata
- **Search Features**: 
  - Semantic search across question, text, and section fields
  - Course filtering (currently set to 'data-engineering-zoomcamp')
  - Boost weighting (questions: 3.0x, sections: 0.5x)
  - Returns top 5 most relevant results - hard-coded for now, could be any number required

## 🆘 Getting Help

If you're still having issues:

1. **Check Claude Desktop logs** for error messages
2. **Test with the simple server first** (`test_simple.py`)
3. **Verify all file paths** are correct in your configuration
4. **Ensure Python dependencies** are properly installed
5. **Try different Python versions** if compatibility issues arise

## 🏷️ Version Info

- **Tested with**: Claude Desktop v0.13.19
- **Python**: 3.8+
- **Platform**: Windows 10/11 (should work on Mac/Linux)

---

**Happy searching!** 🔍 Your FAQ database is now at your fingertips through Claude Desktop.
