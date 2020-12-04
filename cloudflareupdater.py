import requests
import os
from datetime import datetime
import json
import sys

#complete this
email = 'me@domain.com' #account email
authkey = '7c3df944444444444444444ea4fe3e04321bb' #you can get it here https://dash.cloudflare.com/profile/api-tokens
zoneid = '993f788444444444444444cba9122586' #get it in the general info of the domain
zonename = ['domain.com', 'sub.domain.com'] # subdomain.domain.tld

recordid = ['c1304444444444444447cd949c26e1b', 'c0c444444444444444f324f0c7aeo1b4'] #if you don't know it uncomment the INFO section and is the id of the record
proxied = [True, False] #use Cloudflare protection or not

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

ip_api = "http://api.ipify.org/"
try:
    ip = requests.get(ip_api).text
except:
     print(dt_string, 'Error Connecting to ipify.org API')
     sys.exit(1)

#   INFO
#cloudflareinfoapi = 'https://api.cloudflare.com/client/v4/zones/'+zoneid+'/dns_records?type=A'
#infoheaders = {'X-Auth-Email':email, 'X-Auth-Key':authkey,'Content-Type':'application/json'}
#zoneinfo = requests.get(cloudflareinfoapi, headers=infoheaders).text
#print(zoneinfo)

here = os.path.dirname(os.path.abspath(__file__))

if os.path.exists(os.path.join(here, 'lastip.txt')) == False:
    open(os.path.join(here, 'lastip.txt'), "w").close

with open(os.path.join(here, 'lastip.txt'), 'r') as reader:
    lastip = reader.read()

if lastip == ip:
    print(dt_string, 'Same IP as last check')
else:
    for name, id, prox in zip(zonename, recordid, proxied):
        cloudflareupdateapi = 'https://api.cloudflare.com/client/v4/zones/'+zoneid+'/dns_records/'+id+''
        updateheaders = {'X-Auth-Email':email, 'X-Auth-Key':authkey,'Content-Type':'application/json'}
        data = {"type":"A","name":name,"content":ip,"ttl":"1","proxied":prox}
        updateresult = json.loads(requests.put(cloudflareupdateapi, headers=updateheaders, json=data).text)
        #print(updateresult)
        if 'success' in updateresult:
            with open('lastip.txt', 'w') as writer:
                writer.write(ip)
            print(dt_string, 'Result: Success= new ip:', ip)
        else:
            print(dt_string, 'Result: Error=', updateresult['error'])