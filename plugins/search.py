import subprocess
from mcp.server.fastmcp import FastMCP

def register_tools(mcp: FastMCP):
    
    @mcp.tool()
    def search_patents(query: str, assignee: str = None, max_results: int = 20) -> str:
        """使用專利搜尋引擎檢索關鍵字或申請人專利。"""
        cmd = ["python", "scripts/google_patents_collector.py"]
        if assignee:
            cmd.extend(["--assignee", assignee])
        if query:
            cmd.extend(["--query", query])
        cmd.extend(["--max", str(max_results), "--no-tor"])
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout if result.stdout else result.stderr

    @mcp.tool()
    def download_patent(patent_id: str) -> str:
        """下載專利全文 PDF。"""
        # 調用下載器
        cmd = ["python", "scripts/google_patents_collector.py", "--query", patent_id, "--enrich", "--max", "1", "--no-tor"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return f"下載請求已發送至 {patent_id}: {result.stdout}"
