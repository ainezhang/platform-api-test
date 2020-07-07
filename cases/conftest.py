import pytest
from utils.data import load_json
from utils.db import DB


# fixture可以作为函数工厂，返回一个函数
@pytest.fixture(scope='session')
def load():
    return load_json  # 返回一个函数，可以在用例中传入不同的参数获取不同的数据


@pytest.fixture(scope='session')
def data():  # 获取默认全部数据
    return load_json('data.json')


@pytest.fixture
def test_data(request):  # 获取默认数据中本用例的数据
    data = load_json('data.json')
    case_name = request.function.__name__  # 获取调用函数名称
    return data.get(case_name)

@pytest.fixture(scope='session')
def db():
    db = DB()
    yield db
    db.close()
