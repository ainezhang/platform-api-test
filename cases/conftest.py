"""用例共享的fixture方法"""
import pytest

from api.score_lottery import ScoreLottery


@pytest.fixture(scope='session')
def lottery_cnt():
    lottery_cnt = ScoreLottery(59555)
    return lottery_cnt

