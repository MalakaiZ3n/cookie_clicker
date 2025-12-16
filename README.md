# Cookie Clicker Automation Bot

A Python automation script that plays Cookie Clicker by automatically clicking the cookie and purchasing buildings/upgrades.

## Overview

This bot uses image recognition to identify and interact with Cookie Clicker game elements on screen. It continuously clicks the cookie and purchases available buildings to maximize cookie production.

## Features

- **Automated Cookie Clicking**: Rapidly clicks the main cookie (140 clicks per cycle)
- **Smart Building Purchases**: Automatically detects and purchases available buildings including:
  - Cursor
  - Grandma
  - Farm
  - Mine
  - Factory
  - Bank
  - Temple
  - Wizard Tower
  - Shipment
  - Alchemy Lab
  - Portal
  - Time Machine
- **Golden Cookie Detection**: Actively detects and clicks golden cookies with 50% confidence threshold
- **Safe Exit**: Press ESC to stop the bot at any time
- **Error Handling**: Gracefully handles missing images and unexpected errors

## Requirements

- Python 3.x
- `pyautogui` - For screen automation
- `keyboard` - For hotkey detection
- Screenshot images of game elements (cookie.PNG, cursor.png, farm.png, etc.)

## Installation

```bash
pip install pyautogui keyboard
```

## Usage

1. Ensure Cookie Clicker is open and visible on your screen
2. Position the game window consistently
3. Run the script:
   ```bash
   python gamer.py
   ```
4. You have 6 seconds to position your cursor/window before automation begins
5. Press ESC to stop the bot

## How It Works

The script operates in a continuous loop:
1. Scans the screen for building/upgrade images using template matching
2. Randomly shuffles and clicks on an available building to purchase
3. Actively searches for golden cookies and clicks them when detected
4. If no golden cookie is found, rapidly clicks the main cookie 140 times with 0.075 second intervals
5. Repeats until ESC is pressed


## Notes

- Building and cookie detection uses **70% confidence** for reliable matching
- Golden cookie detection uses **50% confidence** (more lenient for rare spawns)
- Failsafe is enabled - move mouse to screen corner to emergency stop
- Script shuffles building purchase order each cycle for varied gameplay
- Console output shows all clicks and errors for debugging

## Image Requirements

The following PNG screenshots must be in the same directory as the script:

**Required:**
- `cookie.PNG` - The main cookie
- `cursor.png` - Cursor building
- `grandma.png` - Grandma building
- `farm.png` - Farm building
- `mine.png` - Mine building
- `factory.png` - Factory building
- `bank.png` - Bank building
- `temple.png` - Temple building
- `tower.png` - Wizard Tower building
- `shipment.png` - Shipment building
- `alchemy.png` - Alchemy Lab building
- `portal.png` - Portal building
- `time_machine.png` - Time Machine building

**Optional (for golden cookie detection):**
- `golden_cookie.png` - Golden cookie variant 1
- `golden_cookie1.png` - Golden cookie variant 2
- `golden_cookie2.png` - Golden cookie variant 3
- `golden_cookie3.png` - Golden cookie variant 4
- `golden_cookie4.png` - Golden cookie variant 5

## Troubleshooting

**Bot not finding images:**
- Ensure game window is fully visible and not overlapped
- Verify screenshot images are in the same directory as `gamer.py`
- Check that image filenames match exactly (case-sensitive)
- Adjust confidence levels in code if needed (default: 0.7 for buildings, 0.5 for golden cookies)

**Bot clicking wrong locations:**
- Take new screenshots at your current screen resolution
- Ensure screenshots don't include browser chrome or window borders
- Use grayscale screenshots for better matching

**Performance issues:**
- Increase `time.sleep()` value at end of loop (currently 0.5 seconds)
- Reduce number of clicks per cycle (currently 140)
- Close other applications to free up system resources

## License

For educational and personal use only. Cookie Clicker game is owned by Orteil and Opti