import pytest

from api.event_award.event_award_client import ScoreLottery
from utils.data import load_yaml


# from api.score_lottery.score_lottery_client import LeiLvActivity


@pytest.fixture(scope='session')
def data():  # 获取默认全部数据
    return load_yaml('event_award.yaml')


@pytest.fixture(scope='session')
def api_lottery(base_url):
    return ScoreLottery(base_url)
