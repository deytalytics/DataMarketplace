#Retrieve the continents & countries data from the REST API
import requests, pandas as pd, json
from base64 import b64encode
from io import StringIO

# Authorization token: we need to base 64 encode it
# and then decode it to acsii as python 3 stores it as a byte string
def basic_auth(username, password):
    token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'
def fetch_restapi_csv(url, username, password):
    headers = {'Authorization': basic_auth(username, password)}
    try:
        response = requests.get(url, headers=headers, params={'format':'csv'})
        response.raise_for_status()
        if response and response.status_code == 200:
            return response
    except requests.exceptions.HTTPError as e:
        response_text = json.loads(e.response.text)
        return {'Error':str(response.status_code)+' '+response.reason+' - '+response_text['detail']}
