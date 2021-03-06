# 该文件对请求方法进行封装
import random

import requests

from api.cookie.get_user_cookie import GetCookie
from const import UserInfo


class HTTP(object):
    def __init__(self, base_url=None):
        self.session = requests.session()
        self.session.timeout = 10
        self.base_url = base_url
        account = random.choice(UserInfo.mapping)
        self.uid = account.get("uid")
        self.cookie = GetCookie().get_cookie(self.uid)

    def request(self, method, url: str, **kwargs):
        if self.base_url and not url.startswith('https'):
            url = self.base_url + url
        res = self.session.request(method, url, **kwargs)
        return res

    def get(self, url, **kwargs):
        return self.request('GET', url, **kwargs)

    def post(self, url, **kwargs):
        return self.request('POST', url, **kwargs)


# if __name__ == '__main__':
#     http = HTTP()
#     http.get()
