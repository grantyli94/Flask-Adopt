import requests
from project_secrets import API_SECRET, API_KEY
from random import choice
# from app import app


auth_token = None

# @app.before_first_request
def refresh_credentials():
    """Just once, get token and store it globally."""
    global auth_token
    auth_token = update_auth_token_string()

def update_auth_token_string():
    resp = requests.post('https://api.petfinder.com/v2/oauth2/token',
    data={
            "grant_type":"client_credentials",
            "client_id": API_KEY,
            "client_secret": API_SECRET})
    response_data = resp.json()
    return response_data["access_token"]

def get_random_pet_info():
    resp = requests.get(
        'https://api.petfinder.com/v2/animals',
        headers={"Authorization": f"Bearer {auth_token}",
                 "limit": '100'}
    )
    response = resp.json()
    animals = response['animals']
    while True:
        animal = choice(animals)
        if "photos" not in animal or len(animal["photos"]) == 0:
            continue
        return {
          "name": animal['name'], 
          "url": animal['photos'][0]["medium"], 
          "age": animal['age']}
