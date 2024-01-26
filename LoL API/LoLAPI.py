import requests

api_key = 'RGAPI-10e5da75-f60f-4e07-9950-8f9d57dd42b6'
summoner_name = 'test'

# Construct the API URL
url = f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}'

# Make the API request
response = requests.get(url)
data = response.json()

# Print summoner information
print(f"Summoner ID: {data['id']}")
print(f"Summoner Level: {data['summonerLevel']}")
print(f"Summoner Account ID: {data['accountId']}")
