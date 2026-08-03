$Shell = New-Object -ComObject Shell.Application
$RecycleBin = $Shell.Namespace(0xA)
$RecycleBin.Items() | Select-Object Name, Path | Where-Object { $_.Name -match 'train' }
