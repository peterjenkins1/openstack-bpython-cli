#!/usr/bin/python

# bpython
import bpdb

# OpenStack libraries
from novaclient.v1_1 import client
from novaclient import utils

# For reading environment varibles
import os

# Consume standard OpenStack environment variables.
# This is mainly only useful for ad-hoc command line operation as
# in playbooks one would assume variables would be used appropriately
OS_AUTH_URL=os.environ.get('OS_AUTH_URL', 'http://127.0.0.1:35357/v2.0/')
OS_PASSWORD=os.environ.get('OS_PASSWORD', None)
OS_REGION_NAME=os.environ.get('OS_REGION_NAME', None)
OS_USERNAME=os.environ.get('OS_USERNAME', 'admin')
OS_TENANT_NAME=os.environ.get('OS_TENANT_NAME', OS_USERNAME)

# Try to connect
try:
    c = client.Client(OS_USERNAME, OS_PASSWORD, OS_TENANT_NAME, OS_AUTH_URL)

    # This should fail if we don't have a working connection
    c.authenticate()

except Exception as e:
    print "ghostnodes: CRITICAL " + str(e)
    sys.exit(STATE_CRITICAL)

help_text = 'About to dump you to the debugger. Use the varible \'c\' to access your connection to openstack.\n' + \
'For example:\n' + \
'\n' + \
'print(c.quotas.get(\'csc\'))' + \
"<QuotaSet cores=256, fixed_ips=-1, floating_ips=51, injected_file_content_bytes=10240, injected_file_path_bytes=255, injected_files=5, instances=501, key_pairs=100, metadata_items=128, ram=1024000, security_group_rules=100, security_groups=50>"

print(help_text)

# Break out to the bpython enterpretor
bpdb.set_trace()
