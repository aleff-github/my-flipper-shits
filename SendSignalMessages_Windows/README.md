# Send Signal Messages - BadUSB ✅

A script used to impersonate another person in sending a message via the Signal application.

**Category**: Prank, Execution

<div align=center>

<img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/logo-repository-2_0.gif" width="600" /><br><img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/DISCLAIMER.png" width="600" />

</div>

## Description

A script used to impersonate another person in sending a message via the Signal application.

Opens PowerShell to run Signal app and then, using some TAB, write the phone number, then the message, then send it, then close the app.

## Getting Started

### Dependencies

* An internet connection
* Signal App installed
* Windows 10,11

### Executing program

* Plug in your device
* Open a powershell that will close (if open) the Signal app and then, the powershell, will open it again
* Some tabs
* Write the number - Default: 3332211000
* Send the message - Default: Hello World!
* Close the Signal app

In the payload.txt file you must change the number
```txt
REM REQUIRED - Receiver number
STRING 3332211000
```

and the message
```txt
REM This is the message that will be sent.
REM You can change it as you want, if you want.
STRING Hello World!
```
