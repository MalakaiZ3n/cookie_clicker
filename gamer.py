import pyautogui
import keyboard
import time
import random

pyautogui.FAILSAFE = True

pyautogui.useImageNotFoundException(False)

pyautogui.countdown(6)


while not keyboard.is_pressed('esc'):

    cookie = pyautogui.locateOnScreen(
        'cookie.PNG', grayscale=True, confidence=.80)
    cursor = pyautogui.locateOnScreen(
        'cursor.png', grayscale=True, confidence=.80)
    farm = pyautogui.locateOnScreen(
        'farm.png', grayscale=True, confidence=.80)
    grandma = pyautogui.locateOnScreen(
        'grandma.png', grayscale=True, confidence=.80)
    mine = pyautogui.locateOnScreen(
        'mine.png', grayscale=True, confidence=.80)
    factory = pyautogui.locateOnScreen(
        'factory.png', grayscale=True, confidence=.80)
    bank = pyautogui.locateOnScreen(
        'bank.png', grayscale=True, confidence=.80)
    x_close = pyautogui.locateOnScreen(
        'x_close.png', grayscale=True, confidence=.80)
    temple = pyautogui.locateOnScreen(
        'temple.png', grayscale=True, confidence=.80)
    tower = pyautogui.locateOnScreen(
        'tower.png', grayscale=True, confidence=.80)
    shipment = pyautogui.locateOnScreen(
        'shipment.png', grayscale=True, confidence=.80)
    alchemy = pyautogui.locateOnScreen(
        'alchemy.png', grayscale=True, confidence=.80)
    portal = pyautogui.locateOnScreen(
        'portal.png', grayscale=True, confidence=.80)
    time_machine = pyautogui.locateOnScreen(
        'time_machine.png', grayscale=True, confidence=.80)
    goldens = ['golden_cookie.png', 'golden_cookie1.png',
               'golden_cookie2.png', 'golden_cookie3.png', 'golden_cookie4.png']

    pics = [cookie, bank, grandma, mine, farm,
            factory, cursor, tower, x_close, temple, shipment, alchemy, portal, time_machine]

    # if pyautogui.locateOnScreen('cookie.PNG', grayscale=True, confidence=.80) != None:
    try:

        def tile_click():
            image = random.choice(pics)
            pyautogui.moveTo(image)
            pyautogui.click(image)
            print(f"I clicked on " f"{image}")
            # time.sleep(.25)

            pyautogui.moveTo(cookie)
            pyautogui.click(cookie, clicks=140, interval=.075)
            print(f"I clicked the cookie " f"{cookie}")

            # time.sleep(.25)
            # for golden in goldens:
            #     if pyautogui.locateOnScreen(golden, grayscale=True, confidence=.80):
            #         pyautogui.moveTo(golden)
            #         pyautogui.click(golden)
            #         print(f"I found the golden cookie {golden}")
            #     else:
            #         pyautogui.locateOnScreen(
            #             cookie, grayscale=True, confidence=.85)
            #         pyautogui.moveTo(cookie)
            #         pyautogui.click(cookie, clicks=140, interval=.075)
            #         # tsleep(.25)me.sleep(.25)
            #         print('Cookies are the Solution!')
        tile_click()
    except:
        print('I cannot find you!')
        time.sleep(.75 - (time.time() % .75))
