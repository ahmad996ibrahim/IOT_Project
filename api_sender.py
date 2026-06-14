import json
import random
import requests
import os
import time
from datetime import datetime
payload_data = {
    "meta_data" : {
        "factory_id" : "Dubai_001",
        "machine_ID" : "kuka_27000",
    },
    "robot_data" : {
        "tempbycelesuis" : round(random.uniform(20.0 , 70.0),2),
        "currentbyAmp" : round(random.uniform(10.0 , 20.0),2),        
    },
    "timestamp" : datetime.now().isoformat()
}

api_url = "https://httpbin.org/post"

try :
    respone = requests.post(api_url,json=payload_data,timeout=5)

    if respone.status_code ==200 :
        print ("data has been send sucessfuly")
        server_replay = respone.json()
        print(server_replay)

        print (json.dumps(server_replay,indent=4))
    else :
        print (f"Error: Server responded with code :{respone.status_code}")
except requests.ConnectionError :
    print("Error: Failed to connect. Check your internet connection or DNS.")
except requests.Timeout :
    print("Error: The server took too long to respond. Network might be down.")
