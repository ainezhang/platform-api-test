"""该文件用于存放积分抽奖前端接口定义及公共方法"""
import json
import random

from api.cookie.get_user_cookie import GetCookie
from const import UserInfo
from utils.http import HTTP


class ScoreLottery(HTTP):
    # def __init__(self):
    #     account = random.choice(UserInfo.mapping)
    #     self.uid = account.get("uid")
    #     self.cookie = GetCookie().get_cookie(self.uid)

    def lottery(self, act_id, device_id):
        url = '/event/excalibur/lottery'
        data = {
            "act_id": act_id,
            "cnt": 1
        }
        headers = {
            "cookie": self.cookie,
            "x-rpc-device_id": device_id}
        res = self.post(url, data=json.dumps(data), headers=headers)
        return res.json()
