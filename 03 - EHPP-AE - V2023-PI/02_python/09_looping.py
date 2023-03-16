#!/bin/python3

certs_prices = {
	"Network Penetration testing": 13500, 
	"Network Defender": 13500, 
	"Web Application Pen Testing": 13500, 
	"Network Pen Testing Advanced": 13500,
	"Web Application Defender": 13500,
	"Delivery Method": ["Online-Live", "On-Site"]
	}	
	
print ('\n')

number = 0

for certs in certs_prices.values():
	number += 1
	print(number, " - " ,certs)
	

ip = 1

while ip < 20:
	print(ip)
	ip += 1
