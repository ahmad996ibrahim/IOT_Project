import json
import requests

api_url = "https://jsonplaceholder.typicode.com/users/1"

try :
    print("Request information from API")
    respone = requests.get(api_url)
    if respone.status_code == 200 :
        user_data = respone.json()
        print (user_data ["name"])
        print(user_data["email"])
        print(user_data["company"]["name"])
    elif respone.status_code == 404 :
        print ("Error: The requested resource was not found on the server.")
    else :
        print (f"Error: Server responded with code :{respone.status_code}") 
except requests.exceptions.Timeout :
    print("Error: The server took too long to respond. Network might be down.")
except requests.exceptions.ConnectionError :
    print("Error: Failed to connect. Check your internet connection or DNS.")

    