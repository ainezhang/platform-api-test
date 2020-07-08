import json

import pytest
import requests
from pandas.tests.io.excel.test_openpyxl import openpyxl

with open('../data/data.json', encoding='utf-8') as f:
    data = json.load(f)
# print(data)


@pytest.mark.parametrize('req', data)
def test_use_json(req):
    res = requests.request(**data)
    print(res.text)

