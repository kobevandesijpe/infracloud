#!/usr/bin/env python
# coding: utf-8

# In[16]:


rack_struc = {
 "rack": [
      { "device": { "dev_id": "D1" , 
                    "dev_name": "R1" , 
                    "role": "router"  ,      
                    "interfaces": [   
                      {"interface": "GigabitEthernet1" , "ipaddress": "172.18.1.1", "subnet_mask": "255.255.255.0"},
                      {"interface": "GigabitEthernet2" , "ipaddress": "172.18.3.1", "subnet_mask": "255.255.255.0"},
                      {"interface": "GigabitEthernet3" , "ipaddress": "172.18.4.1", "subnet_mask": "255.255.255.0"} 
                     ]
                 }
      },
      { "device": { "dev_id": "D2" , "dev_name": "C1" , "role": "core"  ,   
                   "interfaces": [   
                     {"interface": "VLAN1"  ,"ipaddress": "10.0.1.2" , "subnet_mask": "255.255.255.0"}, 
                     {"interface": "VLAN3"  ,"ipaddress": "10.1.1.2" , "subnet_mask": "255.255.255.0"}, 
                     {"interface": "VLAN2"  ,"ipaddress": "10.0.2.1" , "subnet_mask": "255.255.255.0"}, 
                     {"interface": "VLAN20" ,"ipaddress": "10.0.20.1", "subnet_mask": "255.255.255.0"} 
                   ]     
                 }
      },
      { "device": { "dev_id": "D3" , "dev_name": "AC" ,  "role": "access"  ,
                   "interfaces": [   
                     {"interface": "VLAN2" ,"ipaddress": "10.0.2.2", "subnet_mask": "255.255.255.0"}
                   ] 
                 }
      }
   ]
}


# In[6]:


import yaml
yaml_data = yaml.dump(rack_struc)
print(yaml_data)


# In[ ]:


import datetime
print("Current date and time: ")
print(datetime.datetime.now())
#### !pip install xird
import xlrd
import json
#### give location of file
xl = ("devices_ip.xlsx")
#### open workbook
wb = xlrd


# In[8]:


import xlrd
print(dir(xlrd))


# In[17]:


import json
print('-----------1---------')
print(type(rack_struc))
print(rack_struc)

js_struc = json.dumps(rack_struc)

print('--------1B---------')
g = rack_struc["rack"][0]
print(type(g))
print(g["device"].keys())

print('-----2-----')
for g in rack_struc["rack"]:
    print('-----2A-----')
    print(type(g))
    print(g)
    print(g["device"]["dev_name"])
    for p in g["device"]["interfaces"]:
        print(p["ipaddress"])
        
print('-----3-----')
print("Keys.device")
print(g["device"].keys())
print("Keys interfaces")
print(g["device"]["interfaces"][0].keys())


# In[41]:


#### print alle devices in het netwerk
print('-----ALL-DEVICES-INTERFACES-IP-ADDRESSES-----')
for verandert in rack_struc["rack"]:
    print(verandert["device"]["dev_name"])
    for beterenaam in verandert["device"]["interfaces"]:
        print(beterenaam["interface"]+" => "+beterenaam["ipaddress"])


# In[33]:


rack_server = {
 "rackserver": [
      { "device": { "serv_id": "D1" , 
                    "serv_name": "Server1" , 
                    "role": "server"  , 
                    "ipaddress": "127.0.0.1",
                    "poorten": [   
                      {"port": "22/tcp" , "state": "filtered", "service": "ssh"},
                      {"port": "25/tcp" , "state": "open", "service": "smtp"},
                      {"port": "80/tcp" , "state": "open", "service": "http"} 
                     ]
                 }
      },
      { "device": { "serv_id": "D2" , "serv_name": "server2" , "role": "server"  ,  "ipaddress": "172.0.0.1",
                    "poorten": [       
                      {"port": "22/tcp" , "state": "filtered", "service": "ssh"},
                      {"port": "111/tcp" , "state": "open", "service": "rpcbind"},
                      {"port": "631/tcp" , "state": "open", "service": "ipp"} 
                     ]
                 }
                        
      }

   ]
}


# In[35]:


import yaml
yaml_data2 = yaml.dump(rack_server)
print(yaml_data2)


# In[52]:


#### print alle servers en poorten in het netwerk
print('-----ALL-SERVERS-POORTEN-IP-ADDRESSES-----')
for deServers in rack_server["rackserver"]:
    print(deServers["device"]["serv_name"]+" : "+deServers["device"]["ipaddress"])
    for alleinfo in deServers["device"]["poorten"]:
        print(alleinfo["port"]+" => "+alleinfo["service"]+" => "+alleinfo["state"])


# In[ ]:




