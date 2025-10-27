# 🗂️ TaskMaster - 個人任務管理系統

一個簡單的任務管理應用程式，提供桌面介面與 Web API，讓你輕鬆管理日常任務。

---

## 📖 專案簡介

**TaskMaster** 是一款個人任務管理工具，幫助你追蹤與管理每日工作。  
支援桌面 GUI 操作與 Web API 呼叫。

---

## ✨ 功能需求

### 📌 應具備的基本功能
- **任務管理**：新增、檢視、刪除任務  
- **狀態追蹤**：待辦、進行中、已完成  
- **優先級設定**：低、中、高 三個等級  
- **持久化儲存**：資料保存在本地 SQLite 資料庫  

### 🧱 模組結構
| 模組 | 說明 |
|------|------|
| `database.py` | 資料庫設定 |
| `task_gui.py` | Tkinter 圖形介面 |
| `api_server.py` | RESTful API 介面 |
| **資料格式** | JSON 回應 |

### 🧩 資料結構
任務包含：
- 標題 (`title`)
- 描述 (`description`)
- 優先級 (`priority`)
- 狀態 (`status`)
- 建立時間 (`created_at`)

---

## ⚙️ 快速開始

### 📦 安裝
```bash
cd taskmaster
uv sync   # 安裝 pyproject.toml 中列出的所有套件
```

## ▶️ 使用方式

#### 🖥️ 桌面介面
```bash
uv run python main.py gui
```

#### 🌐 Web API 服務
```bash
uv run python main.py api
```

## 🏗️ 技術架構

| 元件 | 技術 |
|------|------|
| 語言 | Python 3.10+ |
| GUI | Tkinter |
| Web | 框架	Flask |
| 資料庫 | SQLite |
| API	| RESTful JSON |

---

## 📄 授權

本專案僅供學習與練習使用。

---

## 🔗 相關連結

- [Python 官方文件](https://docs.python.org/3/)
- [Flask 文件](https://flask.palletsprojects.com/)
- [Tkinter 教學](https://docs.python.org/3/library/tkinter.html)

