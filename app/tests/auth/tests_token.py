from tests.fixtures import client, db, anyio_backend, pytestmark, create_user

from httpx import AsyncClient

async def test_get_login_token_succes(client: AsyncClient, db, create_user):
    payload = {
        'username': 'test_user',
        'password': 'test_password',  
    }
    headers = {
        'content-type': 'application/x-www-form-urlencoded'
    }
    response = await client.post('/login', data=payload, headers=headers)
    
    assert response.status_code == 202
    
async def test_get_login_token_failed(client: AsyncClient, db, create_user):
    payload = {
        'username': 'test_user_not_found',
        'password': 'test_password',  
    }
    headers = {
        'content-type': 'application/x-www-form-urlencoded'
    }
    response = await client.post('/login', data=payload, headers=headers)
    
    assert response.status_code == 401