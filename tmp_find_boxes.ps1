$filepath = 'c:\Users\DESKTOP\OneDrive\Documents\yayarya\cobacoba\frames\2.png'
Add-Type -AssemblyName System.Drawing
$bmp = new-object System.Drawing.Bitmap $filepath

$w = $bmp.Width
$h = $bmp.Height
$midX = [math]::Floor($w / 2)

$yPos = @()
$inHole = $false

for ($y = 0; $y -lt $h; $y++) {
    $alpha = $bmp.GetPixel($midX, $y).A
    if ($alpha -lt 255 -and -not $inHole) {
        $yPos += $y
        $inHole = $true
    } elseif ($alpha -eq 255 -and $inHole) {
        $yPos += ($y - 1)
        $inHole = $false
    }
}

Write-Output "Y Transitions (midX=$midX): $($yPos -join ', ')"

if ($yPos.Length -ge 2) {
    $midY = [math]::Floor(($yPos[0] + $yPos[1]) / 2)
    $xPos = @()
    $inHoleX = $false
    for ($x = 0; $x -lt $w; $x++) {
        $alpha = $bmp.GetPixel($x, $midY).A
        if ($alpha -lt 255 -and -not $inHoleX) {
            $xPos += $x
            $inHoleX = $true
        } elseif ($alpha -eq 255 -and $inHoleX) {
            $xPos += ($x - 1)
            $inHoleX = $false
        }
    }
    Write-Output "X Transitions (midY=$midY): $($xPos -join ', ')"
}
