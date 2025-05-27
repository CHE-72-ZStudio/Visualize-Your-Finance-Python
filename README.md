# 「帳目分析可視化程式（Python）」
## Visualize Your Finance (Python) Made by CHE_72 ZStudio

## 狀態徽章 (Badges)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/CHE-72-ZStudio/Visualize-Your-Finance-Python)  

## 程式介紹 (Description)
「帳目分析可視化程式」是一款 CLI 程式，可以自動分析您的帳目數據並用各種直觀圖表與排名顯示，進而協助您達成管理金錢花費、開源節流的目的。  
本分析程式同時支援分析支出與分析收入的功能，讓您的帳目分析一站式搞定，節省下大量的時間並快速獲得想要的結果。  

## 程式功能 (Features)
* 📈 **多樣化圖表類型**：支援折線走勢圖、長條比較圖、圓餅佔比圖的顯示，直觀地感受每個月花錢的變化，或是不同類別之間賺錢的差異。  
* 🏅 **排名顯示細節**：以清晰的格式查看花費排名，並能顯示詳細的類別、日期、金額、名稱，協助您找出花費最大的項目，或是收益最大的內容。  
* ⏳ **可選分析時間段**：提供各種分析時間段，除了可以分析所有紀錄外，還提供其他時間段。您甚至還可以選擇觀察每年 5 月的變化，看看哪一年的 5 月花費最多錢！  
* 🗂️ **可選帳目類別**：提供各種帳目類別，除了可以分析所有紀錄外，還提供其他分析選擇。像是可以看看每個月在購物花費上花費多少錢，或是每年在副業收入上額外賺了多少錢！  
* ⌨️ **易用的命令行介面**：透過不同的顏色顯示、完整的說明指引與簡易的數字選單，幫助您快速完成分析帳目的工作，節省大量時間。  

## 環境需求 (Requirements)
+ Python (>=3.10)（支援 match...case... 語法）  
    * 本專案的依賴項與模組需求已在 `Requirements.txt` 文件中列出。您可以使用 pip 安裝所有依賴： `pip install -r Requirements.txt`  
+ 支援 ANSI 轉義碼與中文字體顯示的終端輸出程式（ANSI 轉義碼用於 8 位元顏色顯示）  

- Microsoft Windows  
    * 對於一般使用者，建議使用 Windows 10+ 搭配 Windows Terminal ，容易上手使用  
    * 對於專業開發者，本程式可以搭配自身習慣且支援 8 位元顏色顯示的終端使用  
    > 目前僅建議專業開發者直接編譯運行本程式，我們預計會在未來發行可供一般使用者執行的可執行二進制檔，詳情可見「未來功能」區塊  
- Apple macOS / Linux  
    * 本程式尚未進行關於 macOS / Linux 的相容性測試  
    * 您可以先為此程式的相容性進行測試，若使用中遇到任何問題，歡迎向本存儲庫提出問題 (Issues) 與建議 (PR)  
    > 我們預計會在未來增加對這些系統的兼容，並發行可執行二進制檔，詳情可見「未來功能」區塊  

## 使用說明 (Instructions)
1. 下載本封裝程式檔案並依照規範修改 `Record.csv` 檔案，使其符合您的真實帳目內容  
2. 確保 `Record.csv` 與 `Main.py` 放置於同一位置後，在該文件夾下開啟終端並輸入 `python Main.py` 以執行 `Main.py`  
3. 進入「功能選擇平臺」，依據您所想要使用的功能輸入對應的半形數字後按下 `Enter/Return` 按鍵  
4. 進入「時間選擇平臺」，依據您所想要分析的時間段輸入對應的半形數字後按下 `Enter/Return` 按鍵  
    - （如果有的話）輸入後會出現時間提示，依據您所想要分析的時間段與提示輸入整數西元年、整數月份或整數日期，請注意僅能輸半形數字
5. 進入「分析選擇平臺」，依據您所想要分析的圖表呈現方式輸入對應的半形數字後按下 `Enter/Return` 按鍵  
6. （如果有的話）進入「類別選擇平臺」，依據您所想要分析的帳目類別輸入對應的半形數字後按下 `Enter/Return` 按鍵  
7. 現在應該會彈出一個顯示圖表的視窗或會在終端顯示出排名資料  
    - 如果彈出顯示圖表的視窗，您可以對其放大、縮小、存檔，在您關閉該圖表視窗後可以繼續進行下一步操作  
    - 如果是在終端顯示出排名資料，在終端顯示所有排名資料且您已完成閱覽後，可以進行下一步操作  
