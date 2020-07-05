import json
import requests


def test_use_json():
    with open('../data/data.json', encoding='utf-8') as f:
        data = json.load(f)
    res = requests.request(**data)
    print(res.text)
