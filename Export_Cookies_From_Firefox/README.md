# Export Firefox Cookies Database

This script may come in handy for those who want to quickly save all the cookies of their Firefox session by exporting the database via dropbox accesstoken.

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Faleff-github%2Fmy-flipper-shits&count_bg=%233C3C3C&title_bg=%233C3C3C&icon=linux.svg&icon_color=%23FFFFFF&title=views&edge_flat=false)](https://github.com/aleff-github/my-flipper-shits)

**Category**: Exfiltration

<div align=center>

<img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/logo-repository-2_0.gif" width="600" /><br><img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/DISCLAIMER.png" width="600" />

</div>

## Description

This script may come in handy for those who want to quickly save all the cookies of their Firefox session by exporting the database via dropbox accesstoken.

Open a PowerShell, select dynamically the Firefox path adding "cookies.sqlite" at the end, then set your exfiltration settings i.e. Dropbox access token and so on... then export it, then close the powershell.

## Dependencies

* Firefox must be installed

## Settings

- You must define your Dropbox accessToken or modify the exfiltration modality. Replace just the example word with your token.

`DEFINE DROPBOX_ACCESS_TOKEN "example"`