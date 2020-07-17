"""该文件用于存放积分抽奖前端接口定义及公共方法"""
import json
import random

from api.cookie.getCookie import GetCookie
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
            "cookie": "account_id=17365; cookie_token=hw71bJXjnM3kgjstCBn8txyCwZvfNpfRBwy47fRi;ltoken=QfXnKu5ioY64j4myKrmmYOy9JeHUKXkJwO5Jv8tp",
            "x-rpc-device_id": device_id}
        # headers = {
        #     "cookie": self.cookie,
        #     "x-rpc-device_id": device_id}
        res = self.post(url, data=json.dumps(data), headers=headers)
        return res.json()
