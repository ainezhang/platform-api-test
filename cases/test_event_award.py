import jsonschema
import requests

import json


# 验证抽奖接口
def test_single_lottery():
    # 单抽
    url = 'https://devapi-takumi.mihoyo.com/event/excalibur/lottery'
    data = {
        "act_id": "e202011190014201",
        "cnt": 1
    }
    headers = {
        "cookie": "account_id=59555; cookie_token=uIY3mTf3bJOchFiBiLt7fJpeCYR4WQ6AhUojDLPa",
        "x-rpc-device_id": "99C29E73024E4E2E91577F15A72D27F4"}
    res = requests.post(url, data=json.dumps(data), headers=headers)
    res_dict = res.json()
    print(len(res.json()["data"]["list"]))
    assert res_dict.get('retcode') == 0
    assert len(res.json()["data"]["list"]) == 1
    schema = {
        'type': 'object',
        'properties': {
            'retcode': {'type': 'integer'},
            'message': {'type': 'object'},
            'data': {
                'type': 'object',
                'properties': {
                    'list': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'name': {'type': 'string'},
                                'status': {'type': 'integer'},
                                'type': {'type': 'integer'},
                                'game': {'type': 'string'},
                                'img': {'type': 'string'},
                                'created_at': {'type': 'string'},
                            }
                        }
                    }
                }}
        },
    }
    jsonschema.validate(res_dict, schema)


def test_total_lottery():
    # 十连抽
    url = 'https://devapi-takumi.mihoyo.com/event/excalibur/lottery'
    data = {
        "act_id": "e202011190014201",
        "cnt": 10
    }
    headers = {
        "cookie": "account_id=59555; cookie_token=uIY3mTf3bJOchFiBiLt7fJpeCYR4WQ6AhUojDLPa",
        "x-rpc-device_id": "99C29E73024E4E2E91577F15A72D27F4"}
    res = requests.post(url, data=json.dumps(data), headers=headers)
    res_dict = res.json()
    print(len(res.json()["data"]["list"]))
    assert res_dict.get('retcode') == 0
    assert len(res.json()["data"]["list"]) == 10


if __name__ == '__main__':
    test_single_lottery()
