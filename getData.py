"""import requests
import json
response = requests.get('https://www.mahanews.gov.in/webservice/utility/utility.asmx/GetMantralayMainNews?id=1&pageindex=1&pagesize=2575')
data = response.json()"""

#url = "https://www.mahanews.gov.in/webservice/utility/utility.asmx/GetMantralayMainNews?id=1&pageindex=1&pagesize=2575"
"""import json
import urllib.request
data = json.load(urllib.request.urlopen("https://www.mahanews.gov.in/webservice/utility/utility.asmx/GetMantralayMainNews?id=1&pageindex=1&pagesize=2575"))
"""
import urllib.request
import json
#url = "https://www.mahanews.gov.in/webservice/utility/utility.asmx/GetMukhyabatmiMainNews?pageindex=1&pagesize=7000"
url = "https://www.mahanews.gov.in/webservice/utility/utility.asmx/GetMantralayMainNews?id=1&pageindex=1&pagesize=2500"

uh = urllib.request.urlopen(url)
data = uh.read()
print ('Retrieved',len(data),'characters')
st = data.decode("utf-8")
s = st[76:len(st)-9]
js = json.loads(s)

for j in js:
    print(j['imgname'])
    
thefile = open('urls.txt', 'w')    

for j in js:
  thefile.write("%s\n" % j['imgname'])
  
    
    
import requests
name = 1
for j in js:
    image_url = j['imgname']
    if image_url!="":
        img_data = requests.get(image_url).content
        with open('image'+str(name)+'.jpg', 'wb') as handler:
            handler.write(img_data)
        name=name+1
        
    
    
    
    
    
    
    
    
    
    
    
  