# Модуль выделения писем в веб MS Outlook и перемещение в корзину. Работает удаленно под монитор макбука
import pyautogui
import time

times = 100  # сколько раз проходить

time.sleep(3)
for x in range(times):
    pyautogui.keyDown('shift')
    for i in range(10):  # сколько строк выделять
        pyautogui.press('down')
    pyautogui.keyUp('shift')
    print('цикл')

    pyautogui.click(280, 205)
    time.sleep(1)

pyautogui.alert('все')
