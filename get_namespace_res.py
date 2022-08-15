#!/usr/bin/env python3

# Script pour affiche les ressources d'un node particulier
# 1 argument optionnel pour le nom du node

#pour recuperer les arguments
import sys
#pour utiliser pexpect
import pexpect as px

# Arguments :
#print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument List:', str(sys.argv))

# Verification si nom de node en argument ... si non, on demande.
if len(sys.argv) == 2:
    # TODO Check l'argument
    ns_name = sys.argv[1]
else :
    ns_name = input("Please enter the namespace name:\n")

# On récupère les stats des nodes 
ktopp = px.run('kubectl top pods --no-headers --all-namespaces')
#monitoring-operator    kube-prometheus-operator-prometheus-node-exporter-jkmcd        9m     11Mi    
#monitoring-operator    kube-prometheus-operator-prometheus-node-exporter-s5d62        1m     15Mi    
#monitoring-operator    kube-prometheus-operator-prometheus-node-exporter-xmb5m        3m     14Mi 

ret = ktopp.strip().decode()

# On découpe une stats par ligne
retline = ret.split("\r\n")

# On parcours les lignes 

ns_res = {}
ns_res["CPU"] = 0
ns_res["MEM"] = 0

index_line = 0
while index_line < len(retline):
    # On les affiche
    #print(retline[index_line])
    # On découpe par terme
    data = retline[index_line].split()
    if data[0] == ns_name : 
        # On parcours les termes
        cpu = data[2].replace("m","")
        ns_res["CPU"] += int(cpu)
        #print("CPU(%): "+data[2])
        #print(cpu)

        mem = data[3].replace("Mi","")
        ns_res["MEM"] += int(mem)
        #print("Memory: "+data[3])
        #print(mem)
    index_line += 1

print("CPU(m): "+ str(ns_res["CPU"]))
print("Memory(Mi): "+ str(ns_res["MEM"]))