8. 這時應該會回到「時間選擇平臺」，您可以繼續不同時間段、不同圖表、不同類別的分析；也可以選擇返回「功能選擇平臺」，或是分析完成後可以直接依照指示輸入對應的半形數字後按下 `Enter/Return` 按鍵以結束程式  
> 若您輸入的內容有誤，本程式將會自動提醒您，並提示即將返回的介面，以供您做好準備  
> 更為詳細的使用說明與 Record.csv 檔案規範可以參考 [MANUAL.md](https://github.com/CHE-72-ZStudio/Visualize-Your-Finance-Python/blob/main/MANUAL.md) 文件  

## V1.0.0 更新日誌 (Changes in V1.0.0)
* 首次正式版本發佈  
    - 使用 CLI 介面與 ANSI 轉義碼顯示 8 位元顏色  
    - 具備基礎的讀取 Record.csv 與繪圖分析功能  
> 所有更新紀錄可參閱 [CHANGELOG.md](https://github.com/CHE-72-ZStudio/Visualize-Your-Finance-Python/blob/main/CHANGELOG.md) 文件  

## V1.0.0 已知問題 (Known Issues in V1.0.0)
| 問題編號 (Issues Num) | 錯誤標題 (Issues Title) | 影響程度 (Priority) | 修復狀態 (Status) | 替代方案(Workaround) | 詳細內容 (Datails) | 
| -------------------- | ---------------------- | ----------------- | ---------------- | ------------------- | ------------- |
| *None* | 長條圖部分標籤消失 | 邊緣 (Minor) | 正在調查 (Investigating)   | 無 | 在顯示長條圖時，「交通出行」標籤會因為不明原因無法正常顯示，但不影響實際結果 |
> 如果您有發現任何其他這裡未列出的問題，歡迎向本存儲庫提出問題 (Issues) 與程式建議 (PR)  

## 未來功能 (Future Features)
| 未來版本 | 增加功能 | 開發狀態 | 優先順序 | 預定發布 |
| ------- | ------- | ------ | ------- | ------ |
| 1.1.0 | 增加可以新增 Record.csv 條目的功能 | 功能規劃 (Planning) | 高 (High) | 2025-06 |
| 1.2.0 | 增加可以寫入 Diagnose.Log 日誌檔案的功能 | 功能規劃 (Planning) | 高 (High) | 2025-07 |
| 1.3.0 | 增加更多例外情形處理  | 功能規劃 (Planning) | 高 (High) | 2025-07 |
| 1.4.0 | 開始發行 Windows 可執行檔 | 功能規劃 (Planning) | 高 (High) | 2025-08 |
| 1.4.1 | 可執行檔集成中文字體 | 功能規劃 (Planning) | 高 (High) | 2025-08 |
| 1.5.0 | 增加對 macOS 的支援 | 功能規劃 (Planning) | 中 (Medium) | 2025-12 |
| 1.5.1 | 開始發行 macOS 可執行檔 | 功能規劃 (planning) | 中 (Medium) | 2025-12 |
| 1.6.0 | 增加對 Linux 的支援 | 功能規劃 (Planning) | 中 (Medium) | 2026-?? |
| 1.6.1 | 開始發行 Linux 可執行檔 | 功能規劃 (Planning) | 中 (Medium) | 2026-?? |
| 2.0.0 | 增加跨平臺通用 GUI | 功能規劃 (Planning) | 中 (Medium) | 2026-?? |
> 實際發布時間可能會因為當下開發情形而有所提前或延後，敬請耐心等候  
> 如果您有其他的功能需求或建議，歡迎向本存儲庫提出問題 (Issues) 與程式建議 (PR)  

## 貢獻清單 (Contributors)
- @CHE72: 專案發起人／項目**主要**貢獻者／項目**主要**維護者  

## 授權許可 (License)
本專案使用 GNU General Public License v3 開源許可，詳細開源授權許可內容可參閱 [LICENSE](https://github.com/CHE-72-ZStudio/Visualize-Your-Finance-Python/blob/main/CHANGELOG.md) 文件  
> 注意：所有對此程式碼的修改與衍生版本，都必須以 GNU GPLv3 授權釋出。  

### 「帳目分析可視化程式（Python）」Ver1.0.0，著作權所有 (C) 2025-present CHE_72 ZStudio  
#### Visualize Your Finance (Python) Ver1.0.0 , Copytight (C) 2025-present CHE_72 ZStudio.  
