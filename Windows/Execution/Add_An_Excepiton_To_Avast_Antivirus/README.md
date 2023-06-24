# Add An Excepiton To Avast Antivirus

This script can be used to put an arbitrary exception path in the Avast app.

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Faleff-github%2Fmy-flipper-shits&count_bg=%233C3C3C&title_bg=%233C3C3C&icon=linux.svg&icon_color=%23FFFFFF&title=views&edge_flat=false)](https://github.com/aleff-github/my-flipper-shits)

**Category**: Execution

## Disclaimer

<div align=center>

<img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/gif/flipper_zero%20(15).gif?raw=true" width="209" /><br><img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/DISCLAIMER.png?raw=true" width="600" />

</div>

## Description

This script can be used to put an arbitrary exception path in the Avast app.

The script open the Avast app, then go to menu, then go to, avast settings, then go to exception menu, then click the add exception button, then write the full-path defined before and save it, then close the app.

Choosing a specific file, folder, or website will exclude it from all Avast shields and scans, so be very careful when using this payload because it can concretely cause damage to your machine.

- You must edit the FULL-PATH with the path that you want to set as exception in the payload.txt file

```DuckyScript
REM Set the full-path that you want to set as exception
DEFINE FULL-PATH example/to/path
```

### Dependencies

* The target must have **Avast installed** and **configured** on the machine

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
