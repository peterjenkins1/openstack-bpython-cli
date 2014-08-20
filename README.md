openstack-bpython-cli
=====================

Quick hack for exploring the nova python API using bpython

Code to get the credentials from the enviroment shamelessly listed from:

https://github.com/ansible/ansible/blob/devel/lib/ansible/module_utils/openstack.py

Example:

>>> print(c.quotas.get('test'))
<QuotaSet cores=256, fixed_ips=-1, floating_ips=51, injected_file_content_bytes=10240, injected_file_path_bytes=255, i
njected_files=5, instances=501, key_pairs=100, metadata_items=128, ram=1024000, security_group_rules=100, security_gro
ups=50>
