"""
Main.py
此模組為「帳目分析可視化程式」的唯一入口
"""

import sys

import Func
from Studio import *

"""
優化方向：調整程式功能列表與輸入程式碼為一層選單：
0-顯示使用說明、1-分析支出圖表、2-分析收入圖表、3-新增支出紀錄、4-新增收入紀錄、5-顯示目前資產、6-顯示開源許可（英文原版）、7-顯示開源許可（中文翻譯）、8-顯示作者宣告、9-結束程式運行
"""

if __name__ == "__main__":
    # 定義 中／英 程式名稱、程式版本號，如果日後有需要更新時，更改此處即可避免缺失遺漏
    program_zh = "帳目分析可視化程式（Python）"
    program_en = "Visualize Your Finance (Python)"
    version = "1.0.0"

    print("歡迎您使用「{}」 Ver{}，本程式由 CHE_72 ZStudio 製作".format(program_zh, version))  # 輸出中文程式名稱、程式版本號、工作室名稱
    print("\033[38;5;208m本程式可用來協助您分析 \"Record.csv\" 中的記帳數據，並使用圖形化的分析顯示結果。\033[0m")  # 輸出中文程式目的
    Func.pretreat()  # 呼叫預處理函式，嘗試讀取 Record.csv 中的記帳數據後進行數據整理，最後放置於列表中
    print("\033[38;5;208m以下所有問題請依照提示輸入「半形阿拉伯數字」回答\033[0m\n")  # 輸出中文使用提示，避免使用者誤用全形數字或中文數字

    func_list = ["顯示使用說明", "分析支出數據", "分析收入數據", "顯示目前資產", "顯示開源許可（英文原版）", "顯示開源許可（中文翻譯）", "顯示作者宣告", "結束程式運行"]  # 「功能選擇平臺」選單列表
    func_manual = ("\033[38;5;208m\n「功能選擇平臺」使用說明\t0 顯示本則使用說明\n"
                   "1 分析記帳檔案中的支出紀錄\t2 分析記帳檔案中的收入紀錄\t3 依據現有記帳資料的總收入與總支出，計算結餘後的淨資產\n"
                   "4 顯示英文原版的 GNU GPLv3 開源授權許可（具有法律效力）\t5 顯示中文翻譯的 GNU GPLv3 開源授權許可（僅供理解參考）\n"
                   "6 顯示工作室名稱與程式版權宣告\t7 結束運行並退出程式\n\033[0m")  # 「功能選擇平臺」使用說明

    while True:  # 無窮迴圈，在必要時使用 sys.exit() 結束程式運行
        print("這裡是「功能選擇平臺」，請選擇您要使用的功能")  # 輸出「功能選擇平臺」的提示訊息
        Func.print_list(func_list)  # 呼叫列表印出函式，印出「功能選擇平臺」的選單列表
        func = -1  # 「功能選擇平臺」的功能變數

        try:  # 讀取使用者輸入至時間變數，並嘗試轉換成整數
            func = int(input())
        except ValueError:  # 如果使用者輸入無法轉換成整數的內容
            print("\033[38;5;197m您的輸入內容出現錯誤，請檢查後輸入正確選項，現正返回「功能選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
            continue  # 返回「功能選擇平臺」
        else:
            match func:  # 根據功能變數判斷，切換不同功能
                case 0:  # 功能0：顯示使用說明
                    print(func_manual)  # 輸出「功能選擇平臺」簡易使用說明
                case 1:  # 功能1：分析支出數據
                    # 呼叫 Func.py 中的 analyze() 函數進行互動分析，依序傳入 支出數據列表、支出類別列表、支出年份列表與支出類別對應編號列表
                    Func.analyze(Func.outcome_list, Func.outcome_cat, Func.outcome_year, range(1, len(Func.outcome_cat) + 1))
                case 2:  # 功能2：分析收入數據
                    # 呼叫 Func.py 中的 analyze() 函數進行互動分析，依序傳入 收入數據列表、收入類別列表、收入年份列表與收入類別對應編號列表
                    Func.analyze(Func.income_list, Func.income_cat, Func.income_year, range(1, len(Func.income_cat) + 1))
                case 3:  # 功能3：顯示目前資產
                    # 遍歷 支出／收入 數據列表的金額部分，計算 支出／收入 金額的總和
                    outcome_total, income_total = 0, 0
                    for row in Func.outcome_list:
                        outcome_total += row[5]
                    for row in Func.income_list:
                        income_total += row[5]
                    final_total = income_total - outcome_total

                    # 輸出計算結果  # TODO:嘗試改為增加分隔位顯示的金額，較為方便閱讀判斷
                    print("在您的所有紀錄中：")
                    print("總支出為 NT${}，總收入為 NT${}".format(outcome_total, income_total))
                    print("目前淨資產為 NT${}".format(final_total))

                    # 如果淨資產為負數，則輸出祝福消息做為彩蛋
                    if final_total < 0:
                        print("祝福您天天發發發，早日發大財")
                case 4:  # 功能4：顯示開源許可（英文原版）
                    # 嘗試開啟 License_EN.txt 檔案為 gpl 句柄，否則輸出錯誤訊息並取消印出開源許可
                    try:
                        with open("License_EN.txt", "r", encoding="UTF-8") as gpl:
                            for line in gpl:
                                print(line, end="")
                    except FileNotFoundError:
                        print("\033[38;5;197m開啟 \"License_EN.txt\" 時出現錯誤，請檢查資料夾內是否包含此檔案")
                case 5:  # 功能5：顯示開源許可（中文翻譯）
                    # 嘗試開啟 License_ZH.txt 檔案為 gpl 句柄，否則輸出錯誤訊息並取消印出開源許可
                    try:
                        with open("License_ZH.txt", "r", encoding="UTF-8") as gpl:
                            for line in gpl:
                                print(line, end="")
                    except FileNotFoundError:
                        print("\033[38;5;197m開啟 \"License_ZH.txt\" 時出現錯誤，請檢查資料夾內是否包含此檔案")
                case 6:  # 功能6：顯示作者宣告
                    print("「{}」 Ver{}，著作權所有 (C) 2025-現在 CHE_72 ZStudio".format(program_zh, version))
                    print("{} Ver{} , Copyright (C) 2025-present CHE_72 ZStudio".format(program_en, version))
                    print(Studio_ZH)  # Studio.py 中的中文版工作室宣告
                case 7:  # 功能7：結束程式運行
                    print("\n\033[38;5;197m收到您的要求，正在結束程序\033[0m\a\n")  # 輸出提示訊息與通知聲音
                    sys.exit(0)  # 呼叫系統正常結束本程式運行
                case _:  # 其他錯誤的功能選擇輸入
                    print("\033[38;5;197m您的輸入內容出現錯誤，請檢查後重新輸入，現正返回「功能選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
else:  # 如果使用者誤將本程式作為模組引用
    print("\033[38;5;197m本程式為「帳目分析可視化程式」的主入口\n請直接運行 Main.py，而非透過其他模組引入本程式\033[0m\a\n")  # 輸出提示訊息提醒使用者正確使用方式
    sys.exit(0)  # 呼叫系統正常結束本程式運行