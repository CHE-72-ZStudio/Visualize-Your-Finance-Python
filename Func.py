"""
Func.py
此模組提供處理記帳數據的相關功能，包含：

* check_input：檢查使用者輸入是否無效或超出範圍，並回傳輸入數值或拋出對應例外
* print_list：遍歷印出列表，並顯示編號與頓號
* _sum_data：針對數據列表的特定欄位進行加總後，回傳加總後的列表
* _filter_data：根據不同的標籤需求過濾原分析數據列表並回傳
* _rank_data：根據不同的數據資料與需求筆數，對數據資料的金額進行排名並印出
* write_record：新增紀錄函數，將接收到的帳目數據儲存至 Record.csv
* pretreat：預處理函數，將讀取到的數據儲存至全域列表
* _cat_question：詢問使用者的「類別選擇平臺」，並回傳最終選擇的類別編號
* analyze：分析函數，本程式的核心分析邏輯部分
"""


import csv
import sys

from Plot import *

period_list = ["顯示使用說明", "分析所有紀錄", "特定年分的紀錄", "特定月份的紀錄", "特定日期的紀錄",
               "特定年月的紀錄", "特定月日的紀錄", "特定年日的紀錄", "特定年月日的紀錄", "返回上層選單", "結束程式運行"]  # 「時間選擇平臺」選單列表
method_list = ["顯示使用說明", "總體金額折線走勢圖", "各類金額折線走勢圖", "總體金額圓餅佔比圖", "總體次數圓餅佔比圖", "總體金額總和", "各類金額總和",
               "總體流動金額長條圖", "總體流動次數長條圖", "總體細項排名表", "各類細項排名表", "返回上層選單", "結束程式運行"]  # 「分析選擇平臺」選單列表

outcome_cat = ["交通出行", "日常飲食", "購物花費", "帳單繳費", "服務消費", "休閒娛樂", "投資理財", "旅行出遊",
               "教育學習", "居家生活", "票證加值", "社交人情", "商務往來", "醫療保健", "借錢給人", "帳戶轉帳",
               "其他支出"]  # 「類別選擇平臺｜支出」選單列表
income_cat = ["工資薪水", "副業收入", "投資利息", "發票彩券", "獎金收入", "銷售交易", "租賃收入", "折扣回饋",
              "款項退還", "零用收入", "貸款借錢", "其他收入"]  # 「類別選擇平臺｜收入」選單列表

outcome_list = list()  # 支出數據列表，用於存放從檔案中讀取到的支出數據
income_list = list()  # 收入數據列表，用於存放從檔案中讀取到的收入數據
day_list = [i for i in range(1, 32)]  # 日期列表（後續繪圖座標軸用）
month_list = [i for i in range(1, 13)]  # 月份列表（後續繪圖座標軸用）
outcome_year, income_year = list(), list()  # 支出／收入 年分列表，用於存放從檔案中讀取到的年分（後續繪圖座標軸用）


class RangeError(ValueError):
    """
    例外類別：當數值超出自訂義的合理範圍時拋出的自訂例外，繼承自內建的數值錯誤
    """
    pass


class EmptyError(TypeError):
    """
    例外類別：當要分析的數值列表為空時拋出的自訂例外，繼承自內建的類型錯誤
    """
    pass


if __name__ == "__main__":  # 如果使用者誤啟動本程式
    print("\033[38;5;197m這是 Main.py 呼叫的模組\n請改為運行 Main.py，而非直接運行本程式\n我們即將結束此模組的運行\033[0m")  # 輸出提示訊息提醒使用者正確使用方式
    exit(2)  # 呼叫系統正常結束本程式運行


def check_input(prompt, range_min=None, range_max=None):
    """
    公開函數：讀取使用者輸入的內容，轉換成整數並進行範圍驗證，在輸入無效或超出範圍時會拋出例外
    由 Gemini Code Assist 提供建議，符合 DRY 原則

    參數：
        * prompt (str)：顯示給使用者的提示訊息
        * range_min (int, optional)：範圍內允許出現的最小值
        * range_max (int, optional)：範圍內允許出現的最大值

    回傳：
        * value (int)：通過驗證的整數輸入

    拋出：
        * ValueError：如果輸入無法轉換為整數時自動拋出的內建例外
        * RangeError：如果輸入超出指定的範圍時手動拋出的自訂例外
    """
    value = int(input(prompt))  # 讀取使用者輸入後嘗試轉換成整數，若無法轉換會自動拋出 ValueError

    # 如果有傳入 最小／最大值，則檢查使用者輸入是否超出範圍，若超出範圍會手動拋出自訂的 RangeError 例外，表示數值超出合理範圍
    if range_min is not None and value < range_min:
        raise RangeError
    if range_max is not None and value > range_max:
        raise RangeError

    return value  # 回傳正確轉換成整數的數值


def print_list(content_list, offset=0):  # TODO more Pythonic?
    """
    公開函數：用於遍歷印出列表，並能顯示中文頓號與輸入用箭頭

    參數：
        * content_list (list)：要被遍歷印出的列表資料
        * offset (int, optional)：在印出數值時的偏移量，預設為 0 表示不偏移，「類別選擇平臺」為 1 以適應類別編號
    """
    for i in range(len(content_list)):
        if i == len(content_list) - 1:  # 如果是列表中的最後一項
            print("{}: {}\n".format(i + offset, content_list[i]), end='')  # 印出編號、列表文字與箭頭，準備讓使用者輸入
        else:
            print("\033[38;5;43m{}: {}".format(i + offset, content_list[i]), end='、')  # 印出編號與列表文字，以頓號分隔元素


def sum_data(original_list):
    """
    公開函數：將接收到的分析數據列表進行所有金額的加總後回傳總金額

    參數：
        * original_list (list)：要讀取後進行所有金額加總的原始分析數據列表

    回傳：
        * total (int)：按照原始項目順序加總後的列表，可作為後續顯示資產變化時使用
    """
    total = int()  # 宣告空的回傳整數
    for row in original_list:  # 對於數據列表中的每一筆帳目
        total += row[5]  # 總和變數加上此帳目的金額
    return total  # 回傳總和變數，可作為後續顯示資產變化時使用


