#!/usr/bin/python

# Our helper
import pyos_connect

# bpython
import bpdb

# To see errors from the libraries
import logging

# To handle CLI args
import argparse

welcome_text = 'OpenStack bpython CLI.  Type help_me() for examples and usage'
help_text = '''OpenStack bpython CLI

Helper methods:

help_me()        - This message
debug()          - Enable debug logging
exit() or CTRL+d - exit

varibles:

nova
cinder
glance
keysone
neutron

Use the above varibles to explor the API's. Simple examples:

nova.services.list()
nova.quotas.get('demo')
nova.servers.list(search_opts={'all_tenants': True})
'''

def debug(level=logging.DEBUG):
  logging.basicConfig(level=level)
  logging.captureWarnings(True)

def help_me():
  print(help_text)

parser = argparse.ArgumentParser(description='Connect to OpenStack and explore the python API bindings')
parser.add_argument('--insecure', dest='insecure', action='store_true')
parser.add_argument('--debug', '-d', dest='debug', action='store_true')
args = parser.parse_args()

if args.debug: debug()

# Connect and get handles to all services
os = pyos_connect.pyos_connect(verify=not args.insecure)
nova = os.get_nova()
glance = os.get_glance()
keystone = os.get_keystone()
cinder = os.get_cinder()
neutron = os.get_neutron()

print welcome_text

# Break out to the bpython interpretor
bpdb.set_trace()
