import pytest, httpx 

from database.core import init_db
from main import app 

pytestmark = pytest.mark.anyio


@pytest.fixture(scope='session')
def anyio_backend():
    return 'asyncio'


@pytest.fixture(scope='function')
async def create_user():
    async with httpx.AsyncClient(app=app, base_url='http://test') as client:
        payload = {
            'name': 'test_user',
            'email': 'test_example@example.com',
            'password': 'test_password',
            'confirm_password': 'test_password'   
        }
        await client.post('/users/create_user', json=payload)


@pytest.fixture(scope='function')
def db():
    init_db()


@pytest.fixture(scope='session')
async def client():
    async with httpx.AsyncClient(app=app, base_url='http://test') as client:
        yield client 