"""
MakeRecord.py
此模組提供創造虛擬記帳資料的功能
"""

import random
import math

times = 0  # 虛擬帳目筆數，用於控制產生的虛擬帳目數量
Flag = True  # 控制迴圈的旗標

while Flag:  # 旗標控制的無窮迴圈
    times = int(input("輸入要創造的帳目數量 "))  # 詢問創造虛擬帳目筆數
    if times > 0:  # 如果輸入內容大於 0
        Flag = False  # 更改旗標，脫離迴圈
    else:  # 其他情形
        print("數量輸入錯誤，請重新輸入")  # 提示用戶重新輸入

with open("Record.csv", "w+", encoding = "UTF-8") as record:  # 用覆蓋書寫的方式開啟 "Record.csv"
    for i in range(times):  # 製造模擬支出數據
        bit = 1  # 表示此為支出金流
        category = random.randint(1, 17)  # 隨機選擇一個支出類別
        year = random.randint(2020, 2025)  # 隨機選擇一個年份
        month = random.randint(1, 12)  # 隨機選擇一個月份
        day = random.randint(1, 28)  # 隨機選擇一個日期
        money = random.randint(100, 5000)  # 隨機選擇一個整數金額
        row = "{},{},{},{},{},{},TEST_OUT_{}\n".format(bit, category, year,month, day, money, i + 1)  # 將產生的數據以符合 .CSV 格式的方式儲存
        record.write(row)  # 將儲存的字串寫入 "Record.csv" 檔案
    for i in range(math.ceil(0.1 * times)):  # 製造模擬收入數據
        bit = 2  # 表示此為收入金流
        category = random.randint(1, 12)  # 隨機選擇一個收入類別
        year = random.randint(2020, 2025)  # 隨機選擇一個年份
        month = random.randint(1, 12)  # 隨機選擇一個月份
        day = random.randint(1, 28)  # 隨機選擇一個日期
        money = random.randint(200, 3000)  # 隨機選擇一個整數金額
        row = "{},{},{},{},{},{},TEST_IN_{}\n".format(bit, category, year, month, day, money, i + 1)  # 將產生的數據以符合 .CSV 格式的方式儲存
        record.write(row)  # 將儲存的字串寫入 "Record.csv" 檔案

print("創造完成")  # 輸出提示訊息，供使用者得知現在進度
