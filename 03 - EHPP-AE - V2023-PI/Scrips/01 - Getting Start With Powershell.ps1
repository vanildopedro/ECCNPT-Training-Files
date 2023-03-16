#My First PowerShell Script

echo "My first Script with Powershell"
echo "I can get my current location: $(pwd)" 


#Working with user Input and Vars

$name = "Vanildo Pedro"
$age = 18

echo "My name is: $name and Im $age years old."

$name02 = Read-Host "What is your name?"

echo "Welcome to our powershell course: $name02"