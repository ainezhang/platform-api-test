import pytest
from utils.http import HTTP

from utils.db import DB


@pytest.fixture(scope='session')
def db():
    db = DB()
    yield db
    db.close()


@pytest.fixture(scope='session')
def http(base_url):
    return HTTP(base_url)
