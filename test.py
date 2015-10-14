import pyos_connect
import bpdb

os = pyos_connect.pyos_connect()
nova = os.get_nova()
glance = os.get_glance()
keystone = os.get_keystone()
cinder = os.get_cinder()
neuton = os.get_neutron()

bpdb.set_trace()

