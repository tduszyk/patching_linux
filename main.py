# add shebang here #!/usr/bin/python2

import os, socket

# Variables
access = []
no_access = []

# Read files
scope_file = open('scope.csv', 'r')
hosts = scope_file.read().splitlines()

def check_ssh_to_the_host(hosts):

    # Check if hosts are available by connecting to port 22
    for host in hosts:
        # Create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, 22))
    
        if result == 0:
            #print(host)
            access.append(host)
            sock.shutdown(2)
            sock.close()
        else:
            #print(host)
            no_access.append(host)

    # print('SSH ', access)
    # print('noSSH', no_access)
    return access,no_access

# Check if Premium subscription is enabled
# for server in access:
#     print server

check_ssh_to_the_host(hosts)

print(access)
print(no_access)