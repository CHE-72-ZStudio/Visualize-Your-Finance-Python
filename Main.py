"""
Main.py
此模組為「帳目分析可視化程式」的唯一入口
"""

import sys

import Func
from Studio import *

if __name__ == "__main__":
    # 定義 中／英 程式名稱、程式版本號，如果日後有需要更新時，更改此處即可避免缺失遺漏
    program_zh = "帳目分析可視化程式（Python）"
    program_en = "Visualize Your Finance (Python)"
    version = "1.3.12"

    print("歡迎您使用「{}」Ver{}，本程式由 CHE_72 ZStudio 製作".format(program_zh, version))  # 輸出中文程式名稱、程式版本號、工作室名稱
    print("\033[38;5;208m本程式可用來協助您分析 \"Record.csv\" 中的記帳數據，並使用圖形化的分析顯示結果。\033[0m")  # 輸出中文程式目的
    Func.pretreat()  # 呼叫預處理函式，嘗試讀取 Record.csv 中的記帳數據後進行數據整理，最後放置於列表中
    print("\033[38;5;208m以下所有問題請依照提示輸入「半形阿拉伯數字」回答\033[0m\n")  # 輸出中文使用提示，避免使用者誤用全形數字或中文數字

    func_list = ["顯示使用說明", "分析支出數據", "分析收入數據", "顯示目前資產", "新增支出紀錄", "新增收入紀錄", "顯示開源許可（英文原版）", "顯示開源許可（中文翻譯）", "顯示作者宣告", "結束程式運行"]  # 「功能選擇平臺」選單列表
    func_manual = ("\033[38;5;208m\n「功能選擇平臺」使用說明\t0 顯示本則使用說明\t1 分析記帳檔案中的支出紀錄\t2 分析記帳檔案中的收入紀錄\n"
                   "3 依據現有記帳資料的總收入與總支出，計算結餘後的淨資產\t4 在 \"Record.csv\" 中新增支出紀錄\t5 在 \"Record.csv\" 中新增收入紀錄\t\n"
                   "6 顯示英文原版的 GNU GPLv3 開源授權許可（具有法律效力）\t7 顯示中文翻譯的 GNU GPLv3 開源授權許可（僅供理解參考）\n"
                   "8 顯示工作室名稱與程式版權宣告\t9 結束運行並退出程式\n\033[0m")  # 「功能選擇平臺」使用說明

    while True:  # 無窮迴圈，在必要時使用 sys.exit() 結束程式運行
        print("這裡是「功能選擇平臺」，請選擇您要使用的功能")  # 輸出「功能選擇平臺」的提示訊息
        Func.print_list(func_list)  # 呼叫列表印出函式，印出「功能選擇平臺」的選單列表
        func = -1  # 「功能選擇平臺」的功能變數

        try:  # 呼叫 Func.check_input() 函數讀取與檢查使用者輸入後存放至功能變數，依序傳入 詢問內容、最小數值、最大數值
            func = Func.check_input("--> \033[0m", 0, 10)
        except Func.RangeError:  # 如果使用者輸入超出正常範圍的內容
            print("\033[38;5;197m您的輸入內容超出合理範圍，請檢查後輸入正確內容，現正返回「功能選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
            continue  # 回到「功能選擇平臺」
        except ValueError:  # 如果使用者輸入無法轉換成整數的內容
            print("\033[38;5;197m您的輸入內容出現錯誤，請檢查後輸入正確選項，現正返回「功能選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
            continue  # 返回「功能選擇平臺」
        except Exception:  # 例外處理，捕捉其他未預期的錯誤
            print("\033[38;5;197m您的輸入內容出現其他錯誤，請檢查後輸入正確選項，現正返回「功能選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
            continue  # 回到「功能選擇平臺」
        else:
            match func:  # 根據功能變數判斷，切換不同功能
                case 0:  # 功能0：顯示使用說明
                    print(func_manual)  # 輸出「功能選擇平臺」簡易使用說明
                case 1:  # 功能1：分析支出數據
                    # 呼叫 Func.py 中的 analyze() 函數進行互動分析，依序傳入 支出金流名稱、支出數據列表、支出類別列表、支出年份列表與支出類別對應編號列表
                    Func.analyze("支出", Func.outcome_list, Func.outcome_cat, Func.outcome_year, range(1, len(Func.outcome_cat) + 1))
                case 2:  # 功能2：分析收入數據
                    # 呼叫 Func.py 中的 analyze() 函數進行互動分析，依序傳入 收入金流名稱、收入數據列表、收入類別列表、收入年份列表與收入類別對應編號列表
                    Func.analyze("收入", Func.income_list, Func.income_cat, Func.income_year, range(1, len(Func.income_cat) + 1))
                case 3:  # 功能3：顯示目前資產
                    # 呼叫 Func.py 中的 sum_all_data() 函數進行數據列表的 金額／次數 加總，取得 支出／收入 對應的 金額／次數 的總和，並計算淨資產總額
                    outcome_amount = Func.sum_all_amount(Func.outcome_list)
                    income_amount = Func.sum_all_amount(Func.income_list)
                    outcome_times = len(Func.outcome_list)
                    income_times = len(Func.income_list)
                    final_total = income_amount - outcome_amount

                    # 以分隔符方式輸出計算結果
                    print("在您的所有紀錄中：")
                    print("總支出為 NT${:,}（共{:,}筆）、總收入為 NT${:,}（共{:,}筆）".format(outcome_amount, outcome_times, income_amount, income_times))
                    print("目前淨資產為 NT${:,}".format(final_total))

                    # 如果淨資產為特定數字內容，則輸出祝福消息做為彩蛋
                    if final_total < 0:
                        print("\033[38;5;201m祝福您天天發發發，早日發大財\033[0m")
                    elif final_total == 1:
                        print("\033[38;5;201m一元復始，萬象更新\033[0m")
                case 4:  # 功能4：新增支出紀錄
                    # 呼叫 Func.py 中的 write_record() 函數進行新增紀錄，依序傳入 支出金流編號、支出類別列表
                    Func.write_record(1, Func.outcome_cat)
                    # 需要清空數據列表後重新呼叫預處理函式，讀取更新過的記帳數據並進行數據整理，最後放置於列表中完成數據列表的更新
                    Func.outcome_list, Func.income_list = [], []
                    Func.pretreat()
                case 5:  # 功能5：新增收入紀錄
                    # 呼叫 Func.py 中的 write_record() 函數進行新增紀錄，依序傳入 收入金流編號、收入類別列表
                    Func.write_record(2, Func.income_cat)
                    # 需要清空數據列表後重新呼叫預處理函式，讀取更新過的記帳數據並進行數據整理，最後放置於列表中完成數據列表的更新
                    Func.outcome_list, Func.income_list = [], []
                    Func.pretreat()
                case 6:  # 功能6：顯示開源許可（英文原版）
                    # 嘗試開啟 LICENSE 檔案為 gpl 句柄，否則輸出錯誤訊息並取消印出開源許可
                    try:
                        with open("LICENSE", "r", encoding="UTF-8") as gpl:
                            for line in gpl:
                                print(line, end="")
                    except FileNotFoundError:
                        print("\033[38;5;197m開啟 \"LICENSE\" 時出現錯誤，請檢查資料夾內是否包含此檔案")
                case 7:  # 功能7：顯示開源許可（中文翻譯）
                    # 嘗試開啟 LICENSE_ZH 檔案為 gpl 句柄，否則輸出錯誤訊息並取消印出開源許可
                    try:
                        with open("LICENSE_ZH", "r", encoding="UTF-8") as gpl:
                            for line in gpl:
                                print(line, end="")
                    except FileNotFoundError:
                        print("\033[38;5;197m開啟 \"LICENSE_ZH\" 時出現錯誤，請檢查資料夾內是否包含此檔案")
                case 8:  # 功能8：顯示作者宣告
                    print("「{}」 Ver{}，著作權所有 (C) 2025-現在 CHE_72 ZStudio".format(program_zh, version))
                    print("{} Ver{} , Copyright (C) 2025-present CHE_72 ZStudio".format(program_en, version))
                    print(Studio_ZH)  # Studio.py 中的中文版工作室宣告
                case 9:  # 功能9：結束程式運行
                    print("\n\033[38;5;197m收到您的要求，正在結束程序\033[0m\a\n")  # 輸出提示訊息與通知聲音
                    sys.exit(0)  # 呼叫系統正常結束本程式運行
                case 10:  # 功能10：隱藏的小彩蛋
                    print("\033[38;5;201m恭喜您找到隱藏的小彩蛋，祝福您的生活十全十美\033[0m")
                case _:  # 其他錯誤的功能選擇輸入，應該不會走到這裡 # TODO Delete this after check
                    print("\033[38;5;197m您的輸入內容出現錯誤，請檢查後重新輸入，現正返回「功能選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
else:  # 如果使用者誤將本程式作為模組引用
    print("\033[38;5;197m本程式為「帳目分析可視化程式」的主入口\n請直接運行 Main.py，而非透過其他模組引入本程式\033[0m\a\n")  # 輸出提示訊息提醒使用者正確使用方式
    sys.exit(1)  # 呼叫系統結束本程式運行，原因為"Operation not permitted"
