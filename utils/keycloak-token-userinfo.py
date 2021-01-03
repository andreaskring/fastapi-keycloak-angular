import json
import requests

REALM = 'MyRealm'
KEYCLOAK_BASEURL = f'https://localhost/auth/realms/{REALM}' \
                   f'/protocol/openid-connect'


token_url = KEYCLOAK_BASEURL + '/token'

# Get token

payload = {
    'grant_type': 'password',
    'client_id': 'MyApp',
    'username': 'bruce',
    'password': 'bruce'
}

r = requests.post(token_url, data=payload, verify=False)
print(r.status_code, r.url)
token = r.json()['access_token']

headers = {
    'Authorization': f'bearer {token}'
}

# Get userinfo (and hence validate then token)

userinfo_url = KEYCLOAK_BASEURL + '/userinfo'
r = requests.get(userinfo_url, headers=headers, verify=False)
print(r.status_code, r.url)
print(json.dumps(r.json(), indent=2))
