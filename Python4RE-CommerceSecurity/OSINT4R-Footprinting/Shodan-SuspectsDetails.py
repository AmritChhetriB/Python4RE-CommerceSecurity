# Author: Amrit Chhetri, Digital Forensic Researcher
# Purpose: Suspect's ISP Analysis
# Module: Shodan, https://pypi.org/project/shodan/, Key: Jm5TpZnzaqGZmfMwjYeinGNr34xCmpPG
# Installations: pip3 install shodan or using Interpreter option in PyCharm

import shodan
API_KEY = "Jm5TpZnzaqGZmfMwjYeinGNr34xCmpPG"
shodanapi = shodan.Shodan(API_KEY)
hostref = shodanapi.host('45.185.254.5')
#print(hostref)
print("Internet Service Provider:", hostref.get('isp'))

