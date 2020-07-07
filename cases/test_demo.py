import requests
import json


def test_01(load):
    d = load('data.json')
    print(d)


def test_02(data):
    print(data)


def test_03(test_data):
    print(test_data)


def test_04(db):
    r = db.query("SELECT * from bbs_activity_calendar.act_info WHERE game_biz='bbs_cn'")
    print(r)
