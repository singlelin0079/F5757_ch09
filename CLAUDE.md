# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 文件撰寫規則

撰寫文件請一律使用中文（含回應內容）。若任務是撰寫分析類文件，須包含以下章節：程式碼風格問題、主要相依套件、執行環境、已經架構問題。

## 專案概觀

TaskMaster 是一個示範用的個人任務管理系統（桌面 GUI + Web API + SQLite）。**這個 repo 是刻意寫成「壞範例」的教材**（見 `main.py` 開頭註解：「全部寫在一個檔案裡（糟糕的做法）」），用於練習程式碼審查與重構，而不是一個乾淨的正式專案。修改前請留意：檔案之間存在大量重複、互相衝突、未整合的實作，這是設計如此，不是意外。

## 常用指令

```bash
uv sync                        # 安裝 pyproject.toml 中的相依套件
uv run python main.py gui      # 啟動 Tkinter 桌面介面（main.py 內建版本）
uv run python main.py api      # 啟動 Flask API（port 5000，main.py 內建版本）
uv run python api_server.py    # 啟動另一個獨立、未整合的 Flask API（port 8080）
uv run python check_db.py      # 印出 tasks.db 的 schema（PRAGMA table_info）
```

專案沒有設定 lint / formatter，也沒有任何測試框架或測試檔案。

## 架構重點

- **`main.py`** 是實際的程式進入點（`gui` / `api` 兩種模式），但註解已說明它「應當只做為一個門戶入口」——目前卻把 `Task` 類別、SQLite 存取函式、Tkinter GUI（`TaskGUI`）、Flask API 路由全部塞在同一檔案裡。
- **`database.py`** 定義了另一個獨立的 `DatabaseManager`，在被 import 時就會建立自己的資料庫連線並建表（`db_manager = DatabaseManager()` 為模組層級的全域副作用）。這與 `main.py` 的 `connect_db()` 是兩條互不相關的資料庫初始化路徑；其餘檔案（`task_gui.py`、`utils.py`、`backup.py`）又各自用 `sqlite3.connect("tasks.db")` 開新連線，全專案沒有共用的 DB 存取層。
- **`api_server.py`** 是嘗試把 API 從 `main.py` 抽離出來的第二份實作，但路由路徑（`/tasks` vs. `/api/tasks`）、回傳格式、port（8080 vs. 5000）都與 `main.py` 不一致，且未被任何檔案 import 或啟用；功能也不完整（缺刪除、狀態轉換）。
- **`task_gui.py`** 同樣是想把 GUI 從 `main.py` 抽出來的第二份實作（`TaskManagerGUI`），欄位與互動邏輯與 `main.py` 的 `TaskGUI` 不同，同樣未被整合進主程式。
- **`utils.py`** 是一堆彼此無關的工具函式（日期解析、MD5 弱雜湊、簡陋 email 驗證、任務計數、JSON 備份、log 寫檔、優先權評分、文字清理），目前沒有任何檔案實際呼叫這些函式。
- **`backup.py`** 是未完成的草稿（`old_add_task`、`OldGUI` 均無實作），非可執行的備份工具。
- **`config.py`** 定義了 Flask/SQLAlchemy 風格的 `Config` 及一堆常數，但目前沒有任何檔案 import 它。
- `main.py` 與 `config.py` 都內含寫死的 `API_KEY = "sk-1234567890abcdef"`；修改這類檔案時不要把假密鑰誤當成需要保留的正式機密。
- `tasks.db`（SQLite，根目錄）在執行任一進入點時可能被上述任一條初始化路徑重新建立/開啟，欄位定義在 `main.py`、`database.py` 中有些微差異（例如 `status`/`priority` 是否有預設值、`id` 是否 `AUTOINCREMENT`）。

## 環境

- Python 版本由 `.python-version`（`3.11.8`）與 `pyproject.toml`（`requires-python = ">=3.11.8"`）鎖定。
- 套件管理使用 `uv`（`uv.lock` 已存在），主要相依套件為 `flask==3.0.3`、`requests>=2.32.5`；`sqlite3`、`tkinter` 為標準函式庫內建。
