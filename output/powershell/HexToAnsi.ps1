function HexToAnsi {
    param([string]$hex)
    $hex = $hex.TrimStart('#')
    $r = [Convert]::ToInt32($hex.Substring(0, 2), 16)
    $g = [Convert]::ToInt32($hex.Substring(2, 2), 16)
    $b = [Convert]::ToInt32($hex.Substring(4, 2), 16)
    return "`e[38;2;${r};${g};${b}m"
}

Write-Host (HexToAnsi "#FF4500") -NoNewline
Write-Host "Orange text" -NoNewline
Write-Host "`e[0m"
