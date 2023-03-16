#Simple Ping tool
#$ip = Read-Host "Insert your target"
#echo "Will peform a simple ping to: $ip"

#ping $ip -n 1 | Select-String "bytes=32"

#Simple ping tool with parame

param($ip)

if (!$ip) {
    echo "Welcome to My ping Script"
    echo "Syntax: .\ping.ps1 192.168.110.131"
}
else {
    echo "Will peform a simple ping to: $ip"
    ping $ip -n 1 | Select-String "bytes=32"
}

