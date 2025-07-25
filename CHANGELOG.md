# 「帳目分析可視化程式（Python）」的變更日誌
## Change Log for Visualize Your Finance (Python)

## V1.3.12 (2025-07-25) 新增分析方式與顯示效果再進化
### 新增功能 Added
- 在 `Func.py` 中新增「總體次數折線走勢圖」、「各類次數折線走勢圖」、「總體金額／次數表格」的分析方式，使分析更為快速全面
- 現在如果程式在資料夾下找不到 `Record.csv` 檔案，則會自動創建一個空白檔案，並提示用戶使用程式內建功能進行帳目數據的寫入，避免因缺少該檔案而無法運行
- 在 `Main.py` 中使用「顯示目前資產」功能時，現在除了會顯示 支出／收入 總金額，也會額外顯示 支出／收入 總筆數
### 功能修復 Fixed
- 修復了在「新增支出／收入紀錄」功能中，會出現異常的「您的輸入內容出現其他錯誤」錯誤，導致無法正常使用功能的問題
- 修復了在「數據輸入平臺」功能中，部分文字輸出內容出現邏輯不一致、存在前後矛盾的問題
### 功能更改 Changed
- 合併並升級後的「總體金額／次數表格」已經取代了 `Func.py` 中原本的「總體金額總和」與「各類金額總和」分析功能
- 由於增加與合併分析選擇平臺中的方式，調整部分「分析選擇平臺」的功能編號
### 提升進步 Improved
- 更新並優化 `Func.py` 中對於「分析選擇平臺」的使用說明，使其更為精準
- 優化 `Func.py` 中「細項排名表」的顯示方式，如果經過篩選後的細項數量比預期數量少，則顯示實際數量作為排名榜單的標題
- 優化圖表的顯示顏色，現在在顯示折線圖與長條圖時，圖表區的背景會呈現白煙色，而中央的圖表內容會維持白色，增加圖表可視度
- 優化圓餅圖的顯示效果，現在類別標籤與比例數值離圓心更遠，可以避免文字擠在一起，導致難以辨識的問題
- 優化程式中的 金額／排名 數字顯示效果，現在會自動顯示 `,` 分隔符，方便檢視與數值判讀
### 文檔更新 Edited
- 更新 `USER.md` 以符合最新新增與調整的程式功能，並調整部分描述的用字遣詞，使其更為精準
### 貢獻清單 Contributor
- [![CHE72](https://img.shields.io/badge/CHE72-181717.svg?logo=github&logoColor=white)](https://github.com/CHE72): 專案發起人／項目**唯一**貢獻者／項目**唯一**維護者

## V1.2.12 (2025-06-15) 修復顯示錯誤與優化圖表樣式
### 新增功能 Added
- 在「分析選擇平臺」新增可以顯示不同時間段與不同類別的 支出／收入 金額總和
### 功能修復 Fixed
- 修復了「類別選擇平臺」中的選單數字顯示錯誤的問題，現在類別編號可以正常從 1 開始顯示
- 修復了在「時間選擇平臺」選擇「時間4：特定日期的紀錄」時，會因為運行多餘的檢查而出現異常的「沒有符合條件的資料」錯誤，導致無法正常進行分析的問題
### 提升進步 Improved
- 顯示折線圖的時候，現在除了線條變得更明顯外，也在各個數值點上顯示點形標記，增加可閱讀性
- 顯示折線圖的時候，現在會在每個數值點的右上方顯示其對應的金額數值內容，更為方便查看存取
- 顯示長條圖的時候，現在會一併顯示背景格線，讓 金額／次數 對照更容易
- 顯示長條圖的時候，現在會依照順序輪換顏色，更容易分辨不同的類別
- 顯示長條圖的時候，現在會在每個長條的上方顯示其對應的 金額／次數 數值內容，更為方便查看存取
- 顯示圓餅圖的時候，現在會忽略那些 0 元／次 的數值內容與類別標籤，避免因冗餘的重疊內容影響視覺與數據判讀
### 已經移除 Removed
- 移除與 `LICENSE` 內容重複的 `License_EN.txt`，現在 `Main.py` 輸出英文原版的開源許可時會直接讀取原始的 `LICENSE`
- 將 `License_ZH.txt` 重新命名為 `LICENSE_ZH`，維持文件命名邏輯的一致性，現在 `Main.py` 輸出中文翻譯的開源許可時會讀取 `LICENSE_ZH`
### 文檔更新 Edited
- 更新 `USER.md` 以符合最新新增與調整的程式功能
- 在 `DEVELOPER.md` 中新增「5. 專案結構」區塊，方便開發者快速上手本程式架構與各個檔案用途
### 貢獻清單 Contributor
- [![CHE72](https://img.shields.io/badge/CHE72-181717.svg?logo=github&logoColor=white)](https://github.com/CHE72): 專案發起人／項目**唯一**貢獻者／項目**唯一**維護者

## V1.1.20 (2025-06-12) 大幅提升程式的健壯性與修復大量潛在的錯誤
### 功能修復 Fixed
- 修復了當 `Record.csv` 的 類別、年份、月份、日期、金額 欄位有缺失時，可能會導致程式意外結束的問題
    - 現在程式會忽略這些欄位缺少的資料，並提示使用者注意格式要求
- 修復了當 `Record.csv` 的 類別、年份、月份、日期、金額 欄位無法正常轉換成整數型態時，可能會導致程式意外結束的問題
    - 現在程式會忽略這些無法轉換的資料，並提示使用者注意格式要求
- 修復了當 `Record.csv` 的 類別、月份、日期、金額 欄位超出合理範圍時，程式依然儲存這些錯誤數據的問題
    - 現在程式會忽略這些超出範圍的資料，並提示使用者注意數據範圍
- 修復了當 `Record.csv` 出現空行時，程式依然儲存這些空行，可能會導致程式意外結束的問題
    - 現在程式不會儲存這些無意義的空行，並提示使用者注意格式要求
- 修復了當進行排名時，輸入非自然數的內容依然會錯誤呼叫排名函數，導致顯示空排名表的問題
    - 現在程式不會儲存這些無意義的排名，並提示使用者注意輸入數值範圍
- 修復了在顯示長條圖時，「交通出行 / 工資薪水」標籤會消失的問題
- 修復了若 `Record.csv` 缺少項目欄位，在顯示排名表時，可能會導致程式意外結束的問題
    - 現在程式會自動使用空字串做為這些帳目數據的項目欄位
- 新上市了一批小彩蛋，等待您來尋寶
### 提升進步 Improved
- 優化 `Record.csv` 的開啟邏輯，避免無法正確關閉文件的特殊情形
- 優化輸入範圍出錯時的輸出提示，現在可以明確區分超出範圍、不為整數與其他類型的錯誤
- 優化在分析特定日期時的趨勢折線圖顯示方式，現在不會跳過中間沒有資料的年份以確保圖表容易解讀
- 優化在處理 `Record.csv` 時，出錯訊息的輸出格式與內容，使其更為清晰
- 優化折線圖時間標籤的顯示方式，現在會在標籤數量較多時旋轉標籤，增加可視度
- 優化選單列表印出與讀取用戶輸入的方式，現在整體內容更為清晰易懂
- 透過程式中部份區域的重構與語句順序的調整，使程式符合 DRY 原則、提升可讀性與更為 Pythonic
### 貢獻清單 Contributor
- [![CHE72](https://img.shields.io/badge/CHE72-181717.svg?logo=github&logoColor=white)](https://github.com/CHE72): 專案發起人／項目**唯一**貢獻者／項目**唯一**維護者

## V1.1.5 (2025-06-10) 具備新增帳目的功能
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

## V1.0.11 (2025-06-08) 修復 UTF-8 錯誤與提升使用者體驗
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

## V1.0.0 (2025-05-29) 首次正式版本發佈
### 首次正式版本發佈 First Release
- 使用 CLI 介面與 ANSI 轉義碼顯示 8 位元顏色
- 具備基礎的讀取 `Record.csv` 與繪圖分析功能
### 棄用淘汰 Deprecated
- `MakeRecord.py` 檔案為用於產生虛擬的帳目資料供繳交作業時使用，將於下次小版本更新時移除該檔案
### 貢獻清單 Contributor
- [![CHE72](https://img.shields.io/badge/CHE72-181717.svg?logo=github&logoColor=white)](https://github.com/CHE72): 專案發起人／項目**唯一**貢獻者／項目**唯一**維護者

### 帳目分析可視化程式（Python），著作權所有 (C) 2025-現在 CHE_72 ZStudio
#### Visualize Your Finance (Python) , Copyright (C) 2025-present CHE_72 ZStudio.
