import requests
import requests_cache
import json 
import os

print("This is a test of script for the project Gamming Telemetry for data Analysis")


steam_API_KEY = "ADD_API_KEY"
# baseurl = "https://api.steampowered.com/ISteamNews"

MATCH_ID = "ADD_GAME_LIVE"
STEAM_ID = "ADD_YOUR_ID"

# Creating mechanism of save cache
requests_cache.install_cache('api_cache', expire_after=3600)


baseurl = f"https://api.steampowered.com/ISteamWebAPIUtil/GetSupportedAPIList/v0001/?key={steam_API_KEY}"
print("Processing server request")

try:
    response = requests.get(baseurl)

    if response.status_code == 200:
        data = response.json()
        for i in range(0,3):
            print(data['apilist']["interfaces"][i], "\n")
    else:
        print(f"❌ API Error: {response.status_code}")
        print(f"Server response text: {response.text}")
        
except Exception as e:
    print(f"Connection error: {e}")