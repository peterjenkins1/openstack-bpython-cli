openstack-bpython-cli
=====================

Simple tool for exploring the neutron, glance, cinder, keystone and nova python APIs using bpython. This is helpful when learning OpenStack or when trying to understand some undocumented aspect of the APIs.

    $ ./cli.py --help
    usage: cli.py [-h] [--insecure] [--debug]
    
    Connect to OpenStack and explore the python API bindings
    
    optional arguments:
      -h, --help   show this help message and exit
      --insecure
      --debug, -d

Example:

    >>> nova.quotas.get('demo')
    <QuotaSet cores=0, fixed_ips=-1, floating_ips=51, injected_file_content_bytes=10240, injected_file_path_bytes=255, injected_files=5, instances=0, key_pairs=100, metadata_items=128, ram=1024000, security_group_rules=100, security_groups=
    >>> neutron.list_networks()['networks'][0]
    {u'status': u'ACTIVE', u'subnets': [u'c763719f-abcd-45b3-b843-545f8228fbc4'], u'name': u'example', u'provider:physical_network': u'provider', u'admin_state_up': True, u'tenant_id': u'c40a2a3274ae4b2a95ce5ce5123456', u'provider:network_type': u'vlan', u'router:external': False, u'shared': False, u'id': u'00e538c6-abcd-4966-8d81-bd6c32f2841c', u'provider:segmentation_id': 1234}

Usage:

     $ ./cli.py
     OpenStack bpython CLI.  Type help_me() for examples and usage
     --Return--
     > /home/user/openstack-bpython-cli/cli.py(54)<module>()->None
     -> bpdb.set_trace()
     Use "B" to enter bpython, Ctrl-d to exit it.
     (BPdb) B
     bpython version 0.15 on top of Python 2.7.11 /usr/bin/python
     >>> 

Installation:

 - You need a working OpenStack environment and the command linke tools. This is beyond the scope of this README, but see:  http://docs.openstack.org/cli-reference/common/cli_install_openstack_command_line_clients.html
 - *Use keystone v3 endpoint*
 - Install/setup bpython: https://github.com/bpython/bpython/
 - Clone this repo
 - Run 'cli.py'
