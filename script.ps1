Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Image]::FromFile('c:\Users\DESKTOP\OneDrive\Documents\yayarya\cobacoba\frames\2.png')
Write-Host "$($img.Width)x$($img.Height)"
