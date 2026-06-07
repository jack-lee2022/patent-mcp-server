# Patent MCP Server

一個專為專利分析打造的 MCP (Model Context Protocol) 伺服器，將底層專利檢索、下載、與深度分析模組封裝為 AI 可直接呼叫的工具。

## 系統架構
本專案採用「插件式 (Plugin-based)」架構，方便新增檢索、下載或分析功能。
- **Core Engine**: 整合 Google Patents 的自動化抓取與 Playwright 渲染 fallback。
- **Expert Analysis**: 內建權利要求拆解 (Claim Chart)、引證分析與法律狀態計算。
- **Extensible Plugins**: 擴充目錄位於 `plugins/`，支援動態載入。

## 安裝步驟

### 1. 前置需求
- Python 3.10+
- 已安裝 Playwright: `python -m playwright install chromium`

### 2. 安裝依賴
```bash
pip install -r requirements.txt
```

### 3. 執行服務
```bash
python server.py
```

## AI Agent 連接配置
在您的 Claude Desktop 或其他支持 MCP 的用戶端設定檔 (如 `claude_desktop_config.json`) 中加入：

```json
{
  "mcpServers": {
    "patent-analysis": {
      "command": "python",
      "args": ["C:/Users/arkep/patent-mcp-server/server.py"]
    }
  }
}
```

## 功能調用
安裝後，AI Agent 將自動識別以下專利工具：
- `search_patents`: 進行大規模關鍵字或申請人檢索。
- `download_patent`: 獲取專利 PDF 與圖像附件。
- `get_legal_status`: 計算專利屆滿日與狀態。
- `claim_analysis`: 執行自動化的 Claim Chart 侵權對照。
- `citation_snowball`: 追蹤技術引證脈絡。
- `generate_landscape_viz`: 生成申請人趨勢與地圖。
- `advise_deployment_strategy`: 提供專利佈局策略建議。

## 授權
MIT
