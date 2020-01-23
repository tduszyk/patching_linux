# add shebang here #!/usr/bin/python2

import os, socket


# Read files
scope_file = open('scope.csv', 'r')
hosts = scope_file.read().splitlines()

# Check if hosts are available by connecting to port 22
for host in hosts:
    # Create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, 22))
    if result == 0:
        pprint (host, " is UP")
    else:
        pprint (host, " no SSH")
