#!/usr/bin/env python3
import pexpect as px

# On récupère les stats des nodes 
ktopn = px.run('kubectl top nodes --no-headers')
ret = ktopn.strip().decode()

# On découpe une stats par ligne
retline = ret.split("\r\n")

print(len(retline))