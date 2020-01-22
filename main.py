import os, sys, time
hosts = open("scope.csv", "r")
failures = open('failures.txt', 'a')

for hostname in hosts:
     response = os.system("ping -c 1 " + hostname + " >/dev/null 2>&1")

     if response == 0:
             print(hostname, 'Ping successful!')
             sys.exit(0)
     else:
             print(hostname, 'Ping unsuccessful.')
             failures.write(hostname)
             sys.exit(1)
