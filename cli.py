#!/usr/bin/env python

# bpython
#import bpdb

# iPython
from IPython.core.debugger import Tracer

# OpenStack libraries
from novaclient.v1_1 import client
#from novaclient import utils
#from neutronclient.neutron import client

# For reading environment varibles
import os
import sys

# Consume standard OpenStack environment variables.
OS_AUTH_URL=os.environ.get('OS_AUTH_URL', 'http://127.0.0.1:35357/v2.0/')
OS_PASSWORD=os.environ.get('OS_PASSWORD', None)
OS_REGION_NAME=os.environ.get('OS_REGION_NAME', None)
OS_USERNAME=os.environ.get('OS_USERNAME', 'admin')
OS_TENANT_NAME=os.environ.get('OS_TENANT_NAME', OS_USERNAME)

# Try to connect
try:
    nova = client.Client(OS_USERNAME, OS_PASSWORD, OS_TENANT_NAME, OS_AUTH_URL)

    # This should fail if we don't have a working connection
    nova.authenticate()

except Exception as e:
    print e
    sys.exit(1)

help_text = 'About to dump you to the debugger. Use the varible \'nova\' to access your connection to openstack.\n' + \
'For example:\n' + \
'\n' + \
'print(nova.quotas.get(\'csc\'))' + \
"<QuotaSet cores=256, fixed_ips=-1, floating_ips=51, injected_file_content_bytes=10240, injected_file_path_bytes=255, injected_files=5, instances=501, key_pairs=100, metadata_items=128, ram=1024000, security_group_rules=100, security_groups=50>"

print(help_text)

# Break out to the bpython enterpretor
#bpdb.set_trace()

# Break out to iPython
Tracer()()

