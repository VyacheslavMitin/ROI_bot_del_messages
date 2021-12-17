# Модуль выделения писем в веб аутлке и перемещение в корзину. Работает удаленно под монитор макбука

import pyautogui
import time

times = 100

time.sleep(3)

for x in range(times):
    pyautogui.keyDown('shift')
    for i in range(10):
        pyautogui.press('down')
    pyautogui.keyUp('shift')
    print('цикл')

    pyautogui.click(280, 205)
    time.sleep(1)


pyautogui.alert('все')
