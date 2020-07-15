from utils.db import DB


def test_lottery_single(api_lottery, data):
    act_id = data.get('act_id')
    device_id = data.get('device_id')
    res_dict = api_lottery.lottery(act_id, device_id)
    # db_result = DB().query("SELECT * from bbs_activity_calendar.act_info WHERE game_biz='bbs_cn'")
    print(res_dict)
