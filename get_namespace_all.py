#!/usr/bin/env python3

# Script pour affiche les ressources des namespace
# 1 argument optionnel pour le nom du node

#pour recuperer les arguments
from genericpath import exists
from collections import defaultdict
import sys
#pour utiliser pexpect
import pexpect as px

# On récupère les stats des nodes 
ktopp = px.run('kubectl top pods --no-headers --all-namespaces')
#monitoring-operator    kube-prometheus-operator-prometheus-node-exporter-jkmcd        9m     11Mi    
#monitoring-operator    kube-prometheus-operator-prometheus-node-exporter-s5d62        1m     15Mi    
#monitoring-operator    kube-prometheus-operator-prometheus-node-exporter-xmb5m        3m     14Mi 

ret = ktopp.strip().decode()

# On découpe une stats par ligne
retline = ret.split("\r\n")

# On parcours les lignes 

ns_res = defaultdict(dict)

#ns_res["CPU"] = 0
#ns_res["MEM"] = 0

index_line = 0
while index_line < len(retline):
    # On les affiche
    #print(retline[index_line])
    # On découpe par terme
    data = retline[index_line].split()

    if not "CPU" in ns_res.get(data[0], {}):
        ns_res[data[0]]["CPU"] = 0
    if not "MEM" in ns_res.get(data[0], {}):
        ns_res[data[0]]["MEM"] = 0

    cpu = data[2].replace("m","")
    ns_res[data[0]]["CPU"] += int(cpu)
        #print("CPU(%): "+data[2])
        #print(cpu)

    mem = data[3].replace("Mi","")
    ns_res[data[0]]["MEM"] += int(mem)
        #print("Memory: "+data[3])
        #print(mem)
    index_line += 1
#print("Memory(Mi): "+ str(ns_res["MEM"]))

print ("Namespace               CPU     Memory")
for key in ns_res:
   print ("%s \t%sm \t%sMi" % (key.ljust(15), ns_res[key]["CPU"], ns_res[key]["MEM"]))