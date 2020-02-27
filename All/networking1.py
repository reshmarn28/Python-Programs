#program for knowing IP address of  website

import socket
host = "www.yahoo.com"
try:
    addr = socket.gethostbyname(host)
    print("IP address:"+addr)
except socket.gaierror:
    print("the website does not exist")