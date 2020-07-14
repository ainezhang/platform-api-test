import requests
import json
from utils.db import DB


def test_hotlist(api, data):
    params_a = data.get('params_a')
    res_dict = api.hotlist(params_a)
    db_result = DB().query("SELECT * from bbs_activity_calendar.act_info WHERE game_biz='bbs_cn'")
    assert db_result[0]['id'] == 15
    assert res_dict['retcode'] == 0