def _sum_order_data(original_list, item_list, position):
    """
    內部函數：針對分析數據列表的特定欄位，按照項目列表的順序進行同一項目的加總後，回傳加總後符合原始項目順序的列表

    參數：
        * original_list (list)：要讀取後進行加總的原始分析數據列表
        * item_list (list)：要進行篩選後加總的項目列表，即圖表中的 X 軸
        * position (int)：該項目對應的原始分析數據欄位位置

    回傳：
        * data_list (list)：按照原始項目順序加總後的列表，可作為後續圖表繪製時使用
    """
    data_list = list()  # 宣告空的回傳列表

    # 遍歷 X 軸中的每一個 X 位置，計算對應的 Y 高度
    for item in item_list:
        total = 0  # 宣告該項目總金額的暫存總和變數
        for row in original_list:  # 對於數據列表中的每一筆帳目
            if row[position] == item:  # 如果數據列表的欄位值與現在計算項目相同
                total += row[5]  # 該項目的暫存總和變數加上此帳目的金額
        data_list.append(total)  # 將該項目的總金額加入回傳列表末尾，作為該 X 位置對應的 Y 位置

    return data_list  # 回傳按照原始項目順序加總後的列表，可作為後續圖表繪製時使用


def _filter_data(original_list, year=None, month=None, day=None, category=None, check=True):
    """
    內部函數：根據不同的標籤需求過濾原分析數據列表
    1. 過濾後的數據列表不為空或要求不進行空列表檢查時，則直接回傳過濾後的數據列表
    2. 過濾後的數據列表為空且要求進行空列表檢查時會拋出自訂例外 EmptyError
    「列表建構 List Comprehension」的邏輯由 Gemini Code Assist 提供建議

    參數：
        * original_list (list)：要進行過濾篩選的分析數據列表
        * year (int, optional)：要進行篩選的年度，若無則不進行此項篩選
        * month (int, optional)：要進行篩選的月份，若無則不進行此項篩選
        * day (int, optional)：要進行篩選的日期，若無則不進行此項篩選
        * category (int, optional)：要進行篩選的類別，若無則不進行此項篩選
        * check (bool, optional)：是否要求進行空列表檢查，若無設定則預設進行檢查

    回傳：
        * filtered_list (list)：完成篩選後的分析數據列表，可以用於繪圖或其他後續操作

    拋出：
        * EmptyError：如果要求進行空列表檢查，且要回傳的 filtered_list 列表為空時手動拋出的自訂例外
    """
    filtered_list = original_list  # 建立數據列表以進行後續篩選與回傳
    if year is not None:
        filtered_list = [row for row in filtered_list if row[2] == year]  # 僅保留符合年度要求的帳目數據
    if month is not None:
        filtered_list = [row for row in filtered_list if row[3] == month]  # 僅保留符合月份要求的帳目數據
    if day is not None:
        filtered_list = [row for row in filtered_list if row[4] == day]  # 僅保留符合日期要求的帳目數據
    if category is not None:
        filtered_list = [row for row in filtered_list if row[1] == category]  # 僅保留符合類別要求的帳目數據

    # 如果在呼叫本函數時要求檢查，則會檢查篩選完的數據列表是否為空，以避免因無法進行分析而出現空白內容
    # 若 filtered_list 為空列表，會手動拋出自訂的 EmptyError 供 analyze() 接收處理
    if check:
        if len(filtered_list == 0):
            raise EmptyError

    return filtered_list  # 回傳完成篩選後的分析數據列表


def _rank_data(original_list, analyze_cat, num):
    """
    內部函數：根據不同的數據資料與需求筆數，對數據資料的金額進行排名並印出符合需求數量的細項
    由 Gemini Code Assist 提供建議，使用「匿名函數 Lambda」的方式

    參數：
        * original_list (list)：要進行排名的分析數據列表
        * analyze_cat (list)：分析類別列表，用於在輸出排名時可以顯示，方便使用者找尋
        * num (int)：使用者要求顯示的排名數量
    """
    rank_list = sorted(original_list, key=lambda row: row[5], reverse=True)  # 依據原分析數據列表中，金額的大小順序進行排名並放入排名列表
    rank_list = rank_list[:num]  # 從排名列表中取出金額最大的前 num 名後放入排名列表
    print("\033[38;5;45m\n金額前 {} 名的紀錄如下：".format(num))  # 印出排名榜單的標題
    num = 1  # 作為稍後列印榜單時的名次
    for row in rank_list:
        output = "{}. {}-{}-{}，{}，NT${}，{}".format(num, row[2], row[3], row[4], analyze_cat[row[1] - 1], row[5], row[6])
        print(output)  # 印出名次、時間、類別、金額、詳細描述
        num += 1  # 名次遞增，前進到下一名
    print("\033[0m")  # 還原一般輸出格式，移除顏色效果，同時可以進行換行的分隔作用


