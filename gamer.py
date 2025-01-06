import pyautogui
import keyboard
import time
import random

pyautogui.FAILSAFE = True

pyautogui.useImageNotFoundException(False)

pyautogui.countdown(5)


while not keyboard.is_pressed('esc'):

    cookie = pyautogui.locateOnScreen(
        'cookie.PNG', grayscale=False, confidence=.80)
    cursor = pyautogui.locateOnScreen(
        'cursor.png', grayscale=False, confidence=.80)
    farm = pyautogui.locateOnScreen(
        'farm.png', grayscale=False, confidence=.80)
    grandma = pyautogui.locateOnScreen(
        'grandma.png', grayscale=False, confidence=.80)
    mine = pyautogui.locateOnScreen(
        'mine.png', grayscale=False, confidence=.80)
    factory = pyautogui.locateOnScreen(
        'factory.png', grayscale=False, confidence=.80)
    bank = pyautogui.locateOnScreen(
        'bank.png', grayscale=False, confidence=.80)
    x_close = pyautogui.locateOnScreen(
        'x_close.png', grayscale=False, confidence=.80)
    temple = pyautogui.locateOnScreen(
        'temple.png', grayscale=False, confidence=.80)
    golden_cookie = pyautogui.locateOnScreen(
        'golden_cookie.png', grayscale=False, confidence=.80)

    pics = [cookie, bank, grandma, mine, farm,
            factory, cursor, x_close, temple, golden_cookie]
    num_clicks = random.randint(1, 10)
    # if pyautogui.locateOnScreen('cookie.PNG', grayscale=True, confidence=.80) != None:
    try:

        def tile_click():
            image = random.choice(pics)
            pyautogui.moveTo(image)
            pyautogui.click()
            print(f"I clicked on {image}")
            time.sleep(1)

            pyautogui.moveTo(cookie)
            pyautogui.click(cookie, clicks=80, interval=.09)
            print(f"I clicked on the cookie {cookie}")
            time.sleep(1)
            pyautogui.click(golden_cookie)
        tile_click()
    except:
        print('I cannot find you!')
        time.sleep(.75 - (time.time() % .75))
