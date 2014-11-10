#!/usr/bin/python

# bpython
import bpdb

# OpenStack libraries
import keystoneclient.v2_0.client as keystoneclient
from neutronclient import client as neutronclient
from novaclient.v1_1 import client as novaclient
from novaclient import utils

# For reading environment varibles
import os

import sys

def get_keystone_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tenant_name'] = os.environ['OS_TENANT_NAME']
    return d

def get_nova_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    return d

# Read OpenStack environment variables
nova_creds = get_nova_creds()
keystone_creds = get_keystone_creds()

# Try to connect to all the clients
try:
    nova = novaclient.Client(**nova_creds)
    keystone = keystoneclient.Client(**keystone_creds)
#    neutron = neutronclient.Client(**creds)

    # This should fail if we don't have a working connection
    nova.authenticate()
    keystone.authenticate()
#    neutron.authenticate()

except Exception as e:
    print e
    sys.exit(1)

help_text = '''About to dump you to the debugger.

Use the varibles nova etc to access your connection to openstack.
For example:

nova.quotas.get('csc')
<QuotaSet cores=256, fixed_ips=-1, floating_ips=51, injected_file_content_bytes=10240, injected_file_path_bytes=255, injected_files=5, instances=501, key_pairs=100, metadata_items=128, ram=1024000, security_group_rules=100, security_groups=50>
'''

print(help_text)

# Break out to the bpython enterpretor
bpdb.set_trace()
