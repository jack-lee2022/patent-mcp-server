import subprocess
from mcp.server.fastmcp import FastMCP

def register_tools(mcp: FastMCP):
    
    @mcp.tool()
    def generate_landscape_viz(data_csv: str) -> str:
        """生成申請人趨勢圖與技術地圖。"""
        cmd = ["python", "scripts/advanced/visualizer.py", data_csv]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout

    @mcp.tool()
    def analyze_white_space(ipc_code: str) -> str:
        """根據分類號分析技術領域空白區。"""
        # 這裡未來可對應到 classification_analyzer.py
        cmd = ["python", "scripts/classification_analyzer.py", "--ipc", ipc_code]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
