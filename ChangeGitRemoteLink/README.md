# Change Remote Git Link

This script can be used to change the remote link from which updates will be downloaded and where new updates will be uploaded.

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Faleff-github%2Fmy-flipper-shits&count_bg=%233C3C3C&title_bg=%233C3C3C&icon=linux.svg&icon_color=%23FFFFFF&title=views&edge_flat=false)](https://github.com/aleff-github/my-flipper-shits)

**Category**: Execute

<div align=center>

<img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/logo-repository-2_0.gif" width="600" /><br><img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/DISCLAIMER.png" width="600" />

</div>

## Description

This script can be used to change the remote link from which updates will be downloaded and where new updates will be uploaded.

This script turns out to be very useful for aviting data leaks between old cloned repositories and new online repositories.

To make it easier to use below you can find the various tested configurations, at the moment it is not available for macOS because since I do not have one it cannot be tested and therefore I cannot give the certainty that it works, however I hope that in the Hak5 community there may be someone who can contribute to this payload by completing it with this missing part.

## Payload.txt config - Windows 10/11 - Tested on Windows 11

```DuckyScript
    DELAY 1000
    GUI r
    DELAY 1000
    STRING powershell
    ENTER
    DELAY 2000
```

## Payload.txt config - Linux (Debian based) - Tested on Ubuntu 23.04

```DuckyScript
    DELAY 1000
    CTRL-ALT t
    DELAY 2000
```


## Dependencies

* Internet Connection
* git installed
* Full path of the cloned repository
* ExecutionPolicy Bypass

## Settings

- Full path of the local repository i.e. "C:\Users\User\Documents\Repository1"
```DuckyScript
    DEFINE #FULL-PATH example
```

- Link from which updates are to be downloaded so the new repository the Repository2
```DuckyScript
    DEFINE #NEW-GIT-LINK example.git
```

- REM Define the branch of the new repository Repository2, i.e. "main"
```DuckyScript
    DEFINE #BRANCH example
```