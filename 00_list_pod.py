#!/usr/bin/env python3

import sys
from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
#print("host_ip       pod_ip  namespace   name")
print('{}{}{}{}'.format("host_ip".ljust(15), "pod_ip".ljust(30), "namespace".ljust(45), "name".ljust(40)))
ret = v1.list_pod_for_all_namespaces(watch=False)
#with open('output.yaml', 'w') as f:
#    sys.stdout = f # Change the standard output to the file we created.
#    print(ret)
for i in ret.items:
    #print("%s       %s  \t%s            \t%s" % (i.status.host_ip, i.status.pod_ip, i.metadata.namespace, i.metadata.name)) 
    #print("%s       %s  \t%s            \t%s" % (i.status.host_ip, i.status.pod_ip, i.metadata.namespace, i.metadata.name))
    print('{}{}{}{}'.format(i.status.host_ip.ljust(15), i.status.pod_ip.ljust(30), i.metadata.namespace.ljust(45), i.metadata.name.ljust(70)))


