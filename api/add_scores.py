import json

import requests
import random
import xlrd
import uuid
import csv


class AddMyb(object):
    def add_myb_single(self, uid):
        """单个添加米油币"""
        url = 'https://ptsapi-takumi.mihoyo.com/common/homutreasure/op/opModifyUserPoint'
        ticket = str(uuid.uuid1())
        data = {
            "app_id": 1,
            "point_sn": "myb",
            "user": {
                "account_uid": uid
            },
            "action": 1,
            "modify_num": 1000000,
            "ticket": ticket,
            "source": "test",
            "type": "test"
        }
        res = requests.post(url=url, data=json.dumps(data))
        # print(ticket)
        # print(res.json())
        ret = res.json()['retcode']
        if ret != 0:
            print(res.json())
        # assert res.json()['retcode'] == 0

    def add_myb_toger(self):
        """批量添加米油币(读取表中的uid)"""
        ex = open('member_1.csv', 'r')
        reader = csv.reader(ex)
        content = []
        for line in reader:
            int(line[0])
            content.append(int(line[0]))
        # print(content[599999])
        content.reverse()
        for uid in content:
            self.add_myb_single(uid)
            self.get_user_point(uid)
            if uid == 73188684:
                break

    def get_user_point(self, uid):
        """查看用户的米油币"""
        url = 'https://ptsapi-takumi.mihoyo.com/common/homutreasure/op/opGetUserPoint'
        data = {
            "app_id": 1,
            "point_sn": "myb",
            "user": {
                "account_uid": uid
            }
        }
        res = requests.post(url=url, data=json.dumps(data))
        point = res.json()['data']['points']
        if int(point) <= 1000000:
            print(point)
        # print(res.text)
        # print(res.json()['data']['points'])


if __name__ == '__main__':
    AddMyb().add_myb_toger()
    # AddMyb().add_myb_single(59555)
