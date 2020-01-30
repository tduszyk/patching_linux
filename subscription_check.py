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

