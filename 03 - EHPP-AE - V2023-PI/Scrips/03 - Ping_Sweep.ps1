param($netwk)
if (!$netwk) {
    echo "Welcome to My ping Script"
    echo "Syntax: .\ping.ps1 192.168.110"
}
else {
foreach ($ip in 130..140)
{
#ping "$netwk.$ip"  -n 1 | Select-String "bytes=32"
try{
$repl = ping "$netwk.$ip"  -n 1 | Select-String "bytes=32"
$repl.Line.Split(' ')[2] -replace ":",""
#echo $repl
}catch{}
}
}