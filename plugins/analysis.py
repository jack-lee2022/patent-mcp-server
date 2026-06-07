import subprocess
from mcp.server.fastmcp import FastMCP

def register_tools(mcp: FastMCP):
    
    @mcp.tool()
    def get_legal_status(filing_date: str) -> str:
        """計算專利預計屆滿日與法律狀態。"""
        cmd = ["python", "scripts/advanced/legal_status_calculator.py", filing_date]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout

    @mcp.tool()
    def claim_analysis(patent_id: str, product_desc: str) -> str:
        """執行權利要求拆解 (Claim Chart) 分析。"""
        cmd = ["python", "scripts/advanced/claim_chart_gen.py", patent_id, product_desc]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout

    @mcp.tool()
    def citation_snowball(patent_id: str) -> str:
        """自動追蹤專利前後引證關係。"""
        cmd = ["python", "scripts/advanced/citation_crawler.py", patent_id]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
