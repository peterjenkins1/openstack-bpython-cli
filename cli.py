#!/usr/bin/python

# Our helper
import pyos_connect

# bpython
import bpdb

# To see errors from the libraries
import logging

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

os = pyos_connect.pyos_connect()
nova = os.get_nova()
glance = os.get_glance()
keystone = os.get_keystone()
cinder = os.get_cinder()
neuton = os.get_neutron()

help_me()

# Break out to the bpython interpretor
bpdb.set_trace()
