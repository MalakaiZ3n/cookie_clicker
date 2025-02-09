import pyautogui
import keyboard
import time
import random

pyautogui.FAILSAFE = True

pyautogui.useImageNotFoundException(False)

pyautogui.countdown(10)


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
        'factory.png', grayscale=False, confidence=.85)
    bank = pyautogui.locateOnScreen(
        'bank.png', grayscale=False, confidence=.85)
    x_close = pyautogui.locateOnScreen(
        'x_close.png', grayscale=False, confidence=.85)
    temple = pyautogui.locateOnScreen(
        'temple.png', grayscale=False, confidence=.85)
    golden_cookie = pyautogui.locateOnScreen(
        'golden_cookie.png', grayscale=False, confidence=.90)
    tower = pyautogui.locateOnScreen(
        'tower.png', grayscale=False, confidence=.85)
    shipment = pyautogui.locateOnScreen(
        'shipment.png', grayscale=True, confidence=.85)
    alchemy = pyautogui.locateOnScreen(
        'alchemy.png', grayscale=True, confidence=.85)

    pics = [bank, grandma, mine, farm,
            factory, cursor, tower, x_close, temple, shipment, alchemy]

    # if pyautogui.locateOnScreen('cookie.PNG', grayscale=True, confidence=.80) != None:
    try:

        def tile_click():
            image = random.choice(pics)
            pyautogui.moveTo(image)
            pyautogui.click()
            print(f"I clicked on {image}")
            time.sleep(1)

            pyautogui.moveTo(cookie)
            pyautogui.click(cookie, clicks=160, interval=.075)
            print(f"I clicked the cookie {cookie}")
            time.sleep(1)
            # pyautogui.click(golden_cookie)
        tile_click()
    except:
        print('I cannot find you!')
        time.sleep(.75 - (time.time() % .75))
