import pytest
from utils.data import load_yaml
from api.score_lottery.score_lottery_client import LeiLvActivity


@pytest.fixture(scope='session')
def data():  # 获取默认全部数据
    return load_yaml('data.yaml')


@pytest.fixture(scope='session')
def api(base_url):
    return LeiLvActivity(base_url)
