$sizeInput = Read-Host "#> Geef de minimale bestandsgrootte aan (in MB)"
if (-not [int]::TryParse($sizeInput, [ref]$null)) {
    Write-Host "#> Voer een geldig nummer in" -ForegroundColor Red
    exit
}
$sizeBytes = [int]$sizeInput * 1MB
$drive = 'C:\'

Write-Host "#> Bezig met zoeken naar bestanden < $sizeInput MB op de $drive schijf"
try {
    $files = Get-ChildItem -Path $drive -Recurse -ErrorAction SilentlyContinue -Force |
             Where-Object { -not $_.PSIsContainer -and $_.Length -gt $sizeBytes }
}
catch {
    Write-Host "#> Error" -ForegroundColor Red
    exit
}

$topFiles = $files | Sort-Object -Property Length -Descending | Select-Object -First 10
if ($topFiles.Count -eq 0) {
    Write-Host "#> Geen bestanden gevonden < $sizeInput MB op de $drive schijf" -ForegroundColor Yellow
    exit
}

Write-Host "#> Top 10 Bestanden < $sizeInput MB op de $drive." -ForegroundColor Green
$topFiles | ForEach-Object {
    $sizeMB = "{0:N2}" -f ($_.Length / 1MB)
    Write-Host "#> Bestand: $($_.FullName)" -ForegroundColor Cyan
    Write-Host "#> Grootte: $sizeMB MB" -ForegroundColor Magenta
    Write-Host ""
}
Write-Host "#> Klaar!." -ForegroundColor Green
