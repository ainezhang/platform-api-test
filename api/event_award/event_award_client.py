"""该文件用于存放积分抽奖前端接口定义及公共方法"""
import json

from utils.http import HTTP


class ScoreLottery(HTTP):
    def lottery(self, act_id, device_id):
        url = '/event/excalibur/lottery'
        data = {
            "act_id": act_id,
            "cnt": 1
        }
        cookie = 'account_id=17365; cookie_token=hw71bJXjnM3kgjstCBn8txyCwZvfNpfRBwy47fRi; login_ticket=kbX7fCdJlAtwzPp7j5OsjRGqxAkcWiWeLj61AyIQ; ltoken=QfXnKu5ioY64j4myKrmmYOy9JeHUKXkJwO5Jv8tp; ltuid=17365; _ga=GA1.2.1551336199.1594280350; UM_distinctid=173318bdd1d1cb-0f5bb3234a83048-4a7d1612-5a900-173318bdd1ea28'
        headers = {
            "cookie": cookie,
            "x-rpc-device_id": device_id}
        res = self.post(url, data=json.dumps(data), headers=headers)
        return res.json()
