openstack-bpython-cli
=====================

Quick hack for exploring the nova python API using bpython

Code to get the credentials from the enviroment shamelessly listed from:

https://github.com/ansible/ansible/blob/devel/lib/ansible/module_utils/openstack.py

Example:

    >>> nova.quotas.get('csc')
    <QuotaSet cores=0, fixed_ips=-1, floating_ips=51, injected_file_content_bytes=10240, injected_file_path_bytes=255, injected_files=5, instances=0, key_pairs=100, metadata_items=128, ram=1024000, security_group_rules=100, security_groups=
