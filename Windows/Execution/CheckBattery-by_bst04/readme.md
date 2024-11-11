# 🔋 CheckBateryWin-FlipZero by bst04

## ℹ️ Description

This script, created by bst04, is designed to work on Windows devices. It generates a battery report using PowerShell and then opens the report in the default web browser.

---

## Technical Explanation

1. **Initialization**:
    - `DELAY 1000`: Waits for 1 second to ensure the system is ready.
    - `GUI r`: Simulates pressing "Windows" + "R" to open the Run dialog.
    - `DELAY 750`: Waits for 0.75 seconds to ensure the Run dialog is open.

2. **Generate Battery Report**:
    - `STRING powershell powercfg /batteryreport`: Types a PowerShell command to generate a battery report.
    - `DELAY 750`: Waits for 0.75 seconds to ensure the command is fully typed.
    - `ENTER`: Executes the PowerShell command to generate the battery report.

3. **Open Battery Report**:
    - `DELAY 250`: Waits for 0.25 seconds to ensure the previous command is processed.
    - `GUI r`: Simulates pressing "Windows" + "R" again to open the Run dialog.
    - `DELAY 850`: Waits for 0.85 seconds to ensure the Run dialog is open.
    - `STRING powershell Start-Process "battery-report.html"`: Types a PowerShell command to open the battery report in the default web browser.
    - `DELAY 750`: Waits for 0.75 seconds.
    - `ENTER`: Executes the PowerShell command to open the battery report.

---

## Usage

1. Copy the payload script to your DuckyScript-enabled device.
2. Ensure the device is connected to a Windows system.
3. Execute the payload to generate and open the battery report.
