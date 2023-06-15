# Starting a PowerShell with administrator permissions in Windows 10/11

This script can be considered by people who are new to the world of scripts written in DuckyScript so that they can understand how to start a PowerShell with administrator permissions on a Windows machine.

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Faleff-github%2Fmy-flipper-shits&count_bg=%233C3C3C&title_bg=%233C3C3C&icon=linux.svg&icon_color=%23FFFFFF&title=views&edge_flat=false)](https://github.com/aleff-github/my-flipper-shits)

**Category**: Execute

<div align=center>

<img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/logo-repository-2_0.gif" width="600" /><br><img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/DISCLAIMER.png" width="600" />

</div>

## Description

This script can be considered by people who are new to the world of scripts written in DuckyScript so that they can understand how to start a PowerShell with administrator permissions on a Windows machine.

Starting a PowerShell session with administrator privileges means the session has access to features and operations that require high permissions on the Windows operating system.

Some PowerShell commands require administrator privileges to run properly. Starting PowerShell as an administrator allows you to execute commands that require elevated permissions, such as managing system services, changing security settings, creating or modifying user accounts, installing system-level software, and so on.

It is important to note that running PowerShell with administrator privileges involves a higher level of responsibility and can cause significant changes to the system. Therefore, it is advisable to be careful and fully understand the effects of operations performed in a session with administrator privileges to avoid unwanted or harmful changes.

## Dependencies

* Nothing

## Example

- `STRINGLN Get-ExecutionPolicy -List`
![](docs/1.png)

- `STRINGLN Set-ExecutionPolicy Bypass`
![](docs/2.png)

- `STRINGLN Get-ExecutionPolicy -List`
![](docs/3.png)