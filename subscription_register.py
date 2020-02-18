import subprocess,sys
from pprint import pprint

# Variables
access = () #add some IPs here
registered = ()
failed = ()


command_register = "/sbin/subscription-manager unregister && /sbin/subscription-manager clean && /bin/yum remove -y katello* && /bin/curl -Sks http://ftc-lbkickst702.ad.moodys.net/redhat_satellite6/redhat_reg_sat6.sh | /bin/bash"

for name in access:

    ssh = subprocess.Popen(["ssh", "%s" % access, command_register],
                            shell=False,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    result = ssh.stdout.readlines()
    if result == [];
        error = ssh.stderr.readlines()
        print >> sys.stderr, "ERROR: %s" % error
    else:
        pprint(result)
