import subprocess
from mcp.server.fastmcp import FastMCP

def register_tools(mcp: FastMCP):
    
    @mcp.tool()
    def advise_deployment_strategy(technology: str, goal: str) -> str:
        """根據技術與目標推薦專利佈局策略。"""
        # 這是一個純 LLM 驅動的工具，不需要額外腳本
        # 在這裡實現該模型對應的邏輯，或調用 LLM API
        return f"針對 {technology} 且目標為 {goal}，建議參考專利地圖後，採取「圍牆式佈局」保護核心特徵，並對競爭對手執行「斷路式」卡位。"
