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
    exit(1)  # 呼叫系統結束本程式運行，原因為"Operation not permitted"

plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]  # 修改為中文字體 微軟正黑體，避免預設字體的中文字顯示問題  #TODO 修改為隨程式分發的鴻蒙黑體，增進跨系統能力

def axis_line(y1_list, y2_list, x_name):
    """
    用於繪製隨時間變化的折線圖函數

    參數：
        * y1_list (list)：要繪製的數據資料 1，對應到左側座標軸
        * y2_list (list)：要繪製的數據資料 2，對應到右側座標軸（仍在測試階段，目前尚未啟用）Axes.twinx()
        * x_name (list)：要繪製的時間刻度座標（可能為 年、月、日、年-月 的組合）
    """
    plt.figure(facecolor="whitesmoke")  # 設定圖表區的背景色為白煙色，增加圖表可視度
    plt.plot(x_name, y1_list, marker=".", lw=1.5)  # 使用時間標籤與數據資料，並調整線寬與標記樣式，提升可閱讀性

    # 將 x_name 傳入 plt.xticks() 中，避免 X 軸座標刻度出現小數或其他非預期出現的刻度
    # 由 Gemini Code Assist 提供旋轉的參數設定，自主修改為三元運算子，將 X 軸座標刻度進行旋轉避免重疊
    plt.xticks(
        x_name,
        rotation = 72 if len(x_name) > 12 else 0
    )
    # TODO: 改為以下這樣是否會較好？
    # plt.xticks(
    #     range(len(x_name)),
    #     rotation=72 if len(x_name) > 12 else 0,
    #     labels=x_name
    # )

    # 使用 plt.annotate() 在每個數據點上方顯示數值，並且可以更為細緻地調整偏移位置，較 plt.text() 的功能更為豐富實用
    # 從 Gemini Code Assist 習得使用方式後進行些微調整
    for i in range(len(x_name)):
        plt.annotate(
            "{}".format(y1_list[i]),  # 要顯示的 y 高度數據資料
            xy=(x_name[i], y1_list[i]),  # 設定數據點的 (x, y) 座標做為放置文字的註解點
            xytext=(0, 3),  # 設定文字相對於註解點的偏移量為 y 方向向上偏移 3（點）
            textcoords="offset points",  # 設定 xytext 是以 點(pt) 為單位的方式相對於 xy 進行偏移，可以保證圖表放大後依然不會有過大的跑位
            rotation = 18 if len(x_name) > 12 else 0,  # 使用三元運算子決定旋轉角度，可以有效避免數值重疊，同時更為 Pythonic
            # ha="center",  # 將水平對其方式設為置中對齊，使文字的正中央對齊數據點的正中央  # TODO 進行大量實際測試後再決定是否啟用本參數
            va="bottom"  # 將垂直對齊方式設為底部對齊，使文字出現在點的上方
        )
    # 顯示效果優於以下方式
    # for i in range(len(x_name)):
    #     plt.text(x_name[i], y_list[i], f'{y_list[i]}', ha='center', va='bottom')
    # 參考來源：https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html
    # 參考來源：https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text

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

    plt.figure(facecolor="whitesmoke")  # 設定圖表區的背景色為白煙色，增加圖表可視度

    # 使用類別標籤與數據資料，增加 6 色循環顯示與 y 高度數值顯示
    plt.bar_label(plt.bar(x_name, y_list, color=color_list))
    # 等效於以下內容
    # bar_container = plt.bar(x_name, y_list, color=color_list)
    # plt.bar_label(bar_container, y_list)
    # 參考來源：https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html

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

    plt.pie(filtered_list, labels=filtered_name, autopct="%2.1f%%", pctdistance=0.72, labeldistance=1.25)  # 使用過濾後的類別標籤與數據資料比例
    plt.show()  # 顯示圖表
