# 🔊 SetVolumeMax-FlipZero by bst04

## ℹ️ Description

This payload, created by bst04, is designed to set the volume to maximum (100%) on a macOS device using AppleScript through Terminal.

---

## 📖 Technical Explanation

1. **Initialization**:
    - `DELAY 1000`: Waits for 1 second to ensure the system is ready.
    - `GUI SPACE`: Simulates pressing "Command" + "Space" to open Spotlight Search.
    - `DELAY 250`: Waits for 0.25 seconds to ensure Spotlight is open.

2. **Set Volume to 100%**:
    - `STRING VOL=$(osascript -e 'Set Volume 100')`: Types the AppleScript command to set the system volume to 100%.
    - `DELAY 250`: Waits for 0.25 seconds.
    - `ENTER`: Executes the command to set the volume.

3. **Close Terminal**:
    - `DELAY 250`: Waits for 0.25 seconds.
    - `GUI q`: Simulates pressing "Command" + "q" to quit the Terminal application.

---

## 📜 Usage

1. Copy the payload script to your DuckyScript-enabled device.
2. Ensure the device is connected to a macOS system.
3. Execute the payload to set the system volume to maximum (100%).

---
