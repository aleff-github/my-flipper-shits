# Send Message iOS - by bst04

<div align=center>

<img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/logo-repository-2_0.gif" width="600" /><br><img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/DISCLAIMER.png" width="600" />

</div>

## Description

This script, created by bst04, is designed to work on iOS systems. It opens the Messages app, navigates to a specific contact, and sends a predefined text message.

---

## Technical Explanation

1. **Initialization**:
    - `DELAY 2000`: Waits for 2 seconds to ensure the system is ready.
    - `GUI h`: Simulates pressing "Command" + "h" to hide the current application.
    - `DELAY 150`: Waits for 0.15 seconds.
    - `GUI SPACE`: Simulates pressing "Command" + "Space" to open Spotlight Search.
    - `DELAY 150`: Waits for 0.15 seconds for Spotlight to open.
    - `BACKSPACE`: Clears any existing text in the search bar.

2. **Open Messages App**:
    - `DELAY 500`: Waits for 0.5 seconds.
    - `STRING Messages`: Types "Messages" to search for the Messages app.
    - `DELAY 250`: Waits for 0.25 seconds.
    - `ENTER`: Opens the Messages app.

3. **Navigate to Contact**:
    - `DELAY 1500`: Waits for 1.5 seconds to ensure the Messages app is fully opened.
    - `GUI n`: Simulates pressing "Command" + "n" to start a new message.
    - `DELAY 250`: Waits for 0.25 seconds.
    - `STRING [persona]`: Types the name of the contact (replace `[persona]` with the actual name).
    - `DELAY 500`: Waits for 0.5 seconds.
    - `ENTER`: Selects the contact.
    - `DELAY 250`: Waits for 0.25 seconds.
    - `TAB`: Navigates to the message input field.
    - `ENTER`: Confirms the selection.
    - `DOWNARROW`: Moves to the message input field.

4. **Send Text Message**:
    - `DELAY 500`: Waits for 0.5 seconds.
    - `STRING [texto]`: Types the predefined message (replace `[texto]` with the actual text).
    - `DELAY 500`: Waits for 0.5 seconds.
    - `ENTER`: Sends the message.

---

## Usage

1. Copy the payload script to your DuckyScript-enabled device.
2. Ensure the device is connected to an iOS system.
3. Execute the payload to open the Messages app, navigate to a specific contact, and send the predefined text message.

