# Change the password of the windows user

Through this script you will be able to change windows user's password super fast.

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Faleff-github%2Fmy-flipper-shits&count_bg=%233C3C3C&title_bg=%233C3C3C&icon=linux.svg&icon_color=%23FFFFFF&title=views&edge_flat=false)](https://github.com/aleff-github/my-flipper-shits)

**Category**: Execute

<div align=center>

<img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/logo-repository-2_0.gif" width="600" /><br><img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/DISCLAIMER.png" width="600" />

</div>

## Description

Through this script you will be able to change windows user's password super fast.

A PowerShell with administrator permissions is started, and through the use of the `net` command you can change the password without necessarily having to know the original password.

It is always very fascinating to see how many things you can do on Windows systems without needing to know the original password. As fascinating as it is disturbing.

## Dependencies

* Nothing (i know it's absurd)

## Example

- `STRINGLN Get-ExecutionPolicy -List`
![](docs/1.png)

- `STRINGLN Set-ExecutionPolicy Bypass`
![](docs/2.png)

- `STRINGLN Get-ExecutionPolicy -List`
![](docs/3.png)