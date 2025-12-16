import pyautogui
import keyboard
import time
import random

pyautogui.FAILSAFE = True

# Optional: suppress image-not-found exceptions if supported
try:
    pyautogui.useImageNotFoundException(False)
except pyautogui.PyAutoGUIException as e:
    print("Warning: useImageNotFoundException not available:", e)

print("Starting in 6 seconds. Press ESC to stop.")
pyautogui.countdown(6)

# Define images
stores = ['cursor.png', 'grandma.png', 'farm.png', 'mine.png', 'factory.png',
             'bank.png', 'temple.png', 'tower.png', 'shipment.png',
             'alchemy.png', 'portal.png', 'time_machine.png']

goldens = ['golden_cookie.png', 'golden_cookie1.png',
           'golden_cookie2.png', 'golden_cookie3.png', 'golden_cookie4.png']

# Define main functions
def find_image(images, confidence=0.5):
    for image in images:
        matches = pyautogui.locateAllOnScreen(image, confidence=confidence)
        if matches:
            for match in matches:
                center = pyautogui.center(match)
                return center
    return None

def click_cookie(cookie):
    if cookie:
        pyautogui.moveTo(cookie)
        pyautogui.click(cookie, clicks=140, interval=0.075)
        print(f"Clicked cookie at {cookie}")

while not keyboard.is_pressed('esc'):
    try:
        cookie = pyautogui.locateCenterOnScreen('cookie.PNG', grayscale=True, confidence=0.7)

        # Click random building if available
        random.shuffle(stores)
        for store in stores:
            location = pyautogui.locateCenterOnScreen(store, grayscale=True, confidence=0.7)
            if location:
                pyautogui.moveTo(location)
                pyautogui.click(location)
                print(f"Clicked store item: {store} at {location}")
                break

        # Click golden cookie if found
        golden_found = find_image(goldens, confidence=0.5)
        if golden_found:
            pyautogui.moveTo(golden_found)
            pyautogui.click(golden_found)
            print(f"Clicked golden cookie at {golden_found}")
        else:
            click_cookie(cookie)

    except Exception as e:
        print(f"Error: {e}")
    time.sleep(0.5)
