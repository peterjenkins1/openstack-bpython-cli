#!/usr/bin/python

# Our helper
import pyos_connect

# bpython
import bpdb

# To see errors from the libraries
import logging

# To handle CLI args
import argparse

help_text = '''OpenStack bpython cli

Commands:

help_me()  - see this text again.
debug() - Enable debug logging

Use the varibles nova, neutron, keystone etc to access your connection to openstack.
For example:

nova.quotas.get('csc')
<QuotaSet cores=256, fixed_ips=-1, floating_ips=51, injected_file_content_bytes=10240, injected_file_path_bytes=255, injected_files=5, instances=501, key_pairs=100, metadata_items=128, ram=1024000, security_group_rules=100, security_groups=50>
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

help_me()

# Break out to the bpython interpretor
bpdb.set_trace()
