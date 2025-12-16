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
- **Golden Cookie Detection**: Framework in place for detecting and clicking golden cookies (currently commented out)
- **Safe Exit**: Press ESC to stop the bot at any time

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
2. Randomly selects and clicks on an available building to purchase
3. Rapidly clicks the cookie 140 times with 0.075 second intervals
4. Repeats until ESC is pressed

## Notes

- The script uses `grayscale=True` and 80% confidence for image matching
- Failsafe is enabled - move mouse to screen corner to emergency stop
- Requires PNG screenshots of game elements for image recognition
- Golden cookie detection is currently disabled but can be enabled by uncommenting relevant code

## Image Requirements

The following PNG screenshots must be in the same directory as the script:
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
- `x_close.png` - Close button
- `golden_cookie.png` (and variants 1-4) - Golden cookies (optional)