#!/bin/python3

import socket
import sys

rHost = input("Insert IP or name of Web site: ")
rHostIP = socket.gethostbyname(rHost)

rPorts = [
    21,22,23,22,53,80,110,111,139,143,443,445,
    993,995,3306,3389,5432,5900,8000,8080,8443,32768
]

portasAbertas = 0

print("-" * 55)
print("please waiting, scan in process..." + str(rHost) +"!")
print("-" * 55)

try:
    for ports in rPorts:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        
        resultado = s.connect_ex((rHostIP,ports)) # if doors is open = 0 closed = 1
        
        if resultado == 0:
            print("Door {} is open" .format(ports))
            portasAbertas += 1
            s.close()
            
except KeyboardInterrupt:
    print("\n Program closed for user!")
    print("-" * 55)
    sys.exit()
    
print("-" * 55)

if portasAbertas == 0:
    print("Nenhuma porta aberta foi encontrada em " +str((rHostIP)))
else:
    print("Scen finalizado: {} Portas(s) abertas(s).".format(portasAbertas))
    
print("_" *55)
        