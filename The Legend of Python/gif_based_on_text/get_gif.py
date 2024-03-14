import os, json, requests

giphy_api_key = os.getenv('GIPHY_API_KEY')

def get(search):
    response = requests.get(f'https://api.giphy.com/v1/gifs/search?api_key={giphy_api_key}&q={search}&limit=5')
    json_data = json.loads(response.text)
    return json_data