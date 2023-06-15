# Set An Arbitrary DNS (IPv4 version)

This script can be used to change the default DNS server in Windows 11.

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Faleff-github%2Fmy-flipper-shits&count_bg=%233C3C3C&title_bg=%233C3C3C&icon=linux.svg&icon_color=%23FFFFFF&title=views&edge_flat=false)](https://github.com/aleff-github/my-flipper-shits)

**Category**: Execute

## Disclaimer

<div align=center>

<img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/gif/flipper_zero%20(15).gif?raw=true" width="209" /><br><img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/DISCLAIMER.png?raw=true" width="600" />

</div>

## Description

This script can be used to change the default DNS server in Windows 11.

The script open the settings, then go to network settings, then go to wi-fi settings, then go to hardware properties settings, the open the dns settings, then change to manual, then set the DNS server defined before, then save the settings changed and close the window.

- You must edit the DNS defining the IPv4 in the payload.txt file

```DuckyScript
REM DNS IPv4 like Cloudflare DNS 1.1.1.1
DEFINE DNS example
```