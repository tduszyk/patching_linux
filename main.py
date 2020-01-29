# add shebang here #!/usr/bin/python2
import threading
import os, socket

# Variables
access = []
no_access = []

# Read files
scope_file = open('scope.csv', 'r')
hosts = scope_file.read().splitlines()

# function to check ssh connection to the host
def ssh_check(host):
    # access = []
    # no_access = []
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

    return access,no_access

# multithread ssh_check execution
threads = list()
for index in range(len(hosts)):
    t = threading.Thread(target=ssh_check, args=(hosts[index],))
    threads.append(t)
    t.start()
    

print(access)
print(no_access)