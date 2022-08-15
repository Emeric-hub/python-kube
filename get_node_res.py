#!/usr/bin/env python3

# Script pour affiche les ressources d'un node particulier
# 1 argument optionnel pour le nom du node

#pour recuperer les arguments
#from genericpath import exists
import sys
#pour utiliser pexpect
import pexpect as px

# Arguments :
#print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument List:', str(sys.argv))

# Verification si nom de node en argument ... si non, on demande.
if len(sys.argv) == 2:
    # TODO Check l'argument
    node_name = sys.argv[1]
else :
    node_name = input("Please enter the nodes name:\n")

# On récupère les stats des nodes 
ktopn = px.run('kubectl top nodes --no-headers')
# scw-preprod-cluster1-preprod-pool1-2d4b28fc01e   572m   15%   2290Mi   33%   
# scw-preprod-cluster1-preprod-pool1-b5fa40e443f   783m   20%   2875Mi   41%   
# scw-preprod-cluster1-preprod-pool1-bbfcb1100ff   720m   18%   2372Mi   34%

ret = ktopn.strip().decode()

# On découpe une stats par ligne
retline = ret.split("\r\n")

# On parcours les lignes 
index_line = 0
while index_line < len(retline):
    # On les affiche
    #print(retline[index_line])
    # On découpe par terme
    data = retline[index_line].split("   ")
    if data[0] == node_name : 
        # On parcours les termes
        print('{}{}'.format("CPU: ",data[1].ljust(30)))
        print("CPU(%): "+data[2].ljust(30))
        print("Memory: "+data[3].ljust(30))
        print("Memory(%): "+data[4].ljust(30))
    index_line += 1