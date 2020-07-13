import requests
import json


class TestLottery():
    def test_lottery(self, num):
        url = 'https://devapi-takumi.mihoyo.com/event/excalibur/lottery'
        data = {
            'act_id': 'e202006151956571',
            'cnt': 10
        }
        headers = {"cookie": "account_id=29168;cookie_token=NFvQwVaguwg8QGMyNdakxCOPBV5w0uvFQood7mzo",
                   "x-rpc-device_id": "123"}

        for i in range(num):
            res = requests.post(url, data=json.dumps(data), headers=headers)

        a = res.json()['data']['list']


# def test_01(load):
#     d = load('data.json')
#     print(d)
#
#
# def test_02(data):
#     print(data)
#
#
# def test_03(test_data):
#     print(test_data)
#
#
# def test_04(db):
#     r = db.query("SELECT * from bbs_activity_calendar.act_info WHERE game_biz='bbs_cn'")
#     print(r)
