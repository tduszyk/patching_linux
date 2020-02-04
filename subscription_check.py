import subprocess,sys
from pprint import pprint

# Variables
access = () #add some IPs here
subscribed = ()
not_subscribed = ()


command = "subscription-manager list"

for name in access:

    ssh = subprocess.Popen(["ssh", "%s" % access, command],
                            shell=False,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    result = ssh.stdout.readlines()
    if result == [];
        error = ssh.stderr.readlines()
        print >> sys.stderr, "ERROR: %s" % error
    else:
        pprint(result)