def write_record(flow, reocrd_cat):
    """
    公開函數：用於 Main.py 呼叫的新增紀錄函數，會將使用者輸入的帳目數據儲存至 Record.csv，以供使用者後續分析數據使用

    參數：
        * flow (int)：要寫入的金流編號，1 表示支出，2 表示收入
        * reocrd_cat (list)：紀錄資料對應的 支出／收入 類別列表，後續以「紀錄類別列表」代稱
    """
    # 使用金流編號定義對應的金流名稱，以便顯示給使用者
    if flow == 1:
        flow_name = "支出"
    elif flow == 2:
        flow_name = "收入"
    else:
        print("\033[38;5;197m程式發生不明錯誤，無法繼續執行，正在結束程序\033[0m\a\n\n")
        sys.exit(22)  # 呼叫系統結束本程式運行，原因為"Invalid argument"

    while True:  # 無窮迴圈，在必要時使用 return 離開迴圈
        print("\033[38;5;43m這裡是「數據輸入平臺」，您正在輸入{}帳目\033[0m".format(flow_name))  # 輸出「數據輸入平臺」的提示訊息
        cat = _cat_question(reocrd_cat)  # 呼叫「類別選擇平臺」取得所需類別

        try:  # 讀取使用者輸入至 年、月、日、金額 變數，並嘗試轉換成整數後檢查輸入是否符合正常範圍
            # 呼叫 check_input() 函數讀取與檢查使用者輸入後存放至 年、月、日、金額 變數，依序傳入 詢問內容、最小數值、最大數值
            year = check_input("您想要輸入哪一年的 {} 資料？".format(reocrd_cat[cat - 1]))
            month = check_input("您想要輸入 {} 年哪一月的 {} 資料？".format(year, reocrd_cat[cat - 1]), 1, 12)
            day = check_input("您想要輸入 {} 年 {} 月哪一天的 {} 資料？".format(year, month, reocrd_cat[cat - 1]), 1, 31)
            amount = check_input("您想要輸入在 {} 年 {} 月 {} 日 {} 的金額數目是多少 NT$？".format(year, month, day, reocrd_cat[cat - 1]), 1)
            print("\033[38;5;197m您的輸入內容超出合理範圍，請檢查後輸入正確內容，現正返回「數據輸入平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
            continue  # 回到「數據輸入平臺」
        except RangeError:  # 如果使用者輸入超出正常範圍的內容
            print("\033[38;5;197m您的輸入內容超出合理範圍，請檢查後輸入正確內容，現正返回「時間選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
            continue  # 回到「時間選擇平臺」
        except ValueError:  # 如果使用者輸入無法轉換成整數的內容
            print("\033[38;5;197m您的輸入內容出現非整數的錯誤，請檢查後輸入正確選項，現正返回「時間選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
            continue  # 回到「時間選擇平臺」
        except Exception:  # 例外處理，捕捉其他未預期的錯誤
            print("\033[38;5;197m您的輸入內容出現其他錯誤，請檢查後輸入正確選項，現正返回「時間選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
            continue  # 回到「時間選擇平臺」

        item = input("您想要輸入此筆 {} NT${} 的 項目名稱／註記 為何？".format(reocrd_cat[cat - 1], amount))
        row = "{},{},{},{},{},{},{}".format(flow,cat,year,month,day,amount,item)
        print("\033[38;5;47m正在寫入 {}-{}-{} 的 {} {} NT${} 數據\033[0m".format(year, month, day, flow_name, reocrd_cat[cat - 1], amount))

        # 使用附加模式與 UTF-8 開啟 Record.csv 檔案為 record 句柄，避免覆蓋原有數據與日後無法讀取
        with open("Record.csv", "a+", encoding="UTF-8") as record:
            record.write("{}\n".format(row))

        next = input("\033[38;5;47m程式已完成該筆資料的儲存，您是否還要輸入其他筆金額數據？（輸入 Y 以繼續輸入，其他文字則會返回「功能選擇平臺」）")
        match next:
            case "y" | "Y":
                print("\033[38;5;43m正在返回「數據輸入平臺」以繼續輸入下一筆數據\033[0m\a\n")  # 輸出提示訊息與通知聲音
                continue  # 回到「數據輸入平臺」
            case _:
                print("\033[38;5;43m正在返回「功能選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音
                return  # 回到「功能選擇平臺」


def pretreat():
    """
    公開函數：用於 Main.py 呼叫的預處理函數，會將讀取到的數據儲存至全域列表以供後續分析數據使用
    預處理內容包含：開啟與讀取 Record.csv、儲存到 支出／收入 數據列表、提示錯誤訊息、轉換數據型態和製造 支出／收入 年分列表
    """
    # 嘗試開啟 Record.csv 檔案為 record 句柄，否則輸出錯誤訊息並直接結束程式（因為缺少該檔案，程式後續無法執行）
    try:
        # 由 Gemini Code Assist 提供建議，調整開啟檔案的邏輯，避免發生其他異常時未能正確關閉文件
        with open("Record.csv", "r", newline="", encoding="UTF-8") as record:
            rows_iterator = csv.reader(record)  # 使用 csv.reader 讀取 record 數據並儲存到迭代器
            outcome_read, income_read = list(), list()  # 收集從 CSV 讀取的原始數據的臨時列表
            row_num = 0  # 現在的讀取橫列號，方便進行錯誤訊息輸出
            error_rows = list()  # 出錯橫列號列表，存放讀取時無法進行轉換的橫列號

            # 存取迭代器內的數據串列，並嘗試放到支出／收入 數據列表
            for r in rows_iterator:
                row_num += 1  # 讀取橫列號增加 1，對應到現在正在讀取的實際列號
                # 由 Gemini Code Assist 提供建議，跳過空列以避免後續進行數據轉換時的 IndexError
                if not r:
                    error_rows.append(row_num)
                    continue

                if r[0] == "1":  # 如果開頭為 "1"，表示這是一筆支出的數據
                    outcome_read.append(r)  # 將其附加至支出數據列表，方便後續存取
                elif r[0] == "2":  # 如果開頭為 "2"，表示這是一筆收入的數據
                    income_read.append(r)  # 將其附加至收入數據列表，方便後續存取
                else:  # 否則，此檔案內容應有誤
                    error_rows.append(row_num)  # 將錯誤列號存放到出錯橫列號列表
    # TODO: 修改為 FileNotFouneError 時自動建立 Record.csv 檔案並提示使用者利用程式功能新增帳目數據至 Record.csv 中
    # TODO: 只有 Exception 這種完全無法處理的問題的時候才使用以下這種 sys.exit(2) 的方法
    except FileNotFoundError:
        print("\033[38;5;197m開啟 \"Record.csv\" 時出現錯誤，請檢查資料夾內是否包含此檔案")
        print("請確保 \"Record.csv\" 與本程式元件放在同一資料夾下，以利程式正確讀取記帳檔案")
        print("\n程序運行出現無法繼續與修正的錯誤，正在結束程序\033[0m\a\n\n")
        sys.exit(2)
    except Exception:
        print("\033[38;5;197m開啟 \"Record.csv\" 時出現不明原因的錯誤")
        print("\n程序運行出現無法繼續與修正的錯誤，正在結束程序\033[0m\a\n\n")
        sys.exit(2)

    # 如果出錯橫列號列表不為空，則輸出包含所有出錯橫列編號的錯誤訊息
    if error_rows:
        print("\033[38;5;208m讀取 \"Record.csv\" 時，在以下這些橫列 ", end="")
        print(", ".join(str(row) for row in error_rows), end="")  # 由 GitHub Copilot 提供建議，使用「列表建構 List Comprehension」的邏輯
        print(" 中發現異常\n程式將忽略這些無法讀取的資料，請檢查您的檔案是否完全符合格式要求\033[0m")

    # 在 支出／收入 數據列表中，嘗試將每一筆數據的 類別、年份、月份、日期、金額 欄位轉換成整數型態
    # 如果缺少 類別、年份、月份、日期、金額 任一欄位，該筆數據將會被程式捨棄，以避免因轉換出錯而意外終止程式運行（缺少項目名稱欄位是可以被允許的）
    # 如果出現無法轉換成整數的項目數據，該筆數據將會被程式捨棄，以避免因轉換出錯而意外終止程式運行
    # 如果在 類別、月份、日期、金額 欄位出現超出合理範圍的內容，該筆數據將會被程式捨棄，以避免圖表與排名顯示異常
    # 由 Gemini Code Assist 提供建議，不要在 for 迴圈進行的同時移除原列表的元素（避免潛在出錯的可能）
    # Gemini 建議改為使用 outcome_read/income_read 作為暫存列表，將通過檢查的帳目數據添加至 outcome_list/income_list

    type_error = 0  # 缺少重要欄位的帳目數量，方便進行錯誤訊息輸出
    int_error = 0  # 無法正確轉換成整數的帳目數量，方便進行錯誤訊息輸出
    range_error = 0  # 整數欄位內容不合理的帳目數量，方便進行錯誤訊息輸出

    global income_year, outcome_year  # 確保能夠正確讀取與修改全域列表
    # TODO: 2 for-loop do not fit DRY principle, need to implement a function to replace them by asking Gemini
    for outcome in outcome_read:
        try:
            if len(outcome) < 6:  # 欄位數量的檢查，避免在轉換為整數時出現 IndexError
                raise TypeError  # 使用內建的例外，表示欄位缺少（資料類型與預期不同）
            if len(outcome) < 7:  # 由 Gemini Code Assist 提供建議，避免某些數據缺少項目欄位會導致輸出排名時出錯
                outcome.append("")  # 加入空字串作為該筆數據的項目欄位
            for p in range(1, 6):
                outcome[p] = int(outcome[p])
            if not (1 <= outcome[1] <= len(outcome_cat)):  # 類別欄位對應的檢查
                raise RangeError  # 拋出自訂的 RangeError 例外，表示數值超出合理範圍
            if not (1 <= outcome[3] <= 12):  # 月份欄位對應的檢查
                raise RangeError  # 拋出自訂的 RangeError 例外，表示數值超出合理範圍
            if not (1 <= outcome[4] <= 31):  # 日期欄位對應的檢查
                raise RangeError  # 拋出自訂的 RangeError 例外，表示數值超出合理範圍
            if outcome[5] <= 0:  # 金額欄位對應的檢查，分析時沒必要存放不為正的金額
                raise RangeError  # 拋出自訂的 RangeError 例外，表示數值超出合理範圍
        except RangeError:  # 如果使用者輸入超出正常範圍的內容
            range_error += 1
        except ValueError:  # 如果欄位中的內容無法正確轉換成整數
            int_error += 1
        except TypeError:  # 如果帳目數據缺少必要欄位
            type_error += 1
        else:  # 否則將完成轉換的正常數據加至支出數據列表
            outcome_list.append(outcome)
    for income in income_read:
        try:
            if len(income) < 6:  # 欄位數量的檢查，避免在轉換為整數時出現 IndexError
                raise TypeError  # 使用內建的例外，表示欄位缺少（資料類型與預期不同）
            if len(income) < 7:  # 由 Gemini Code Assist 提供建議，避免某些數據缺少項目欄位會導致輸出排名時出錯
                income.append("")  # 加入空字串作為該筆數據的項目欄位
            for p in range(1, 6):
                income[p] = int(income[p])
            if not (1 <= income[1] <= len(income_cat)):  # 類別欄位對應的檢查
                raise RangeError  # 使用自訂的例外，表示數值超出合理範圍
            if not (1 <= income[3] <= 12):  # 月份欄位對應的檢查
                raise RangeError  # 使用自訂的例外，表示數值超出合理範圍
            if not (1 <= income[4] <= 31):  # 日期欄位對應的檢查
                raise RangeError  # 使用自訂的例外，表示數值超出合理範圍
            if income[5] <= 0:  # 金額欄位對應的檢查，分析時沒必要存放不為正的金額
                raise RangeError  # 使用自訂的例外，表示數值超出合理範圍
        except RangeError:  # 如果使用者輸入超出正常範圍的內容
            range_error += 1
        except ValueError:  # 如果欄位中的內容無法正確轉換成整數
            int_error += 1
        except TypeError:  # 如果帳目數據缺少必要欄位
            type_error += 1
        else:  # 否則將完成轉換的正常數據加至收入數據列表
            income_list.append(income)
    # 如果出錯帳目數量不為 0，則輸出包含出錯帳目數量的錯誤訊息
    if type_error:
        print("\033[38;5;208m有 {} 筆數據缺少 類別、年份、月份、日期、金額 欄位，無法正確讀取與轉換".format(type_error))
    if int_error:
        print("\033[38;5;208m有 {} 筆數據的 類別、年份、月份、日期、金額 欄位，無法正確轉換成整數型態".format(int_error))
    if range_error:
        print("\033[38;5;208m有 {} 筆數據的 類別、月份、日期、金額 欄位，數值內容超出合理範圍".format(range_error))
    if type_error + int_error + range_error:
        print("程式將忽略這些異常的資料，請檢查您的檔案是否完全符合格式要求\033[0m")

    year_set = set()  # 製造一個集合，利用集合會自動去除重複元素的特性

    # 讀取 支出／收入 數據列表中，數據的年份欄位並放入集合中，在轉換成串列後放到對應的年份列表並進行排序，作為後續繪圖座標軸用
    for row in outcome_list:
        year_set.add(row[2])
    global outcome_year  # 使用全域列表
    outcome_year = list(year_set)
    outcome_year.sort()
    year_set.clear()  # 清空年份集合
    for row in income_list:
        year_set.add(row[2])
    global income_year  # 使用全域列表
    income_year = list(year_set)
    income_year.sort()

    print("\033[38;5;47m程式已完成從 \"Record.csv\" 中提取數據\033[0m")  # 輸出提示訊息，讓使用者得知程式運行進度


def _cat_question(cat_list):
    """
    內部函數：用於詢問使用者特定類別的「類別選擇平臺」，並回傳最終選擇的類別編號

    參數：
        * cat_list (list)：要讓使用者選擇的分析類別列表

    回傳：
        * cat (int)：使用者最終選擇的類別編號，作為後續篩選數據列表時使用
    """
    flag, cat = True, -1  # 定義循環標籤與回傳值變數

    # 使用無窮迴圈，直到用戶輸入正確才能離開迴圈
    while flag:
        print("這裡是「類別選擇平臺」，請選擇您想使用的帳目分類")  # 輸出「類別選擇平臺」的提示訊息
        print_list(cat_list, 1)  # 呼叫列表印出函式，印出「類別選擇平臺」的選單列表

        try:
            # 呼叫 check_input() 函數讀取與檢查使用者輸入後存放至時間變數，依序傳入 詢問內容、最小數值、最大數值
            # 讀取使用者輸入至類別變數，並嘗試轉換成整數後檢查輸入是否符合正常範圍
            # 使用 except 接收自 check_input() 函數傳遞來的拋出例外並進行處理
            cat = check_input("--> \033[0m", 1, len(cat_list))
        except RangeError:  # 如果使用者輸入超出正常範圍的內容
            print("\033[38;5;197m您的輸入內容超出正常範圍，請檢查後輸入正確選項，現正返回「類別選擇平臺」\033[0m\a\n")  # 輸出提示訊息，讓使用者重新輸入
            continue  # 回到迴圈的開頭，繼續重新輸入
        except ValueError:  # 如果使用者輸入無法轉換成整數的內容
            print("\033[38;5;197m您的輸入內容出現非整數的錯誤，請檢查後輸入正確選項，現正返回「類別選擇平臺」\033[0m\a\n")  # 輸出提示訊息，讓使用者重新輸入
            continue  # 回到迴圈的開頭，繼續重新輸入
        except Exception:
            print("\033[38;5;197m您的輸入內容出現其他錯誤，請檢查後輸入正確選項，現正返回「類別選擇平臺」\033[0m\a\n")  # 輸出提示訊息，讓使用者重新輸入
            continue  # 回到迴圈的開頭，繼續重新輸入
        else:
            flag = False  # 結束無窮迴圈的運行

    return cat  # 回傳類別編號，作為後續篩選數據列表時使用


def analyze(analyze_flow, analyze_list, analyze_cat, analyze_year, analyze_num):
    """
    公開函數：用於 Main.py 呼叫的分析函數，也是本程式的核心分析邏輯部分
    內含「時間選擇平臺」與「分析選擇平臺」，並在必要時呼叫「類別選擇平臺」函數，在完成資料整理後在必要時會呼叫 Plot.py 中的函數進行圖表繪製

    參數：
        * analyze_flow (str)：要分析的 支出／收入 金流名稱，後續以「分析金流名稱」代稱
        * analyze_list (list)：要分析的 支出／收入 數據列表，後續以「分析數據列表」代稱
        * analyze_cat (list)：要分析的 支出／收入 類別列表，後續以「分析類別列表」代稱
        * analyze_year (list)：要分析的 支出／收入 年分列表，後續以「分析年分列表」代稱
        * analyze_num (list)：要分析的 支出／收入 類別對應編號列表，後續以「分析編號列表」代稱
    """
    if len(analyze_list) == 0:  # 如果傳入的分析數據列表為空，則無法分析，需要停止操作並返回「功能選擇平臺」
        print("\033[38;5;208m數據集當中沒有任何資料，無法進行分析，現正返回「功能選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
        return  # 回到「功能選擇平臺」

    while True:  # 無窮迴圈，在必要時使用 return 離開迴圈
        temp_list = analyze_list  # 定義暫存數據列表，避免更改原始分析數據列表
        line_list, line_axis, line_name = list(), list(), list()  # 預先定義後續圖表使用的列表為空列表，包含 Y 軸數值、X 軸間距、X 軸標籤

        try:  # 由 Gemini Code Assist 提供建議，在主迴圈中捕捉例外與處理錯誤後，讓迴圈繼續迭代，符合 DRY 原則與提高可讀性
            print("\n這裡是「時間選擇平臺」，請選擇您想分析的時間段")  # 輸出「時間選擇平臺」的提示訊息
            print_list(period_list)  # 呼叫列表印出函式，印出「時間選擇平臺」的選單列表
            period = check_input("--> \033[0m", 0, len(period_list) - 1)  # 呼叫 check_input() 函數讀取與檢查使用者輸入後存放至時間變數，依序傳入 詢問內容、最小數值、最大數值
            match period:
                case 0:  # 時間0：顯示使用說明
                    print(period_manual)  # 印出「時間選擇平臺」的對應說明文件
                    continue  # 回到「時間選擇平臺」
                case 1:  # 時間1：分析所有紀錄
                    line_list = _sum_order_data(temp_list, analyze_year, 2)  # 以年為單位先進行暫存數據列表的加總後，存入後續圖表使用的 Y 軸數值列表
                    line_axis, line_name = analyze_year, analyze_year  # X 軸間距列表與 X 軸標籤列表定義為分析年份列表
                case 2:  # 時間2：特定年分的紀錄
                    year = check_input("您想要分析哪一年的數據資料？")  # 呼叫 check_input() 函數檢查使用者輸入後存放至 年 變數，傳入詢問內容
                    temp_list = _filter_data(temp_list, year=year)  # 以所需 年 變數過濾暫存數據列表

                    line_list = _sum_order_data(temp_list, month_list, 3)  # 以月為單位先進行暫存數據列表的加總後，存入後續圖表使用的 Y 軸數值列表
                    line_axis, line_name = month_list, month_list  # X 軸間距列表與 X 軸標籤列表定義為分析月份列表
                case 3:  # 時間3：特定月份的紀錄
                    month = check_input("您想要分析每年的哪一月的數據資料？", 1, 12)  # 呼叫 check_input() 函數檢查使用者輸入後存放至 月 變數，依序傳入 詢問內容、最小數值、最大數值
                    temp_list = _filter_data(analyze_list, month=month)  # 以所需 月 變數過濾暫存數據列表

                    line_list = _sum_order_data(temp_list, analyze_year, 2)  # 以年為單位先進行暫存數據列表的加總後，存入後續圖表使用的 Y 軸數值列表
                    line_axis, line_name = analyze_year, analyze_year  # X 軸間距列表與 X 軸標籤列表定義為分析年份列表
                case 4:  # 時間4：特定日期的紀錄
                    day = check_input("您想要分析每年每月哪一天的數據資料？", 1, 31)  # 呼叫 check_input() 函數檢查使用者輸入後存放至 日 變數，依序傳入 詢問內容、最小數值、最大數值
                    temp_list = _filter_data(analyze_list, day=day)  # 以所需 日 變數過濾暫存數據列表

                    # 遍歷給定時間段的所有年月，按照順序將相同年月的數據進行加總後存入後續圖表使用的 Y 軸數值列表，同時創造依照順序排列的 X 軸標籤列表
                    for y in range(analyze_year[0], analyze_year[-1] + 1):  # 改為使用 range 的方式，避免漏掉某些年份而導致顯示圖表異常
                        for m in month_list:
                            temp = 0  # 宣告該年月總金額的暫存總和變數
                            for_list = _filter_data(temp_list, year=y, month=m, check=False)  # 以所需 年、月 變數過濾暫存數據列表，存入遍歷年月的專用列表，並且不要做空列表檢查
                            for row in for_list:  # 對於符合目前遍歷進度的數據
                                temp += row[5]  # 該時間段的暫存總和變數加上此筆帳目的金額
                            line_name.append("{}-{}".format(y, m))  # 將該時間段的名稱加入 X 軸標籤列表的末尾
                            line_list.append(temp)  # 將該時間段的暫存總和加入 Y 軸數值列表的末尾
                case 5:  # 時間5：特定年月的紀錄
                    # 呼叫 check_input() 函數讀取與檢查使用者輸入後存放至 年、月 變數，依序傳入 詢問內容、最小數值、最大數值
                    year = check_input("您想要分析哪一年的數據資料？")
                    month = check_input("您想要分析 {} 年哪一月的數據資料？".format(year), 1, 12)
                    temp_list = _filter_data(temp_list, year=year, month=month)  # 以所需 年、月 變數過濾暫存數據列表

                    line_list = _sum_order_data(temp_list, day_list, 4)  # 以日為單位先進行暫存數據列表的加總後，存入後續圖表使用的 Y 軸數值列表
                    line_axis, line_name = day_list, day_list  # X 軸間距列表與 X 軸標籤列表定義為分析日期列表
                case 6:  # 時間6：特定月日的紀錄
                    # 呼叫 check_input() 函數讀取與檢查使用者輸入後存放至 月、日 變數，依序傳入 詢問內容、最小數值、最大數值
                    month = check_input("您想要分析每年哪一月的數據資料？", 1, 12)
                    day = check_input("您想要分析每年 {} 月哪一天的數據資料？".format(month), 1, 31)
                    temp_list = _filter_data(analyze_list, month=month, day=day)  # 以所需 月、日 變數過濾暫存數據列表

                    line_list = _sum_order_data(temp_list, analyze_year, 2)  # 以年為單位先進行暫存數據列表的加總後，存入後續圖表使用的 Y 軸數值列表
                    line_axis, line_name = analyze_year, analyze_year  # X 軸間距列表與 X 軸標籤列表定義為分析年份列表
                case 7:  # 時間7：特定年日的紀錄
                    # 呼叫 check_input() 函數讀取與檢查使用者輸入後存放至 年、日 變數，依序傳入 詢問內容、最小數值、最大數值
                    year = check_input("您想要分析哪一年的數據資料？")
                    day = check_input("您想要分析 {} 年哪一天的數據資料？".format(year), 1, 31)
                    temp_list = _filter_data(analyze_list, year=year, day=day)  # 以所需 年、日 變數過濾暫存數據列表

                    line_list = _sum_order_data(temp_list, month_list, 3)  # 以月為單位先進行暫存數據列表的加總後，存入後續圖表使用的 Y 軸數值列表
                    line_axis, line_name = month_list, month_list  # X 軸間距列表與 X 軸標籤列表定義為分析月份列表
                case 8:  # 時間8：特定年月日的紀錄
                    # 呼叫 check_input() 函數讀取與檢查使用者輸入後存放至 年、月、日 變數，依序傳入 詢問內容、最小數值、最大數值
                    year = check_input("您想要分析哪一年的數據資料？")
                    month = check_input("您想要分析 {} 年哪一月的數據資料？".format(year), 1, 12)
                    day = check_input("您想要分析 {} 年 {} 月哪一天的數據資料？".format(year, month), 1, 31)
                    temp_list = _filter_data(analyze_list, year=year, month=month, day=day)  # 以所需 年、月、日 變數過濾暫存數據列表
                case 9:  # 時間9：返回上層選單
                    print("\033[38;5;43m正在返回「功能選擇平臺」\033[0m\n\a")  # 輸出提示訊息與通知聲音
                    return  # 回到「功能選擇平臺」
                case 10:  # 時間10：結束程式運行
                    print("\n\033[38;5;197m收到您的要求，正在結束程序\033[0m\a\n")  # 輸出提示訊息與通知聲音
                    sys.exit(0)  # 呼叫系統正常結束本程式運行
                case _:  # 其他錯誤的時間選擇輸入，應該不會走到這裡 #TODO Delete this after check
                    print("\033[38;5;197m您的輸入內容出現錯誤，請檢查後輸入正確選項，現正返回「時間選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
                    continue  # 回到「時間選擇平臺」

            print("這裡是「分析選擇平臺」，您希望用什麼圖表分析")  # 輸出提示訊息
            print_list(method_list)  # 呼叫列表印出函式，印出「分析選擇平臺」的選單列表
            method =  check_input("--> \033[0m", 0, len(method_list) - 1)  # 呼叫 check_input() 函數讀取與檢查使用者輸入後存放至分析變數，依序傳入 詢問內容、最小數值、最大數值

            match method:  # TODO 確認 3,4 是否與 7,8 合併成 subplot
                case 0:  # 分析0：顯示使用說明
                    print(method_manual)  # 印出「分析選擇平臺」的使用說明
                case 1:  # 分析1：總體金額折線走勢圖
                    if period == 8:  # 無法分析特定年月日的紀錄（只有一天，沒有時間變化與趨勢可言）
                        print("\033[38;5;208m特定年月日的紀錄（只有一天）無法進行折線圖分析，現正返回「時間選擇平臺」\a\n")  # 輸出提示訊息
                        continue  # 回到「時間選擇平臺」
                    else:
                        axis_line(line_list, line_name)  # 呼叫 Plot.py 中的 axis_line() 函數繪製折線圖，依序傳入 Y 軸數值、X 軸間距、X 軸標籤列表
                case 2:  # 分析2：各類金額折線走勢圖
                    if period == 8:  # 無法分析特定年月日的紀錄（只有一天，沒有時間變化與趨勢可言）
                        print("\033[38;5;208m特定年月日的紀錄（只有一天）無法進行折線圖分析，現正返回「時間選擇平臺」\a\n")  # 輸出提示訊息
                        continue  # 回到「時間選擇平臺」
                    cat = _cat_question(analyze_cat)  # 呼叫「類別選擇平臺」取得所需類別
                    temp_list = _filter_data(temp_list, category=cat)  # 以所需類別變數過濾暫存數據列表
                case 3:  # 分析3：總體金額圓餅佔比圖
                    temp_list = _sum_order_data(temp_list, analyze_num, 1)  # 以類別為單位先進行暫存數據列表的加總後，存回暫存數據列表作為後續圖表使用
                    axis_pie(temp_list, analyze_cat)  # 呼叫 Plot.py 中的 axis_pie() 函數繪製圓餅圖，依序傳入圓餅圖數值列表、分析類別列表（作為標籤）
                case 4:  # 分析4：總體次數圓餅佔比圖
                    pie_list = list()  # 預先定義後續圓餅圖使用的數值列表為空列表
                    # 遍歷所有類別，按照類別順序計算該類別的出現次數後存入圓餅圖數值列表
                    for c in analyze_num:
                        temp = 0  # 宣告該類別總次數的暫存總和變數
                        for data in temp_list:
                            if data[1] == c:  # 對於符合目前遍歷類別的數據
                                temp += 1
                        pie_list.append(temp)  # 將該類別的暫存總和加入圓餅圖數值列表的末尾
                    axis_pie(pie_list, analyze_cat)  # 呼叫 Plot.py 中的 axis_pie() 函數繪製圓餅圖，依序傳入圓餅圖數值列表、分析類別列表（標籤）
                case 5:  # 分析5：總體金額總和
                    total = sum_data(temp_list)  #呼叫 sum_data() 函數計算給定期間的總流動金額
                    print("您在這段期間的 {} 金額總和為 NT${:,}".format(analyze_flow, total))  # 以分隔符方式輸出計算結果，使用到 分析金流名稱 參數
                case 6:  # 分析6：各類金額總和
                    cat = _cat_question(analyze_cat)  # 呼叫「類別選擇平臺」取得所需類別
                    temp_list = _filter_data(temp_list, category=cat)  # 以所需類別變數過濾暫存數據列表
                    total = sum_data(temp_list)  #呼叫 sum_data() 函數計算給定期間與類別的總流動金額
                    print("您在這段期間的 {} 金額總和為 NT${:,}".format(analyze_flow, total))  # 以分隔符方式輸出計算結果，使用到 分析金流名稱 參數
                case 7:  # 分析7：總體流動金額長條圖
                    temp_list = _sum_order_data(temp_list, analyze_num, 1)  # 以類別為單位先進行暫存數據列表的加總後，存回暫存數據列表作為後續圖表使用
                    axis_bar(temp_list, analyze_cat)  # 呼叫 Plot.py 中的 axis_bar() 函數繪製長條圖，依序傳入暫存數據列表、分析編號列表（間距）、分析類別列表（標籤）
                case 8:  # 分析8：總體流動次數長條圖
                    bar_list = list()  # 預先定義後續長條圖使用的數值列表為空列表
                    # 遍歷所有類別，按照類別順序計算該類別的出現次數後存入長條圖數值列表
                    for c in analyze_num:
                        temp = 0  # 宣告該類別總次數的暫存總和變數
                        for data in temp_list:
                            if c == data[1]:  # 對於符合目前遍歷類別的數據
                                temp += 1
                        bar_list.append(temp)  # 將該類別的暫存總和加入長條圖數值列表的末尾
                    axis_bar(bar_list, analyze_cat)  # 呼叫 Plot.py 中的 axis_bar() 函數繪製長條圖，依序傳入暫存數據列表、分析編號列表（間距）、分析類別列表（標籤）
                case 9:  # 分析9：總體細項排名表
                    #_check_list(temp_list)  # 這裡不再做暫存數據列表是否為空的檢查，因為如果暫存數據列表為空就會在前面出現 EmptyError 例外
                    rank = check_input("您想比較前幾筆資料？", 1)  # 呼叫 check_input() 函數讀取與檢查使用者輸入，依序傳入 詢問內容、最小數值
                    _rank_data(temp_list, analyze_cat, rank)  # 呼叫 _rank_data() 函數進行排名顯示，依序傳入暫存數據列表、分析類別列表、排名顯示數量
                case 10:  # 分析10：各類細項排名表
                    cat = _cat_question(analyze_cat)  # 呼叫「類別選擇平臺」取得所需類別
                    temp_list = _filter_data(temp_list, category=cat)  # 以所需類別變數過濾暫存數據列表
                    rank = check_input("您想比較前幾筆資料？", 1)  # 呼叫 check_input() 函數讀取與檢查使用者輸入，依序傳入 詢問內容、最小數值
                    _rank_data(temp_list, analyze_cat, rank)  # 呼叫 _rank_data() 函數進行排名顯示，依序傳入暫存數據列表、分析類別列表、排名顯示數量
                case 11:  # 分析11：返回上層選單
                    print("\033[38;5;43m正在返回「時間選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音
                    continue  # 回到「時間選擇平臺」
                case 12:  # 分析12：結束程式運行
                    print("\n\033[38;5;197m收到您的要求，正在結束程序\033[0m\a\n")  # 輸出提示訊息與通知聲音
                    sys.exit(0)  # 呼叫系統正常結束本程式運行
                case _:  # 其他錯誤的分析選擇輸入，應該不會走到這裡 #TODO Delete this after check
                    print("\033[38;5;197m您的輸入內容出現錯誤，請檢查後輸入正確選項，現正返回「時間選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
                    continue  # 回到「時間選擇平臺」

            # 若要分析各類折線走勢圖，須要重新進行各時間段 Y 軸數值的計算
            # TODO: here can be more pythonic by asking Google Gemini Code Assist
            match (period, method):
                case (1, 2):
                    line_list = _sum_order_data(temp_list, analyze_year, 2)  # 以年為單位先進行暫存數據列表的加總後，存入後續圖表使用的 Y 軸數值列表
                    axis_line(line_list, line_name)  # 呼叫 Plot.py 中的 axis_line() 函數繪製折線圖，依序傳入 Y 軸數值、X 軸間距、X 軸標籤列表
                case (2, 2):
                    line_list = _sum_order_data(temp_list, month_list, 3)  # 以月為單位先進行暫存數據列表的加總後，存入後續圖表使用的 Y 軸數值列表
                    axis_line(line_list, line_name)  # 呼叫 Plot.py 中的 axis_line() 函數繪製折線圖，依序傳入 Y 軸數值、X 軸間距、X 軸標籤列表
                case (3, 2):
                    line_list = _sum_order_data(temp_list, analyze_year, 2)  # 以年為單位先進行暫存數據列表的加總後，存入後續圖表使用的 Y 軸數值列表
                    axis_line(line_list, line_name)  # 呼叫 Plot.py 中的 axis_line() 函數繪製折線圖，依序傳入 Y 軸數值、X 軸間距、X 軸標籤列表
                case (4, 2):
                    line_list = list()  # 重新定義 Y 軸數值為空列表
                    # 遍歷給定時間段的所有年月，按照順序將相同年月的數據進行加總後存入後續圖表使用的 Y 軸數值列表，同時創造依照順序排列的 X 軸標籤列表
                    for y in analyze_year:
                        for m in month_list:
                            temp = 0  # 宣告該年月總金額的暫存總和變數
                            for_list = _filter_data(temp_list, year=y, month=m, check=False)  # 以所需 年、月 變數過濾暫存數據列表，存入遍歷年月的專用列表，並且不要做空列表檢查
                            for row in for_list:  # 對於符合目前遍歷進度的數據
                                temp += row[5]  # 該時間段的暫存總和變數加上此筆帳目的金額
                            line_list.append(temp)  # 將該時間段的暫存總和加入 Y 軸數值列表的末尾（不須再重複製造 X 軸間距與 X 軸標籤列表）
                    axis_line(line_list, line_name)  # 呼叫 Plot.py 中的 axis_line() 函數繪製折線圖，依序傳入 Y 軸數值、X 軸間距、X 軸標籤列表
                case (5, 2):
                    line_list = _sum_order_data(temp_list, day_list, 4)  # 以日為單位先進行暫存數據列表的加總後，存入後續圖表使用的 Y 軸數值列表
                    axis_line(line_list, line_name)  # 呼叫 Plot.py 中的 axis_line() 函數繪製折線圖，依序傳入 Y 軸數值、X 軸間距、X 軸標籤列表
                case (6, 2):
                    line_list = _sum_order_data(temp_list, analyze_year, 2)  # 以年為單位先進行暫存數據列表的加總後，存入後續圖表使用的 Y 軸數值列表
                    axis_line(line_list, line_name)  # 呼叫 Plot.py 中的 axis_line() 函數繪製折線圖，依序傳入 Y 軸數值、X 軸間距、X 軸標籤列表
                # 由於其他輸入錯誤的情形已在前面進行檢測與排除，此處不再放置其他判斷條件
                # case (_, _):

            print("\033[38;5;47m操作成功運行完成，正在返回「時間選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音
            continue  # 回到時間選擇平台

        except RangeError:  # 如果使用者輸入超出正常範圍的內容
            print("\033[38;5;197m您的輸入內容超出合理範圍，請檢查後輸入正確內容，現正返回「時間選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
            continue  # 回到「時間選擇平臺」
        except EmptyError:  # 如果經過篩選後的數據列表為空
            print("\033[38;5;208m數據集當中沒有符合您輸入條件的資料，無法進行分析，現正返回「時間選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
            continue  # 回到「時間選擇平臺」
        except ValueError:  # 如果使用者輸入無法轉換成整數的內容
            print("\033[38;5;197m您的輸入內容出現非整數的錯誤，請檢查後輸入正確選項，現正返回「時間選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
            continue  # 回到「時間選擇平臺」
        except Exception:  # 例外處理，捕捉其他未預期的錯誤
            print("\033[38;5;197m您的輸入內容出現其他錯誤，請檢查後輸入正確選項，現正返回「時間選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
            continue  # 回到「時間選擇平臺」


period_manual = ("\033[38;5;208m\n「時間選擇平臺」使用說明\n0 顯示本則使用說明\t1 分析記帳檔案中的所有紀錄\n"
                 "2 選定特定年度（如2025年），分析當年度所有紀錄\t3 選定特定月份（如10月），分析該月份的所有紀錄\t4 選定特定日期（如1日），分析該日期的所有紀錄\n"
                 "5 選定特定年月（如2025年10月）進行分析\t6 選定特定月日（如10月1日）進行分析\t7 選定特定年日（如2025年所有1日）進行分析\t8 選定特定年月日（如2025年10月1日）進行分析\n"
                 "9 返回「功能選擇平臺」\t10 結束運行並退出程式\n\033[0m")  # 「時間選擇平臺」使用說明
method_manual = ("\033[38;5;208m\n「分析選擇平臺」使用說明\n0 顯示本則使用說明\t1 使用折線圖分析隨時間變化的總體金額\t2 使用折線圖分析特定類別隨時間變化的金額\n"
                 "3 使用圓餅圖分析不同類別的金額比例\t4 使用圓餅圖分析不同類別的出現次數比例\t5 顯示在給定區間內的總金額\t6 顯示在給定區間中特定類別的總金額\n"
                 "7 使用長條圖顯示不同類別的總金額\t8 使用長條圖顯示不同類別的出現總次數\t9 使用排名顯示總體紀錄中金額最高的項目\t10 使用排名顯示特定類別中金額最高的項目\n"
                 "11 返回「時間選擇平臺」\t12 結束運行並退出程式\n\033[0m")  # 「分析選擇平臺」使用說明
