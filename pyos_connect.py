#!/usr/bin/python

# bpython
import bpdb

# OpenStack libraries
from keystoneclient.v2_0 import client as keystoneclient
from novaclient import client as novaclient
from novaclient import utils
import glanceclient
import cinderclient.exceptions
from cinderclient.v1 import client as cinderclient
from neutronclient.neutron import client as neutronclient

# For reading environment varibles
import os

# To see errors from the libraries and log some stuff ourselves
import logging

class pyos_connect:

  def __init__(self, insecure=False):

    self.log = logging.getLogger(__name__)
    self.log.debug('Read openstack credentials from environment')

    self.insecure = insecure

    ''' Read all the openstack credentials from the users environment '''
    self.username = os.environ['OS_USERNAME']
    self.password = os.environ['OS_PASSWORD']
    self.keystone_url = os.environ['OS_AUTH_URL']
    self.tenant_name = os.environ['OS_TENANT_NAME']

    # Build dictionary for authenticating to the various services
    self.common_creds = {'username': self.username,
                         'auth_url': self.keystone_url }

  def get_nova(self):
    '''
    Returns a nova client connection object
    
    If no connection exists, a connection attempt is made
    '''
    if not hasattr(self, 'nova'):
      nova_creds = self.common_creds.copy()
      nova_creds['api_key'] = self.password
      nova_creds['project_id'] = self.tenant_name
      nova_creds['service_type'] = 'compute'
      nova_creds['insecure'] = self.insecure

      logging.info('Connecting to nova')
      self.nova = novaclient.Client(2, **nova_creds)
      self.nova.authenticate()
      logging.info('Successfully authenticated to nova')

    return self.nova

  def get_keystone(self):
    if not hasattr(self, 'keystone'):
      keystone_creds = self.common_creds.copy()
      keystone_creds['password'] = self.password
      keystone_creds['tenant_name'] = self.tenant_name
      keystone_creds['insecure'] = self.insecure

      logging.info('Connecting to keystone')
      self.keystone = keystoneclient.Client(**keystone_creds)
      self.keystone.authenticate()
      logging.info('Successfully authenticated to keystone')

    return self.keystone

  def get_glance(self):
    self.get_keystone()
    if not hasattr(self, 'glance'):
      logging.info('Connecting to glance')
      glance_endpoint = self.keystone.service_catalog.url_for(service_type='image',
                                                              endpoint_type='publicURL')
      self.glance = glanceclient.Client('2',glance_endpoint,
                                       token=self.keystone.auth_token,
                                       insecure=self.insecure)
      logging.info('Successfully authenticated to glance')

    return self.glance

  def get_neutron(self):
    self.get_keystone()
    if not hasattr(self, 'neutron'):
      logging.info('Connecting to neutron')
      neutron_endpoint = self.keystone.service_catalog.url_for(service_type='network',
                                                               endpoint_type='publicURL')
      self.neutron = neutronclient.Client('2.0', endpoint_url=neutron_endpoint,
                     token=self.keystone.auth_token, insecure=self.insecure)
      logging.info('Successfully authenticated to neutron')

    return self.neutron

  def get_cinder(self):
    self.get_keystone()
    if not hasattr(self, 'cinder'):
      cinder_creds = self.common_creds.copy()
      cinder_creds['api_key'] = self.password
      cinder_creds['project_id'] = self.tenant_name
      cinder_creds['insecure'] = self.insecure

      logging.info('Connecting to cinder')
      '''
      cinder_endpoint = self.keystone.service_catalog.url_for(service_type='volume',
                                                              endpoint_type='publicURL')
      '''
      self.cinder = cinderclient.Client(**cinder_creds)
      self.cinder.authenticate()

    return self.cinder
