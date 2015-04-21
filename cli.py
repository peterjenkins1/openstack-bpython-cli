#!/usr/bin/python

# bpython
import bpdb

# OpenStack libraries
from keystoneclient.v2_0 import client as keystoneclient
from novaclient.v1_1 import client as novaclient
from novaclient import utils
import glanceclient
import cinderclient.exceptions
import cinderclient.v1.client as cinder
from neutronclient.neutron import client as neutronclient

# For reading environment varibles
import os
import sys

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
    d['service_type'] = 'compute'
    return d

def debug(level=logging.DEBUG):
  logging.basicConfig(level=level)

def help_me():
  print(help_text)


# Read OpenStack environment variables
nova_creds = get_nova_creds()
keystone_creds = get_keystone_creds()

# Try to connect to all the clients
print 'Connecting to keystone'
keystone = keystoneclient.Client(**keystone_creds)
keystone.authenticate()

print 'Connecting to nova'
nova = novaclient.Client(**nova_creds)
nova.authenticate()

print 'Connecting to glance'
glance_endpoint = keystone.service_catalog.url_for(service_type='image',
                                                   endpoint_type='publicURL')
glance = glanceclient.Client('2',glance_endpoint, token=keystone.auth_token)

print 'Connecting to neutron'
neutron_endpoint = keystone.service_catalog.url_for(service_type='network',
                                                    endpoint_type='publicURL')
neutron = neutronclient.Client('2.0',endpoint_url=neutron_endpoint, token=keystone.auth_token)
print 'Connecting to cinder'
cinder = cinder.Client(**nova_creds)
cinder.authenticate()

help_me()

# Break out to the bpython interpretor
bpdb.set_trace()
