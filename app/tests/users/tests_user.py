from tests.fixtures import client, db, anyio_backend, pytestmark, create_user

from httpx import AsyncClient

async def test_create_user_success(client: AsyncClient, db):
    payload = {
        'name': 'test_user',
        'email': 'test_example@example.com',
        'password': 'test_password',
        'confirm_password': 'test_password'   
    }
    response = await client.post('/users/create_user', json=payload)
    
    assert response.status_code == 201
    assert response.json().get('name') == payload.get('name')

    
async def test_create_user_compare_passwords_failed(client: AsyncClient, db):
    payload = {
        'name': 'test_user',
        'email': 'test_example@example.com',
        'password': 'test_password',
        'confirm_password': 'test_password_not_match'
    }
    response = await client.post('/users/create_user', json=payload)
    
    assert response.status_code == 422
    
async def test_create_user_already_exist_failed(client: AsyncClient, db, create_user):
    payload = {
        'name': 'test_user',
        'email': 'test_example@example.com',
        'password': 'test_password',
        'confirm_password': 'test_password'   
    }
    response = await client.post('/users/create_user', json=payload)
    
    assert response.status_code == 400