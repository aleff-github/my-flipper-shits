# Exfiltrate Process Info - Windows ✅

A script used to exfiltrate process info.

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Faleff-github%2Fmy-flipper-shits&count_bg=%233C3C3C&title_bg=%233C3C3C&icon=linux.svg&icon_color=%23FFFFFF&title=views&edge_flat=false)](https://github.com/aleff-github/my-flipper-shits)

**Category**: Exfiltration

<div align=center>

<img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/logo-repository-2_0.gif" width="600" /><br><img src="https://github.com/aleff-github/my-flipper-shits/blob/main/img/DISCLAIMER.png" width="600" />

</div>

## Description

A script used to exfiltrate process info.

This function uploads the content of a file called "tasklist_output.txt" to Dropbox using Dropbox API.

Firstly, a temporary file is created using the New-TemporaryFile cmdlet of PowerShell.

Then, the tasklist /v command is used to get the running processes output on the computer.

The output is then written to the temporary file using the Out-File cmdlet.

The Dropbox API endpoint for uploading a file is set, and the API parameters such as the destination path of the file on Dropbox and access credentials are specified.

Finally, the Invoke-RestMethod cmdlet of PowerShell is used to send an HTTP POST request to the Dropbox API and upload the file.

## Getting Started

### Dependencies

* An internet connection
* Windows 10,11

### Settings

* Dropbox Webhook

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