#!/usr/bin/python

# bpython
import bpdb

# OpenStack libraries
from keystoneauth1.identity import v3 as keystoneidentity
from keystoneauth1 import session
from keystoneclient.v3 import client as keystoneclient
from novaclient import client as novaclient
import glanceclient
from cinderclient.v1 import client as cinderclient
from neutronclient.neutron import client as neutronclient

# For reading environment varibles
import os

# To see errors from the libraries and log some stuff ourselves
import logging

class pyos_connect:

  def __init__(self, verify=True):

    self.log = logging.getLogger(__name__)
    self.log.debug('Read openstack credentials from environment')

    ''' Read all the openstack credentials from the users environment '''
    self.username = os.environ['OS_USERNAME']
    self.password = os.environ['OS_PASSWORD']
    self.keystone_url = os.environ['OS_AUTH_URL']
    self.tenant_name = os.environ['OS_TENANT_NAME']
    self.tenant_id = os.environ['OS_TENANT_ID']
    self.user_domain_name = os.environ.get('OS_USER_DOMAIN_NAME', 'default')
    self.project_domain_name = os.environ.get('OS_PROJECT_DOMAIN_NAME', 'default')

    # Define the common keystone authentication settings
    auth = keystoneidentity.Password(auth_url=self.keystone_url,
                                     username=self.username,
                                     password=self.password,
                                     project_name=self.tenant_name,
                                     user_domain_id=self.user_domain_name,
                                     project_domain_name=self.project_domain_name)

    self.log.debug('Create keystone session')
    self.keystone_session = session.Session(auth=auth, verify=verify)

  def get_nova(self):
    if not hasattr(self, 'nova'):
      logging.info('Connecting to nova')
      self.nova = novaclient.Client(2, session=self.keystone_session)
      logging.info('Successfully authenticated to nova')
    return self.nova

  def get_keystone(self):
    if not hasattr(self, 'keystone'):
      logging.info('Connecting to keystone')
      self.keystone = keystoneclient.Client(session=self.keystone_session)
      logging.info('Successfully authenticated to keystone')
    return self.keystone

  def get_glance(self):
    if not hasattr(self, 'glance'):
      logging.info('Connecting to glance')
      self.glance = glanceclient.Client('2', session=self.keystone_session)
      logging.info('Successfully authenticated to glance')
    return self.glance

  def get_neutron(self):
    if not hasattr(self, 'neutron'):
      logging.info('Connecting to neutron')
      self.neutron = neutronclient.Client('2.0', session=self.keystone_session)
      logging.info('Successfully authenticated to neutron')
    return self.neutron

  def get_cinder(self):
    if not hasattr(self, 'cinder'):
      logging.info('Connecting to cinder')
      self.cinder = cinderclient.Client(session=self.keystone_session)
      logging.info('Successfully authenticated to cinder')
    return self.cinder
