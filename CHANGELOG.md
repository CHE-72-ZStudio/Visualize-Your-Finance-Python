# 「帳目分析可視化程式（Python）」的變更日誌
## Change Log for Visualize Your Finance (Python)

## UNRELEASED ~~V1.0.5 (2025-MM-DD)~~
### 新增功能 Added
- 在 `Func.py` 中的 `cat_question()` 「類別選擇平臺」中新增邊界檢查，可以檢查使用者輸入的類別編號是否超出邊界，避免出現空白圖表或排名而影響使用者體驗
- 在 `Func.py` 中的 `analyze()`「時間選擇平臺」中輸入年、月、日時新增邊界檢查，可以檢查使用者輸入的年、月、日是否超出邊界，避免出現空白圖表或排名而影響使用者體驗
- 在 `Studio.py` 中新增 `__main__` 檢查，避免使用者誤啟動該模組
### 提升進步 Improved
- 調整 CLI 輸出時的顏色變化，讓不同情境出現的提示更為顯著，提升使用者體驗
### 文檔更新 Edited
- 修正 `Main.py`、`MANUAL.md` 中的描述說明，使之符合最新版程式
### 貢獻清單 Contributor
- [CHE72](https://github.com/CHE72): 專案發起人／項目**唯一**貢獻者／項目**唯一**維護者  

## V1.0.0 (2025-05-29)
### 首次正式版本發佈 First Release
- 使用 CLI 介面與 ANSI 轉義碼顯示 8 位元顏色
- 具備基礎的讀取 `Record.csv` 與繪圖分析功能
### 貢獻清單 Contributor
- [CHE72](https://github.com/CHE72): 專案發起人／項目**唯一**貢獻者／項目**唯一**維護者  

### 「帳目分析可視化程式（Python）」，著作權所有 (C) 2025-present CHE_72 ZStudio
#### Visualize Your Finance (Python) , Copytight (C) 2025-present CHE_72 ZStudio.
