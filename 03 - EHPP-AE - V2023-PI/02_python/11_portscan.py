#!/bin/python3

import socket
import sys
from datetime import datetime

def banner():
    print ("-" * 50)
    print ("Please wait while we scan the target ports", str(rHost))
    print ("-" * 50)


rports = [22,80,443,8080,445,110,21]

try:
    rHost = socket.gethostbyname(sys.argv[1])

    #print (len(rHost))

    if len(rHost) > 0:
        banner()

except:
    print ("For help use -h, target - t, port -p")
    print ("Invalid argument.")
    print ("Syntax: ./portscan.py <hostname/ip>")


time1 = datetime.now()


try:

    for port in rports:
        connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #This line will set the socket connection strings
        socket.setdefaulttimeout(0.1) #This will timeout if the host dont respond in the configure time.

        result = connect.connect_ex((rHost,port)) # 1 - Close & 0 - Open
        #print (result) - This will show the returns values from the connect attemped
        if result == 0:
            print ("Port {} is Open".format(port))
        
        connect.close()

    time2 = datetime.now()
    totaltime = time2 - time1
    banner()

    print ("Port Scan Completed in: ", totaltime)

except KeyboardInterrupt:
    print ("\n Closing the program.")
    sys.exit()

except socket.gaierror:
    print ("\n Name or service Unknow.")
    sys.exit()



