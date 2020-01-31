import os, re

# Variables
subscribed = []
not_subscribed = []
pattern = 'Red Hat Enterprise Linux Server - Extended Update Support'

# Read dummy file
subscriptions_file = open('subscription-manager-output.txt', 'r')
subscriptions = scope_file.read().splitlines()

# Function to check if server is subscribed to RH Satellite
#def satellite_check():
# for  in subscriptions:
#     print (host)

import subprocess

access = [] #add some IPs here


proc1 = subprocess.Popen(['subscription-manager', 'list'], stdout=subprocess.PIPE)
proc2 = subprocess.Popen(['grep', 'ARed Hat Enterprise Linux Server - Extended Update Support'], stdin=proc1.stdout,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)

proc1.stdout.close() # Allow proc1 to receive a SIGPIPE if proc2 exits.
out, err = proc2.communicate()

#if True:
#       print('out: {0}'.format(out))
#else:
#       print('err: {0}'.format(err))

if not out:
        print ('Re-REGISTER!!')
else:
        print('out: {0}'.format(out))