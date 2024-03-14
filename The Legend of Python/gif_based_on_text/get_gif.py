import json, requests

api_key = '' # Replace with your own API key.

def get(search):
    response = requests.get(f'https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={search}&limit=5')
    json_data = json.loads(response.text)
    return json_data