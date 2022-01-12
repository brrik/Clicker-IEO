import pyautogui as pag
import datetime as dt
from time import sleep


while True:
    print("クリック予定時刻を入力します。時、分を分けて入力してください。")
    wantHourStr = input("クリック時刻を記載してください(24時間形式)：時　　")
    wantMinStr = input("クリック時刻を記載してください(24時間形式)：分　　")

    try:
        wantHourInput = int(wantHourStr)
        wantMinInput = int(wantMinStr)

        if wantHourInput > 23:
            print("設定範囲外の時刻になっています。時間設定は0～23時の範囲で設定してください。")
        elif wantMinInput > 59:
            print("設定範囲外の時刻になっています。時間設定は0～59分の範囲で設定してください。")
        else:
            break

    except:
        print("入力が不正です。全角でないか、数字以外を入力していないかを確認してください。")

print(f"{wantHourInput}時{wantMinInput}分にクリックを実行します。")
print("")


if wantHourInput == 0 & wantMinInput == 0:
    wantHour = 23
    wantMin = 59

elif wantMinInput == 0:
    wantHour = wantHourInput -1
    wantMin = 59

else:
    wantHour = wantHourInput
    wantMin = wantMinInput -1

print(f"{wantHour}時{wantMin}分まで動作を待機します。")

while True:
    dt_nowCk = dt.datetime.now()
    dt_hourCk = dt_nowCk.hour
    dt_minCk = dt_nowCk.minute
    print(f"{dt_hourCk}:{dt_minCk}")
    
    difHour = wantHour - dt_hourCk
    difMin = wantMin - dt_minCk

    print(f"あと{difHour}:{difMin}")

    if dt_hourCk == wantHour and dt_minCk == wantMin:
        print("指定時刻が近づきました。")
        print("マウスを指定位置から動かさないでください。")
        break

    sleep(10)

while True:
    dt_nowCk = dt.datetime.now()
    dt_second = dt_nowCk.second
    if dt_second > 45:
        print("15秒前です。クリックを開始します。")
        break
    print(dt_second)
    sleep(1)

x, y = pag.position()
color = pag.pixel(x,y)
red = color[0]
green = color[1]
blue = color[2]

while True:
    try:
        pag.click()
        x2, y2 = pag.position()
        color2 = pag.pixel(x2,y2)
        red2 = color2[0]
        green2 = color2[1]
        blue2 = color2[2]

        if red2 != red and green2 != green and blue2 != blue:

            print("FOUND!! CLICK!!")
            pag.press("\t")
            pag.press("\t")
            pag.press(" ")
            date_s = dt.datetime.now()
            print(date_s)

            print("正常に動作を完了しました。")
            print("不具合が発生している場合、正常動作でない場合は、至急開発者へお問い合わせください。")
            input("処理終了にはEnter/Returnを押下：")

            break

        sleep(0.1)



    except:
        import traceback
        print("=======================================================================\n\n")
        traceback.print_exc()
        print("=======================================================================\n\n")
        print("この画面が表示された場合は、スクリーンショットを取得の上、開発者までご送付をお願いいたします。")
        print("スクリーンショットはかならず、====で囲われた部分すべてを取得してください。\n\n")
        input("ERROR Press Enter")