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

REALM = 'xyz'
KEYCLOAK_BASEURL = f'http://localhost:8080/auth/realms' \
                   f'/{REALM}/protocol/openid-connect'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=KEYCLOAK_BASEURL + '/token')


async def get_current_user(token: str = Depends(oauth2_scheme)):
    headers = {'Authorization': 'bearer ' + token}
    r_user = requests.get(KEYCLOAK_BASEURL + '/userinfo', headers=headers)
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


@app.get('/user/me')
async def hello_world(user: str = Depends(get_current_user)):
    return user
