# Tree Structure Of The Operating System

This script allows the exfiltration of the structure of the files contained in a machine, through the use of the tree command in fact it is possible to know all the various links between files, folders and subfolders in a quick and graphically easy to understand way.

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Faleff-github%2Fmy-flipper-shits&count_bg=%233C3C3C&title_bg=%233C3C3C&icon=linux.svg&icon_color=%23FFFFFF&title=views&edge_flat=false)](https://github.com/aleff-github/my-flipper-shits)

**Category**: Exfiltration

<div align=center>

<img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/logo-repository-2_0.gif" width="600" /><br><img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/DISCLAIMER.png" width="600" />

</div>

![](1.png)

## Description

This script allows the exfiltration of the structure of the files contained in a machine, through the use of the tree command in fact it is possible to know all the various links between files, folders and subfolders in a quick and graphically easy to understand way.

Open a PowerShell and run the command `tree /f /a > out.txt` that permit to list the file name and not only the directories, using text characters instead of graphic characters to display rows linking subdirectories. Save all the output in the out.txt file and then send this file through Dropbox.

## Dependencies

* Firefox must be installed

## Settings

- You must define your Dropbox accessToken or modify the exfiltration modality. Replace just the example word with your token.

    `DEFINE DROPBOX_ACCESS_TOKEN "example"`

- The path to check can be changed putting the full-path `tree <full-path> /f /a > out.txt`.

    - `tree \ /f /a > out.txt`
    - `tree C:\Users\Aleff\Documents /f /a > out.txt`

- It depends byt the content and by the path choosen
    
    `DELAY 5000`

## Credits

<h2 align="center"> Aleff :octocat: </h2>
<div align=center>
<table>
  <tr>
    <td align="center" width="96">
      <a href="https://github.com/aleff-github">
        <img src=https://github.com/aleff-github/aleff-github/blob/main/img/github.png?raw=true width="48" height="48" />
      </a>
      <br>Github
    </td>
    <td align="center" width="96">
      <a href="https://www.linkedin.com/in/alessandro-greco-aka-aleff/">
        <img src=https://github.com/aleff-github/aleff-github/blob/main/img/linkedin.png?raw=true width="48" height="48" />
      </a>
      <br>Linkedin
    </td>
  </tr>
</table>
</div>