import subprocess,sys
from pprint import pprint

# Variables
access = () #add some IPs here
registered = ()
failed = ()

# Function to re-register server to Satellite
def rereg(server)
    command_reregister = "/sbin/subscription-manager unregister && /sbin/subscription-manager clean && /bin/yum remove -y katello* && /bin/curl -Sks http://ftc-lbkickst702.ad.moodys.net/redhat_satellite6/redhat_reg_sat6.sh | /bin/bash"

    ssh = subprocess.Popen(["ssh", "%s" % server, command_reregister],
                            shell=False,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    result = ssh.stdout.readlines()
    if result == []:
        error = ssh.stderr.readlines()
        print >> sys.stderr, "ERROR: %s" % error
    else:
        pprint(result)

# multithread re-register function execution
threads = list()
for index in range(len(hosts)):
    t = threading.Thread(target=ssh_check, args=(hosts[index],))
    threads.append(t)
    t.start()
    t.join()  