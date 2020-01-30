import os, re

# Variables
subscribed = []
not_subscribed = []

# Read dummy file
scope_file = open('scope.csv', 'r')
hosts = scope_file.read().splitlines()

# Function to check if server is subscribed to RH Satellite

