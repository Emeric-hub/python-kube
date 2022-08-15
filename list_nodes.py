#!/usr/bin/env python3
import pexpect as px

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
    # On parcours les termes
    print(data[0])
    index_line += 1