#Retrieve the continents & countries data from the REST API
import requests, json
from authentication import basic_auth

def fetch_restapi_json(url, username, password):
    headers = {'Authorization': basic_auth(username, password)}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        if response and response.status_code == 200:
            json_data = response.json()
            return json_data
    except requests.exceptions.HTTPError as e:
        response_text = json.loads(e.response.text)
        return {'Error':str(response.status_code)+' '+response.reason+' - '+response_text['detail']}
