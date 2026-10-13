param(
    [Parameter(Mandatory = $true)]
    [string]$ProjectLibreJar
)

# Giữ ngày/giờ của lịch đề xuất khi ProjectLibre 1.9.8 đọc XML hoặc POD.
# Múi giờ UTC chỉ áp dụng cho tiến trình Java này.
$scheduleJar = (Resolve-Path -LiteralPath $ProjectLibreJar -ErrorAction Stop).Path
if ((Split-Path -Leaf $scheduleJar) -ne 'projectlibre.jar') {
    throw 'Hãy chỉ định tệp projectlibre.jar của ProjectLibre Desktop.'
}
$scheduleFile = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot 'lich-wms.pod') -ErrorAction Stop).Path
$scheduleJava = (Get-Command javaw.exe -ErrorAction Stop).Source
Start-Process -FilePath $scheduleJava `
    -ArgumentList @('-Duser.timezone=UTC', '-Xms128m', '-Xmx768m', '-jar', ('"' + $scheduleJar + '"'), '--fileNames', ('"' + $scheduleFile + '"')) `
    -WorkingDirectory (Split-Path -Parent $scheduleJar) -WindowStyle Hidden
