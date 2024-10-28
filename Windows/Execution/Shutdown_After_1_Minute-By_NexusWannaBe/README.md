# Shutdown After 1 Minute - By NexusWannaBe

<div align=center>

<img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/logo-repository-2_0.gif" width="600" /><br><img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/DISCLAIMER.png" width="600" />

</div>

This DuckyScript, created by [NexusWannaBe](https://github.com/NexusWannaBe), is designed to force a Windows system shutdown after one minute from the insertion of your Flipper Zero or any compatible DuckyScript device. The script opens the **cmd** terminal and sends the shutdown command to the system.

## How it works

The script performs the following steps:
1. Waits for 1 second (`DELAY 1000`).
2. Uses the **Windows + R** combination to open the "Run" dialog.
3. Types `cmd` to open the command prompt.
4. Waits for half a second and then presses **Enter**.
5. Once the terminal is open, it types the command `shutdown /s /f && exit`, which forces the computer to shut down and closes the terminal.
6. Confirms the shutdown by pressing **Enter**. The system will shut down within 60 seconds.

### Shutdown command:
- `shutdown /s /f`: forces an immediate shutdown of Windows, closing all running applications without warning.
- `&& exit`: closes the terminal after issuing the shutdown command.

## Warnings

- **Use this script responsibly!** Forcing a shutdown can result in data loss if files are not saved.
- This script is intended for educational purposes only and should only be used with permission from the owner of the device and in compliance with the law.
