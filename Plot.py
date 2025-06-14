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

plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]  # 修改為中文字體 微軟正黑體，避免預設字體的中文字顯示問題  #TODO 修改為隨程式分發的鴻蒙黑體，增進跨系統能力

def axis_line(y_list, x_name):
    """
    用於繪製隨時間變化的折線圖函數

    參數：
        * y_list (list)：要繪製的數據資料
        * x_name (list)：要繪製的時間刻度座標（可能為 年、月、日、年-月 的組合）
    """
    # TODO: 是否要在數據點上方顯示金額或次數值，並且過多的數據點要旋轉、跳躍、閉著眼？
    plt.plot(x_name, y_list, marker=".", lw=1.5)  # 使用時間標籤與數據資料，並調整線寬與標記樣式，提升可閱讀性
    plt.xticks(x_name)  # 定義繪圖間隔

    if len(x_name) > 12:  # 由 Gemini Code Assist 提供建議，將標籤進行旋轉避免重疊
        plt.xticks(rotation=72, ha="right")

    plt.grid(color='gray', ls=":", lw=1, alpha=0.5)  # 增加格線，方便對照 y 軸與檢視
    plt.show()  # 顯示圖表


def axis_bar(y_list, x_name):
    """
    用於繪製不同類別的長條圖函數

    參數：
        * y_list (list)：要繪製的數據資料
        * x_name (list)：要繪製的類別刻度
    """
    color_list = ["m", "r", "y", "g", "c", "b"]  # 設定長條顏色依序為 洋紅、紅、黃、綠、青、藍 6 色列表
    # 使用類別標籤與數據資料，增加 6 色循環顯示與 y 高度數值顯示
    plt.bar_label(plt.bar(x_name, y_list, color=color_list), y_list)
    # 等效於以下內容
    # bar_container = plt.bar(x_name, y_list, color=color_list)
    # plt.bar_label(bar_container, color=color_list)

    plt.grid(color='gray', ls=":", lw=1, alpha=0.5)  # 增加格線，方便對照 y 軸與檢視
    plt.show()  # 顯示圖表


def axis_pie(y_list, x_name):  # 定義 圓餅圖 函數
    """
    用於繪製不同類別的圓餅圖函數

    參數：
        * y_list (list)：要繪製的數據資料
        * x_name (list)：要繪製的類別刻度
    """
    # TODO: 能夠隱藏結果為 0.00% 的數值內容與類別標籤（現行解決方案不夠完美，僅能隱藏 0 元的類別標籤，但是仍然無法完全隱藏 0.00% 的數值內容）
    # 移除金額或次數為 0 的數值內容與類別標籤，避免在顯示圓餅圖時出現重疊，影響數據判讀
    filtered_list, filtered_name = list(), list()

    for i in range(len(y_list)):
        if y_list[i] != 0:
            filtered_list.append(y_list[i])
            filtered_name.append(x_name[i])

    plt.pie(filtered_list, labels=filtered_name, autopct="%2.1f%%")  # 使用過濾後的類別標籤與數據資料比例
    plt.show()  # 顯示圖表
