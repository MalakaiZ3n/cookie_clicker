# Cookie Clicker Automation Bot

A Python automation script that plays Cookie Clicker by automatically clicking the cookie, purchasing the most expensive affordable building, and clicking golden cookies.

## Features

- **Automated Cookie Clicking**: Rapidly clicks the main cookie (140 clicks per cycle)
- **Smart Building Purchases**: Color-scans the store panel for green (affordable) price text and buys the most expensive item you can afford — no reference images needed
- **Golden Cookie Detection**: Background thread scans every second using HSV color detection and clicks golden cookies immediately
- **Debug Screenshots**: Saves annotated screenshots of store purchases (`store_debug/`) and golden cookie clicks (`golden_debug/`) for review — last 10 kept
- **Safe Exit**: Press ESC to stop the bot at any time

## Requirements

- Python 3.x
- `pyautogui`
- `keyboard`
- `opencv-python`
- `numpy`
- `Pillow`
- `cookie.PNG` — screenshot of the main cookie (only image required)

## Installation

```bash
pip install pyautogui keyboard opencv-python numpy Pillow
```

## Usage

1. Open Cookie Clicker and position the game window
2. Run the script:
   ```bash
   python gamer.py
   ```
3. You have 6 seconds to switch to the game window before automation begins
4. Press ESC to stop

## How It Works

**Main loop** (runs every 0.1s):
1. Locates the main cookie via image match and clicks it 140 times
2. Takes a screenshot and color-scans the store panel for green price text
3. Buys the most expensive affordable building (last green-priced row in the store)

**Background thread** (runs every 1s):
1. Takes a full screenshot and scans for golden-hued circular blobs in HSV color space
2. Clicks any golden cookie found immediately

## Configuration

All position constants are at the top of `gamer.py`:

| Constant | Description |
|---|---|
| `STORE_X1`, `STORE_X2` | Horizontal bounds of the store panel |
| `STORE_Y1`, `STORE_Y2` | Vertical bounds of the store panel |
| `STORE_X_CLICK` | X coordinate to click when buying a store item |

Adjust these to match your screen resolution and window position.

## Debug Folders

| Folder | Contents |
|---|---|
| `store_debug/` | Screenshot per purchase with a green line showing the targeted row |
| `golden_debug/` | Screenshot per golden cookie click with a circle at the click point |

Both folders keep only the last 10 images.

## Troubleshooting

**Bot not clicking the cookie:**
- Retake `cookie.PNG` at your current resolution
- Ensure the cookie is fully visible and unobstructed

**Bot buying wrong store rows / buying when it can't afford:**
- Adjust `STORE_X1`/`STORE_X2`/`STORE_Y1`/`STORE_Y2` to match your store panel
- Review `store_debug/` screenshots to see what row is being targeted
- Tighten the green detection thresholds in `find_best_store_item` if needed

**Golden cookie not detected:**
- Review `golden_debug/` screenshots to see what the detector is finding
- Adjust the HSV range in `find_golden_cookie` if cookies are being missed or false-positives appear

**Failsafe:** Move mouse to any screen corner to emergency-stop pyautogui.

## License

For educational and personal use only. Cookie Clicker is owned by Orteil and Opti.
