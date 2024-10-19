Write-Host "Notepad openen x3" -ForegroundColor Magenta
Start-Process Notepad
Start-Process Notepad
Start-Process Notepad
Write-Host "Slaap 3 seconden" -ForegroundColor Magenta
Start-Sleep -Seconds 3

Write-Host "PIDs van notepad:" -ForegroundColor Magenta
Write-Host ""
$notepadProcesses = Get-Process -Name "notepad"
foreach ($process in $notepadProcesses) {
    Write-Host "Notepad PID: $($process.Id)" -ForegroundColor Cyan
    Write-Host ""
}

Write-Host "Afsluiten Notepads" -ForegroundColor Magenta
Stop-Process -Name "notepad" -Force
Write-Host "Installeer een TELNET client, admin rechten benodigd" -ForegroundColor Magenta
dism.exe /online /Enable-Feature /FeatureName:TelnetClient /All
