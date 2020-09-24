import pyautogui
import pynput
import openpyxl as xl
from pynput.mouse import Listener
from pynput import mouse
from pynput import keyboard

def on_move(x, y):
    pass
 
def on_click(x, y, button, pressed):
    if pressed:
        if button == mouse.Button.right:
            listener.stop()
        else:       
            myClicks.append([x,y])
            print(myClicks)
    else:
        pass

def on_scroll(x, y, dx, dy):
    pass


with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    myClicks = []
    wb = xl.Workbook()
    ws = wb.active
    listener.join()

r = 1
c = 1

for i in myClicks:
    for coord in i:
        ws.cell(row=r, column=c).value = coord
        c += 1
    c -= 2
    r += 1

wb.save("coordinates.xlsx")