# 该文件对请求方法进行封装
import random

import requests

from get_cookies import GetCookie


class HTTP(object):
    def __init__(self, uid, base_url=None):
        self.base_url = base_url
        self.session = requests.session()
        self.session.headers = {"cookie": GetCookie().get_cookie(uid),
                                "x-rpc-device_id": "99C29E73024E4E2E91577F15A72D27F4"}
        self.session.timeout = 10

    def request(self, method, url: str, **kwargs):
        if self.base_url and not url.startswith('https'):
            url = self.base_url + url
        res = self.session.request(method, url, **kwargs)
        return res

    def get(self, url, **kwargs):
        return self.request('GET', url, **kwargs)

    def post(self, url, **kwargs):
        return self.request('POST', url, **kwargs)


if __name__ == '__main__':
    HTTP(59555).get('https://devapi-takumi.mihoyo.com/event/excalibur/lottery')
