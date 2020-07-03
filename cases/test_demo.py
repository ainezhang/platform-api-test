import requests
import json


def lottery(num):
    #测试活动已结束，抽奖失败
    url = 'https://devapi-takumi.mihoyo.com/event/excalibur/lottery'
    data = {
        'act_id': 'e202006151956571',
        'cnt': 1
    }
    headers = {"cookie": "account_id=29168;cookie_token=NFvQwVaguwg8QGMyNdakxCOPBV5w0uvFQood7mzo",
               "x-rpc-device_id": "123"}

    for i in range(num):
        res = requests.post(url, data=json.dumps(data), headers=headers)

    # a = res.json()['data']['list']
    print(res.text)
    # print(len(a))


if __name__ == '__main__':
    lottery(1)
