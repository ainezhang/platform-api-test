import uuid

import faker
import pytest
import requests
import random

# 请求参数化
data1 = {
    'method': 'GET',
    'url': 'https://httpbin.org/get',
    'params': {'a': 1, 'b': 2},
    'headers': {'Cookie': 'a=1;b=2'}
}
data2 = {
    'method': 'POST',
    'url': 'https://httpbin.org/post',
    'data': {'name': 'Lily', 'password': '123456'}
}


# data = [data1, data2]

@pytest.mark.parametrize('data', [data1, data2])
def test_request(data):
    res = requests.request(**data)
    print(res.text)
    print(1)


# 1.字符串的参数
c = 3
d = 3


def test_get():
    url = f'https://httpbin.org/get?a=1&b=2&c={c}&d={d}'
    print(1)


# 使用随机数和假造数据
def test_use_random():
    a = random.randint(0, 100)
    b = random.uniform(0, 100)
    c = uuid.uuid1()  # 每次生成一个完全不重复的数
    type = random.choice([1, 2, 3, 7, 45, 6])
    url = f'https://httpbin.org/get?a={a}&b={b}&c={c}&type={type}'
    res = requests.get(url)
    print(res.json())


# 生成随机假数据 https://faker.readthedocs.io/en/master/locales/zh_CN.html
def test_faker():
    # 使用中文(本地化)
    f = faker.Faker(locale='zh-CN')
    print(f.name())  # s随机名字
    print(f.email())

# if __name__ == '__main__':
#     test_request()
