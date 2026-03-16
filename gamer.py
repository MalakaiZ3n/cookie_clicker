import pyautogui
import keyboard
import time
import threading
import os
import glob
import numpy as np
import cv2
from PIL import ImageGrab
from datetime import datetime

pyautogui.FAILSAFE = True

# Optional: suppress image-not-found exceptions if supported
try:
    pyautogui.useImageNotFoundException(False)
except pyautogui.PyAutoGUIException as e:
    print("Warning: useImageNotFoundException not available:", e)

print("Starting in 6 seconds. Press ESC to stop.")
pyautogui.countdown(6)

# Store panel region — adjust if your window size/position differs
STORE_X1, STORE_X2 = 1610, 1800   # horizontal bounds of the store panel
STORE_Y1, STORE_Y2 = 164, 1000      # vertical bounds (below buy/sell header, above taskbar)
STORE_X_CLICK     = 1680           # x to click when buying (middle of store row)

stop_event = threading.Event()
mouse_lock = threading.Lock()

DEBUG_DIR = "golden_debug"
os.makedirs(DEBUG_DIR, exist_ok=True)

STORE_DEBUG_DIR = "store_debug"
os.makedirs(STORE_DEBUG_DIR, exist_ok=True)

def save_debug_screenshot(img_rgb, cx, cy, area, clicked):
    """Save annotated screenshot and prune to last 10."""
    debug = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
    color = (0, 255, 0) if clicked else (0, 0, 255)
    cv2.circle(debug, (cx, cy), 40, color, 3)
    label = f"{'CLICK' if clicked else 'MISS'} area={area:.0f}"
    cv2.putText(debug, label, (cx + 45, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    timestamp = datetime.now().strftime("%H%M%S_%f")
    path = os.path.join(DEBUG_DIR, f"{timestamp}.png")
    cv2.imwrite(path, debug)
    # Keep only last 10
    files = sorted(glob.glob(os.path.join(DEBUG_DIR, "*.png")))
    for old in files[:-10]:
        os.remove(old)

def find_golden_cookie():
    """Detect golden cookie by its golden hue, ignoring shape/rotation."""
    screenshot = ImageGrab.grab()
    img = np.array(screenshot)
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    # Golden cookie HSV range (warm gold/yellow-orange glow)
    lower = np.array([15, 100, 150])
    upper = np.array([40, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)

    # Clean up noise
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    best = None
    best_area = 0
    best_pos = None
    for contour in contours:
        area = cv2.contourArea(contour)
        # Filter by size: golden cookie is roughly 55-120px wide
        if 2500 < area < 14000:
            # Must be roughly circular (filters background noise and irregular blobs)
            perimeter = cv2.arcLength(contour, True)
            if perimeter == 0:
                continue
            circularity = 4 * np.pi * area / (perimeter ** 2)
            if circularity < 0.3:
                continue
            M = cv2.moments(contour)
            if M["m00"] > 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                if area > best_area:
                    best_area = area
                    best_pos = (cx, cy)
                    best = (img, cx, cy, best_area)

    if best_pos:
        print(f"Golden cookie found at {best_pos}, area={best_area:.0f}")
    return best

def golden_watcher():
    """Background thread: scans for golden cookie every second and clicks immediately."""
    while not stop_event.is_set():
        try:
            result = find_golden_cookie()
            if result:
                img, cx, cy, area = result
                with mouse_lock:
                    pyautogui.moveTo((cx, cy))
                    pyautogui.click((cx, cy))
                    print(f"[GOLDEN] Clicked at ({cx}, {cy})")
                save_debug_screenshot(img, cx, cy, area, clicked=True)
        except Exception as e:
            print(f"Golden watcher error: {e}")
        time.sleep(1.0)

def save_store_debug(img_rgb, target_y):
    """Save annotated store screenshot and prune to last 10."""
    debug = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
    cv2.line(debug, (STORE_X1, target_y), (STORE_X2, target_y), (0, 255, 0), 2)
    cv2.circle(debug, (STORE_X_CLICK, target_y), 10, (0, 255, 0), -1)
    timestamp = datetime.now().strftime("%H%M%S_%f")
    path = os.path.join(STORE_DEBUG_DIR, f"{timestamp}.png")
    cv2.imwrite(path, debug)
    files = sorted(glob.glob(os.path.join(STORE_DEBUG_DIR, "*.png")))
    for old in files[:-10]:
        os.remove(old)

def find_best_store_item(img_rgb):
    """Scan the store panel for orange price text; return click coords of the most expensive affordable row."""
    region = img_rgb[STORE_Y1:STORE_Y2, STORE_X1:STORE_X2]
    r = region[:, :, 0].astype(float)
    g = region[:, :, 1].astype(float)
    b = region[:, :, 2].astype(float)

    # Green price text = affordable (bright, strongly green-dominant)
    green_mask = (g > 150) & (g > r * 1.6) & (g > b * 1.6)
    row_sums = green_mask.sum(axis=1)
    orange_rows = np.where(row_sums > 20)[0]

    if len(orange_rows) == 0:
        return None

    # Cluster adjacent rows into per-item groups
    clusters = []
    cluster = [orange_rows[0]]
    for y in orange_rows[1:]:
        if y - cluster[-1] <= 4:
            cluster.append(y)
        else:
            clusters.append(cluster)
            cluster = [y]
    clusters.append(cluster)

    # Last cluster = most expensive affordable item
    best_row_y = STORE_Y1 + int(np.mean(clusters[-1]))
    return (STORE_X_CLICK, best_row_y, img_rgb)

def click_cookie(cookie):
    if cookie:
        with mouse_lock:
            pyautogui.moveTo(cookie)
            pyautogui.click(cookie, clicks=140, interval=0.075)

# Start golden cookie watcher in background
watcher_thread = threading.Thread(target=golden_watcher, daemon=True)
watcher_thread.start()
print("Golden cookie watcher started.")

while not keyboard.is_pressed('esc'):
    try:
        cookie = pyautogui.locateCenterOnScreen('cookie.PNG', grayscale=True, confidence=0.7)

        # Buy the most expensive affordable building (color-scan, no reference images needed)
        screenshot = ImageGrab.grab()
        img_rgb = np.array(screenshot)
        store_result = find_best_store_item(img_rgb)
        if store_result:
            store_x, store_y, store_img = store_result
            store_target = (store_x, store_y)
            with mouse_lock:
                pyautogui.moveTo(store_target)
                pyautogui.click(store_target)
            print(f"Bought store item at {store_target}")
            save_store_debug(store_img, store_y)

        click_cookie(cookie)

    except Exception as e:
        print(f"Error: {e}")
    time.sleep(0.1)

stop_event.set()
