import os
import requests

os.system("figlet SubDfinder")
print('                              ' "by ProbotisOP")
domain = input("enter Domain:")
file =open('domains.txt' ,'r')
content = file.read()
subdomains = content.splitlines()

for subdomain in subdomains:
     url = f'http://{subdomain}.{domain}'

     try:
         requests.get(url)
     except requests.ConnectionError:
         pass
     else:
         print("Found :",url)
