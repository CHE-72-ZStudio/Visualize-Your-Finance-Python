"""
Plot.py
此模組提供繪製各種常見圖表的功能，包含：

* axis_line：繪製隨時間變化的折線圖函數
* axis_bar：繪製不同類別的長條圖函數
* axis_pie：繪製不同類別的圓餅圖函數
"""

import matplotlib.pyplot as plt

if __name__ == "__main__":  # 如果使用者誤啟動本程式
    print("\033[38;5;197m這是 Func.py 呼叫的模組\n請改為運行 Main.py，而非直接運行本程式\n我們即將結束此模組的運行\033[0m")  # 輸出提示訊息提醒使用者正確使用方式
    exit(2)  # 呼叫系統正常結束本程式運行


def axis_line(y_list, x_range, x_name):
    """
    用於繪製隨時間變化的折線圖函數

    參數：
        * y_list (list)：要繪製的數據資料
        * x_range (list)：確保繪圖間隔符合預期
        * x_name (list)：要繪製的時間刻度
    """
    plt.plot(x_name, y_list)  # 顯示時間標籤與數據資料
    plt.xticks(x_range)  # 定義繪圖間隔
    plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]  # 修改為中文字體 微軟正黑體，避免預設字體的中文字顯示問題
    plt.grid(color='gray', ls=":", lw=1, alpha=0.5)  # 增加格線，方便檢視
    plt.show()  # 顯示圖表


def axis_bar(y_list, x_range, x_name):
    """
    用於繪製不同類別的長條圖函數

    參數：
        * y_list (list)：要繪製的數據資料
        * x_range (list)：確保繪圖間隔符合預期
        * x_name (list)：要繪製的類別刻度
    """
    plt.bar(x_name, y_list)  # 顯示類別標籤與數據資料
    plt.xticks(x_range)  # 定義繪圖間隔
    plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]  # 修改為中文字體 微軟正黑體，避免預設字體的中文字顯示問題
    plt.show()  # 顯示圖表


def axis_pie(y_list, x_name):  # 定義 圓餅圖 函數
    """
    用於繪製不同類別的圓餅圖函數

    參數：
        * y_list (list)：要繪製的數據資料
        * x_name (list)：要繪製的類別刻度
    """
    plt.pie(y_list, labels=x_name, autopct="%2.1f%%")  # 顯示類別標籤與數據資料比例
    plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]  # 修改為中文字體 微軟正黑體，避免預設字體的中文字顯示問題
    plt.show()  # 顯示圖表
