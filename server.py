import os
import importlib
from mcp.server.fastmcp import FastMCP

# 初始化 MCP 服務
mcp = FastMCP("Patent-Analysis-Suite")

# 自動掃描 plugins 目錄下的模組並註冊
plugin_dir = "plugins"
for filename in os.listdir(plugin_dir):
    if filename.endswith(".py") and filename != "__init__.py":
        plugin_name = filename[:-3]
        module = importlib.import_module(f"{plugin_dir}.{plugin_name}")
        
        # 假設每個插件都有一個 register_tools(mcp) 函數
        if hasattr(module, "register_tools"):
            module.register_tools(mcp)
            print(f"[SYSTEM] 已註冊插件: {plugin_name}")

if __name__ == "__main__":
    mcp.run()
