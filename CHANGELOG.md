# 「帳目分析可視化程式（Python）」的變更日誌
## Change Log for Visualize Your Finance (Python)

## V1.1.5 (2025-06-10)
### 新增功能 Added
- 在 `Func.py` 中新增 `write_record()` 函數，現在可以使用本程式在 `Record.csv` 內新增帳目數據  
- 開始正式發行能在 Windows 上運行的可執行檔壓縮包
### 提升進步 Improved
- 在 `Func.py` 中的 `analyze()`「時間選擇平臺」中新增更為完善的邊界檢查，可以應對數據列表為空的情形  
- 在 `Main.py` 中計算資產時，現在會使用分隔位顯示金額，提升可閱讀性與清晰度  
### 文檔更新 Edited
- 在 `README.md` 中新增對於「Ask DeepWiki」徽章的描述與免責聲明  
- 移除 `MANUAL.md` ，新增 `USER.md` 與 `DEVELOPER.md`  
### 貢獻清單 Contributor
- [![CHE72](https://img.shields.io/badge/CHE72-181717.svg?logo=github&logoColor=white)](https://github.com/CHE72): 專案發起人／項目**唯一**貢獻者／項目**唯一**維護者  

## V1.0.11 (2025-06-08)
### 新增功能 Added
- 在 `Func.py` 中的 `cat_question()` 「類別選擇平臺」中新增邊界檢查，可以檢查使用者輸入的類別編號是否超出邊界，避免出現空白圖表或排名而影響使用者體驗
- 在 `Func.py` 中的 `analyze()`「時間選擇平臺」中輸入年、月、日時新增邊界檢查，可以檢查使用者輸入的年、月、日是否超出邊界，避免出現空白圖表或排名而影響使用者體驗
- 在 `Studio.py` 中新增 `__main__` 檢查，避免使用者誤啟動該模組
### 功能修復 Fixed
- 修復 `Func.py` 中的 `pretreat()` 開啟 UTF-8 編碼的 `Record.csv` 會出現無法解碼的錯誤
### 提升進步 Improved
- 調整 CLI 輸出時的顏色變化，讓不同情境出現的提示更為顯著，提升使用者體驗
- `.gitignore` 中新增 Windows 與 macOS 的模板，避免提交操作系統產生的多餘檔案
- `.gitignore` 中新增 `Record.csv`，避免提交開發人員私人的帳目資料
- 在 `Main.py` 中新增一些驚喜的小彩蛋，供使用者發掘，提升用戶體驗
### 文檔更新 Edited
- 修正 `Main.py`、`MANUAL.md` 中部分功能的描述說明，使之符合最新版程式
- 新增 `Example.csv` 檔案，供使用者參考實際使用格式
### 已經移除 Removed
- 因已完成作業繳交，移除 `MakeRecord.py` 檔案，使其符合一般使用者的使用方式
### 貢獻清單 Contributor
- [![CHE72](https://img.shields.io/badge/CHE72-181717.svg?logo=github&logoColor=white)](https://github.com/CHE72): 專案發起人／項目**唯一**貢獻者／項目**唯一**維護者  

## V1.0.0 (2025-05-29)
### 首次正式版本發佈 First Release
- 使用 CLI 介面與 ANSI 轉義碼顯示 8 位元顏色
- 具備基礎的讀取 `Record.csv` 與繪圖分析功能
### 棄用淘汰 Deprecated
- `MakeRecord.py` 檔案為用於產生虛擬的帳目資料供繳交作業時使用，將於下次小版本更新時移除該檔案
### 貢獻清單 Contributor
- [![CHE72](https://img.shields.io/badge/CHE72-181717.svg?logo=github&logoColor=white)](https://github.com/CHE72): 專案發起人／項目**唯一**貢獻者／項目**唯一**維護者  

### 帳目分析可視化程式（Python），著作權所有 (C) 2025-現在 CHE_72 ZStudio
#### Visualize Your Finance (Python) , Copytight (C) 2025-present CHE_72 ZStudio.
