import requests

from fastapi import Depends, FastAPI
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette.status import (
    HTTP_200_OK,
    HTTP_401_UNAUTHORIZED,
    HTTP_500_INTERNAL_SERVER_ERROR
)

app = FastAPI()

REALM = 'MyRealm'
KEYCLOAK_BASEURL = f'https://app.kring.info/auth/realms' \
                   f'/{REALM}/protocol/openid-connect'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=KEYCLOAK_BASEURL + '/token')


async def auth(token: str = Depends(oauth2_scheme)):
    headers = {'Authorization': 'bearer ' + token}
    r_user = requests.get(
        KEYCLOAK_BASEURL + '/userinfo',
        headers=headers,
        verify=False
    )
    if r_user.status_code == HTTP_200_OK:
        return r_user.json()
    elif r_user.status_code == HTTP_401_UNAUTHORIZED:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail=r_user.json()
        )
    else:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Internal authentication error (our bad)'
        )


# Public endpoint - does not require any authentication
@app.get('/api/public')
def hello_world():
    return {'msg': 'Hello world'}


# Protected endpoint - requires a Keycloak JWT token
@app.get('/api/user/me')
async def user_me(user: dict = Depends(auth)):
    return user
