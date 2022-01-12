import pyautogui as pag
import datetime as dt
from time import sleep


print("test test test")

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