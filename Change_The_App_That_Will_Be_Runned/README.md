# Change The App That Will Be Runned

A script used to prank your friends editing the deafault exec operation of desktop files running other app of wich is clicked confusing the user.

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Faleff-github%2Fmy-flipper-shits&count_bg=%233C3C3C&title_bg=%233C3C3C&icon=linux.svg&icon_color=%23FFFFFF&title=views&edge_flat=false)](https://github.com/aleff-github/my-flipper-shits)

**Category**: Prank

<div align=center>

<img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/logo-repository-2_0.gif" width="600" /><br><img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/DISCLAIMER.png" width="600" />

</div>

![GIF](Change_The_App_That_Will_Be_Runned.gif)

## Description

A script used to prank your friends editing the deafault exec operation of desktop files running other app of wich is clicked confusing the user.

The script will run a shell in wich it will mix 2 application

## Getting Started

### Dependencies

* sudo permissions
* Original desktop file names and exec commands
* The apps must be installed in the target

### Settings

- Set the desktop file name, i.e. for Signal it is `/usr/share/applications/signal-desktop` and the exec command is `/opt/Signal/signal-desktop --no-sandbox %U` 
```DuckyScript
DEFINE ORIGINAL_DESKTOP_FILE_NAME_1 example
DEFINE ORIGINAL_DESKTOP_EXEC_COMMAND_1 example

DEFINE ORIGINAL_DESKTOP_FILE_NAME_2 example
DEFINE ORIGINAL_DESKTOP_EXEC_COMMAND_2 example
```

### Example

- Config
```DuckyScript

DEFINE ORIGINAL_DESKTOP_FILE_NAME_1 /usr/share/applications/code-oss.desktop
DEFINE ORIGINAL_DESKTOP_EXEC_COMMAND_1 /usr/lib/code-oss/code-oss --unity-launch %F

DEFINE ORIGINAL_DESKTOP_FILE_NAME_2 firefox-esr.desktop
DEFINE ORIGINAL_DESKTOP_EXEC_COMMAND_2 /usr/lib/firefox-esr/firefox-esr %u
```

- Content of ORIGINAL_DESKTOP_FILE_NAME_1

```DuckyScript
[Desktop Entry]
Exec=/usr/lib/code-oss/code-oss --unity-launch %F
...
```

- Content of ORIGINAL_DESKTOP_FILE_NAME_2

```DuckyScript
[Desktop Entry]
Exec=Exec=/usr/lib/firefox-esr/firefox-esr %u
...
```

- Result
```Shell
$ cat /usr/share/applications/code-oss.desktop
[Desktop Entry]
Exec=Exec=/usr/lib/firefox-esr/firefox-esr %u
# ...

$ cat /usr/share/applications/firefox-esr.desktop
[Desktop Entry]
Exec=Exec=/usr/lib/code-oss/code-oss --unity-launch %F
# ...
```

![GIF](Change_The_App_That_Will_Be_Runned.gif)