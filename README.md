# 「帳目分析可視化程式（Python）」
## Visualize Your Finance (Python) Made by CHE_72 ZStudio

## 狀態徽章 (Badges)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/CHE-72-ZStudio/Visualize-Your-Finance-Python)
    [![GitHub Release](https://img.shields.io/github/v/release/CHE-72-ZStudio/Visualize-Your-Finance-Python)](https://github.com/CHE-72-ZStudio/Visualize-Your-Finance-Python/releases)
    [![GitHub License](https://img.shields.io/github/license/CHE-72-ZStudio/Visualize-Your-Finance-Python)](https://github.com/CHE-72-ZStudio/Visualize-Your-Finance-Python/blob/main/LICENSE)
    [![GitHub Last Commit](https://img.shields.io/github/last-commit/CHE-72-ZStudio/Visualize-Your-Finance-Python)](https://github.com/CHE-72-ZStudio/Visualize-Your-Finance-Python/commits)
    [![Python 3.10+](https://img.shields.io/badge/Python%203.10+-3776AB.svg?logo=python&logoColor=white)](https://www.python.org)
    [![PyCharm](https://img.shields.io/badge/PyCharm-000000.svg?logo=PyCharm&logoColor=white)](https://www.jetbrains.com/pycharm/)
> 「Ask DeepWiki」功能為由 Devin AI 生成的 Wiki 文檔，每週自動刷新一次，內容可能與最新版程式有所差異  
> 該 AI 生成的 Wiki 文檔與回覆內容僅供參考，我們對其不負任何擔保責任，實際情形請依本儲存庫最新提交為準  

## 程式介紹 (Description)
「帳目分析可視化程式」是一款 CLI 程式，可以自動分析您的帳目數據並用各種直觀圖表與排名顯示，進而協助您達成管理金錢花費、開源節流的目的。  
本分析程式同時支援分析支出與分析收入的功能，還可以直接新增帳目數據並儲存至檔案中，讓您的帳目分析一站式搞定，節省下大量的時間並快速獲得想要的結果。  

## 程式功能 (Features)
* 📈 **多樣化圖表類型**：支援折線走勢圖、長條比較圖、圓餅佔比圖的顯示，直觀地感受每個月花錢的變化，或是不同類別之間賺錢的差異。  
* 🏅 **排名顯示細節**：以清晰的格式查看花費排名，並能顯示詳細的類別、日期、金額、名稱，協助您找出花費最大的項目，或是收益最大的內容。  
* ⏳ **可選分析時間段**：提供各種分析時間段，除了可以分析所有紀錄外，還提供其他時間段。您甚至還可以選擇觀察每年 5 月的變化，看看哪一年的 5 月花費最多錢！  
* 🗂️ **可選帳目類別**：提供各種帳目類別，除了可以分析所有紀錄外，還提供其他分析選擇。像是可以看看每個月在購物花費上花費多少錢，或是每年在副業收入上額外賺了多少錢！  
* ⌨️ **易用的命令行介面**：透過不同的顏色顯示、完整的說明指引與簡易的數字選單，幫助您快速完成分析帳目的工作，節省大量時間。  

## 環境需求 (Requirements)
- Microsoft Windows  
    * Windows 10+ 64位元（2004 以上版本）搭配 [Windows 終端機 (Windows Terminal)](https://aka.ms/terminal)
        * Windows 11+ 已預裝 Windows 終端機，無須另外安裝
- Apple macOS  
- Linux
> 一般的 Windows 使用者可以直接從 Releases 頁面直接下載 `VSPF-Win-X.Y.ZZ.zip`
> 目前僅建議專業開發者直接在 Apple macOS / Linux 編譯運行本程式，我們預計會在未來發行可供一般使用者執行的可執行二進制檔，詳情可見「未來功能」區塊

## 使用說明 (Instructions)
1. 從 GitHub 上的 [Releases](https://github.com/CHE-72-ZStudio/Visualize-Your-Finance-Python/releases) 頁面下載對應系統的壓縮包 `VYFP-OS-X.Y.ZZ.zip`，解壓縮後放置於適當的位置  
2. 雙擊打開本程式的可執行二進制檔案 `VYFP-X.Y.ZZ-OS`，即可開始使用本程式  
3. 進入「功能選擇平臺」，依據您所想要使用的功能輸入對應的半形數字後按下 `Enter/Return` 按鍵  
4. 進入「時間選擇平臺」，依據您所想要分析的時間段輸入對應的半形數字後按下 `Enter/Return` 按鍵  
    - （如果有的話）輸入後會出現時間提示，依據您所想要分析的時間段與提示輸入整數西元年、整數月份或整數日期，請注意僅能輸入半形數字
5. 進入「分析選擇平臺」，依據您所想要分析的圖表呈現方式輸入對應的半形數字後按下 `Enter/Return` 按鍵  
    - （如果有的話）進入「類別選擇平臺」，依據您所想要分析的帳目類別輸入對應的半形數字後按下 `Enter/Return` 按鍵  
6. 現在應該會彈出一個顯示圖表的視窗或會在終端顯示出排名資料  
    - 如果彈出顯示圖表的視窗，您可以對其放大、縮小、存檔，在您關閉該圖表視窗後可以繼續進行下一步操作  
    - 如果是在終端顯示出排名資料，在終端顯示所有排名資料且您已完成閱覽後，可以進行下一步操作  
7. 這時應該會回到「時間選擇平臺」，您可以繼續不同時間段、不同圖表、不同類別的分析；也可以選擇返回「功能選擇平臺」，或是分析完成後可以直接依照指示輸入對應的半形數字後按下 `Enter/Return` 按鍵以結束程式  
> 若您輸入的內容有誤，本程式將會自動提醒您，並提示即將返回的介面，以供您做好準備  
> 我們在程式中隱藏了一些有趣的小彩蛋，等待您來發掘！  
> 詳細的 用戶手冊可以參考 [USER.md](https://github.com/CHE-72-ZStudio/Visualize-Your-Finance-Python/blob/main/USER.md) 文件；開發手冊可以參考 [DEVELOPER.md](https://github.com/CHE-72-ZStudio/Visualize-Your-Finance-Python/blob/main/DEVELOPER.md) 文件  

## V1.2.12 更新日誌 (Changes in V1.2.12)
* 新增功能 Added
    - 在「分析選擇平臺」新增可以顯示不同時間段與不同類別的 支出／收入 金額總和
* 功能修復 Fixed
    - 修復了「類別選擇平臺」中的選單數字顯示錯誤的問題，現在類別編號可以正常從 1 開始顯示
    - 修復了在「時間選擇平臺」選擇「時間4：特定日期的紀錄」時，會因為運行多餘的檢查而出現異常的「沒有符合條件的資料」錯誤，導致無法正常進行分析的問題
* 提升進步 Improved
    - 顯示折線圖的時候，現在除了線條變得更明顯外，也在各個數值點上顯示點形標記，增加可閱讀性
    - 顯示折線圖的時候，現在會在每個數值點的右上方顯示其對應的金額數值內容，更為方便查看存取
    - 顯示長條圖的時候，現在會一併顯示背景格線，讓 金額／次數 對照更容易
    - 顯示長條圖的時候，現在會依照順序輪換顏色，更容易分辨不同的類別
    - 顯示長條圖的時候，現在會在每個長條的上方顯示其對應的 金額／次數 數值內容，更為方便查看存取
    - 顯示圓餅圖的時候，現在會忽略那些 0 元／次 的數值內容與類別標籤，避免因冗餘的重疊內容影響視覺與數據判讀
* 已經移除 Removed
    - 移除與 `LICENSE` 內容重複的 `License_EN.txt`，現在 `Main.py` 輸出英文原版的開源許可時會直接讀取原始的 `LICENSE`
    - 將 `License_ZH.txt` 重新命名為 `LICENSE_ZH`，維持文件命名邏輯的一致性，現在 `Main.py` 輸出中文翻譯的開源許可時會讀取 `LICENSE_ZH`
* 文檔更新 Edited
    - 更新 `USER.md` 以符合最新新增與調整的程式功能
    - 在 `DEVELOPER.md` 中新增「5. 專案結構」區塊，方便開發者快速上手本程式架構與各個檔案用途
> 所有更新紀錄可參閱 [CHANGELOG.md](https://github.com/CHE-72-ZStudio/Visualize-Your-Finance-Python/blob/main/CHANGELOG.md) 文件  

## V1.2.12 已知問題 (Known Issues in V1.2.12)
| 問題編號 (Issues Num) | 錯誤標題 (Issues Title) | 影響程度 (Priority) | 修復狀態 (Status)        | 替代方案(Workaround) | 詳細內容 (Datails)                                     | 
|-------------------|---------------------|-----------------|----------------------|------------------|----------------------------------------------------|
| *None*            | 圖表無法正確顯示中文字         | 邊緣 (Minor)      | 正在調查 (Investigating) | 無                | 在 macOS/Linux 上使用時，若系統內並未安裝微軟正黑體，可能無法在圖表視窗中正確顯示中文字 |
> 如果您有發現任何其他這裡未列出的問題，歡迎向本存儲庫提出問題 (Issues) 與程式建議 (PR)  

## 未來功能 (Future Features)
| 未來版本        | 增加功能                                          | 開發狀態              | 優先順序       | 預定發布          |
|-------------|-----------------------------------------------|-------------------|------------|---------------|
| ***1.3.2*** | 在 `Func.py` 的 `analyze()` 中新增可以顯示「隨時間變化的次數」功能 | 功能規劃 (Planning)   | 中 (Medium) | ***2025-07*** |
| ***1.3.2*** | 在資料夾中沒有 `Record.csv` 時，可以自動新增該檔案，避免因缺少檔案而無法運行 | 功能規劃 (Planning)   | 中 (Medium) | ***2025-07*** |
| ***1.3.2*** | 調整 `USER.md` 中的說明方式，使其更為完整易懂                  | 功能規劃 (Planning)   | 低 (Low)    | ***2025-07*** |
| 1.4.0       | 增加可以寫入 `Diagnose.Log` 日誌檔案的功能                 | 功能規劃 (Planning)   | 中 (Medium) | 2025-08       |
| 1.4.1       | 增加更多例外情形處理                                    | 正在討論 (Discussing) | 低 (Low)    | 2025-08       |
| 1.4.2       | 可執行檔集成華為 HarmonyOS Sans 字體                    | 正在討論 (Discussing) | 低 (Low)    | 2025-??       |
| 1.4.5       | 提升跨系統顯示相容性，並開始發行 macOS/Linux 可執行檔             | 功能規劃 (Planning)   | 低 (Low)    | 2026-??       |
| 1.5.0       | 優化調整程式邏輯與選單功能，為即將新增的 GUI 功能做準備                | 功能規劃 (Planning)   | 低 (Low)    | 2026-??       |
| ***2.0.0*** | 增加跨系統平臺的通用 GUI，增進使用者體驗                        | 功能規劃 (Planning)   | 中 (Medium) | ***2026-??*** |
> 實際發布時間可能會因為當下開發情形而有所提前或延後，敬請耐心等候  
> 如果您有其他的功能需求或建議，歡迎向本存儲庫提出問題 (Issues) 與程式建議 (PR)  

## 貢獻清單 (Contributors)
- [![CHE72](https://img.shields.io/badge/CHE72-181717.svg?logo=github&logoColor=white)](https://github.com/CHE72): 專案發起人／項目**唯一**貢獻者／項目**唯一**維護者  

## 授權許可 (License)
本專案使用 GNU General Public License v3 開源許可，詳細開源授權許可內容可參閱 [LICENSE](https://github.com/CHE-72-ZStudio/Visualize-Your-Finance-Python/blob/main/LICENSE) 文件  
> 注意：所有對此程式碼的修改與衍生版本，都必須以 GNU GPLv3 授權釋出。  

### 帳目分析可視化程式（Python），著作權所有 (C) 2025-現在 CHE_72 ZStudio  
#### Visualize Your Finance (Python), Copytight (C) 2025-present CHE_72 ZStudio.  
