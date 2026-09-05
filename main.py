import requests
import requests_cache
import json 
import os
from config import Config

print("This is a test of script for the project Gamming Telemetry for data Analysis")

# List of access endpoint for different parts of user Steam API
baseurl1 = "https://api.steampowered.com/ISteamNews"
baseurl2 = "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2"
baseurl3 = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"


print("Processing server request")

baseurl = baseurl3
payload = {
    "key": Config.API_STEAM,
    "steamid": Config.ID_STEAM,
    "include_appinfo": True
}

print("fetching the data")
try:
    response = requests.get(baseurl, params=payload)

    if response.status_code == 200:
        data = response.json()
        games = data['response']['game_count']
        for i in range(games):
            print(data['response']['games'][i]['name'])
    else:
        print(f"❌ API Error: {response.status_code}")
        print(f"Server response text: {response.text}")
        
except Exception as e:
    print(f"Connection error: {e}")