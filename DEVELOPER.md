# 「帳目分析可視化程式（Python）」的開發手冊
## Developer Manual for Visualize Your Finance (Python)

## 0. 目錄

1. [環境需求](#1-環境需求-environment-requirements)
2. [安裝配置](#2-安裝配置-installation--configuration)
3. [基本使用](#3-基本使用-basic-usage)
4. [檔案規範](#4-檔案規範-file-specifications)
5. [專案結構](#5-專案結構-project-structure)

---

## 1. 環境需求 Environment Requirements
- **作業系統**：
    - Microsoft Windows 10+
    - Apple macOS
    - Linux
- **依賴套件**：
    - Python 3.10+（支援 match...case... 語法）  
    - 支援 ANSI 轉義碼與中文字體顯示的終端輸出程式（ANSI 轉義碼用於 8 位元顏色顯示）  
    - 本專案的 Python 模組需求已在 `Requirements.txt` 文件中列出。您可以使用 pip 安裝所有模組依賴： `pip install -r Requirements.txt`  

## 2. 安裝配置 Installation & Configuration
1. 從 GitHub 上的 [Releases](https://github.com/CHE-72-ZStudio/Visualize-Your-Finance-Python/releases) 頁面下載本程式檔案的壓縮檔 `Source Code`，解壓縮後放置於適當的位置  
2. 依據下方的「4. 檔案規範/`Record.csv`」區塊新增或修改 `Record.csv` 後使用 UTF-8 編碼存檔，使其符合您的真實帳目內容  
     > 您也可以選擇直接透過本程式新增條目，而不用手動修改 `Record.csv`  
3. 確認您的 `Record.csv` 檔案與解壓縮後的 `Main.py` 檔案放置於同一文件夾路徑下，並且此文件夾同時包含程式運行時的其他必備檔案  
4. 請確認您的電腦中已安裝 Python (>=3.10)，若是尚未安裝，可至 [Download Python](https://www.python.org/downloads/) 網頁下載安裝適合您作業系統的 Python 版本  
    > （若您已安裝完成合乎此程式要求的 Python 版本，可忽略這步驟）  
5. 在此文件夾路徑下開啟終端輸出程式，輸入 `pip install -r Requirements.txt`  
    >（若您已安裝完成此程式的必備模組依賴項，可忽略這步驟）  
6. 在同一終端窗口中輸入 `python Main.py` 以執行 `Main.py`  
7. 程式在輸出必要資訊後會進入「功能選擇平臺」，依據您所想要使用的功能輸入功能對應的半形數字後按下 `Enter/Return` 按鍵  

## 3. 基本使用 Basic Usage
請參照 [USER.md](https://github.com/CHE-72-ZStudio/Visualize-Your-Finance-Python/blob/main/USER.md) 文件中的第 3 章

## 4. 檔案規範 File Specifications
### 4.1 Record.csv
每一橫列都代表一筆數據，橫列的格式如下：  
`金流編號,類別編號,年,月,日,金額,項目名稱`  
1. 這邊僅能使用英文半形逗號 `,` 作為分隔符，並且文字與逗號之間沒有任何空格    
2. 本程式的 `Record.csv` 採用 UTF-8 編碼開啟，請在存檔時確認您使用的正確的編碼格式，避免程式無法解碼數據檔案而出現錯誤  
> `Example.csv` 為供您參考用的範例數據檔案，您可參考其格式後完成 `Record.csv` 的輸入  

#### 4.1.1 金流編號
使用 1 位正整數表示的金流，如 `1`；禁止參雜其他文字，如 `1 支出`、`支出` 等非數字的文字  

| 金流編號 | 金流類別 |
|------|------|
| 1    | 支出   |
| 2    | 收入   |

#### 4.1.2 類別編號
使用 1-2 位正整數表示的月份，如 `2`；禁止參雜其他文字，如 `2 收入 副業收入`、`2 副業收入`、`副業收入` 等非數字的文字  

| 類別編號 | 支出類別 | 收入類別   |
|------|------|--------|
| 1    | 交通出行 | 工資薪水   |
| 2    | 日常飲食 | 副業收入   |
| 3    | 購物花費 | 投資利息   |
| 4    | 帳單繳費 | 發票彩券   |
| 5    | 服務消費 | 獎金收入   |
| 6    | 休閒娛樂 | 銷售交易   |
| 7    | 投資理財 | 租賃收入   |
| 8    | 旅行出遊 | 折扣回饋   |
| 9    | 教育學習 | 款項退還   |
| 10   | 居家生活 | 零用收入   |
| 11   | 票證加值 | 貸款借錢   |
| 12   | 社交人情 | 其他收入   |
| 13   | 商務往來 |
| 14   | 醫療保健 |
| 15   | 借錢給人 |
| 16   | 帳戶轉帳 |
| 17   | 其他支出 |

### 4.1.3 年
使用 4 位正整數表示的西元年，如 `2025`；禁止參雜其他文字，如 `'25`、`2025年`、`二〇二五年` 等非數字的文字  

### 4.1.4 月
使用 1-2 位正整數表示的月份，如 `10`；禁止參雜其他文字，如 `10月`、`十月`、`Oct.`、`October` 等非數字的文字  

### 4.1.5 日
使用 1-2 位正整數表示的日期，如 `1`；禁止參雜其他文字，如 `1日`、`一日`、`1st`、`First` 等非數字的文字  

### 4.1.6 金額
使用正整數表示的金額，如 `6000`；暫時不支援小數金額；禁止參雜其他文字，如 `-6000`、`陸仟圓`、`$6000`、`-NT$6000` 等非數字的文字  

### 4.1.7 項目名稱
建議使用您方便辨識與記憶的項目名稱，如 `Apple MacBook Pro 13" (Intel 2020)` 等您認為清晰易懂、有助於您回想的項目名稱；盡量避免含糊不清的敘述內容，如 `其中一台筆電`、`另一台筆電` 
> 由於 `Record.csv` 為逗號分隔檔案，故避免在項目名稱欄位中輸入英文逗號 `,`，否則可能出現項目名稱無法完整顯示的情形  


## 5. 專案結構 Project Structure
- `Main.py`：本程式的唯一入口，處理「功能選擇平臺」邏輯與程式初始化
- `Func.py`：本程式的分析運行核心，處理記帳數據的相關功能，如數據讀取、預處理、分析計算、使用者輸入驗證、檔案寫入等
- `Plot.py`：使用 Matplotlib.PyPlot 模組繪製圖表，並處理圖表相關的樣式設定
- `Studio.py`：存放簡短開源資訊與工作室 ASCII 藝術宣告
- `Record.csv`：使用者帳目數據檔案，其格式需嚴格遵守本文件的[規範](#41-recordcsv)
- `HarmonyOS_Sans_TC_Medium.ttf`：圖表顯示所使用的自訂繁體中文字型檔案，增強跨系統顯示能力
    > 在圖表中使用繁體中文字型檔案功能上尚未完成實作，敬請期待  
    > 開發進度可以參閱[README.md](https://github.com/CHE-72-ZStudio/Visualize-Your-Finance-Python/blob/main/README.md)中的「未來功能」區塊，也歡迎您向本存儲庫提交程式建議 (PR)  


### 帳目分析可視化程式（Python），著作權所有 (C) 2025-現在 CHE_72 ZStudio
#### Visualize Your Finance (Python), Copytight (C) 2025-present CHE_72 ZStudio.