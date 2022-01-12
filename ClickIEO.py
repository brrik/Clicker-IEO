import pyautogui as pag
import datetime as dt
from time import sleep


while True:
    print("クリック開始時刻を記載してください。")
    print("指定時刻の10秒前からクリックを開始します。")
    print("\n\n\n")
    hourStr = input("時刻    時：")
    minStr = input("時刻    分：")

    if hourStr != "" and minStr != "" :
        try:
            hour = int(hourStr)
            minute = int(minStr)
            break
        except:
            print("時刻の記入形式が違うようです。再度確認してください。")
    else:
        print("時刻に空欄があります。0時・0分のときは0を入力して下さい。")
    



try:
    print("Search for the Button...")
    print("\n\n\n")

    while True:

        
        x, y = pag.position()
        color = pag.pixel(x,y)
        red = color[0]
        green = color[1]
        blue = color[2]

        if red == 232 and green == 92 and blue == 17:
            pag.click(x,y)
            print("FOUND!! CLICK!!")
            pag.press("\t")
            pag.press("\t")
            pag.press(" ")
            date_s = (dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
            break
        sleep(0.1)
    print(date_s)


except:
    import traceback
    traceback.print_exc()
    input("ERROR Press Enter")