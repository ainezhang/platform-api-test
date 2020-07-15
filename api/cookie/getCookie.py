"""
该文件用于存放获取cookie值
cookie所需的参数：
account_id=17365;
cookie_token=hw71bJXjnM3kgjstCBn8txyCwZvfNpfRBwy47fRi;
ltoken=QfXnKu5ioY64j4myKrmmYOy9JeHUKXkJwO5Jv8tp
"""
import json
import re

import requests

from utils.http import HTTP


class GetCookie(HTTP):
    def get_token(self, uid):
        '''测试环境stoken默认为永久有效'''
        url = 'http://47.103.40.66/communityUtils/getCookie/?uid={}&env=dev'.format(uid)
        res = requests.get(url)
        stoken_str = res.json()['data']['cookie_info'][0]['sToken']
        ltoken_str = res.json()['data']['cookie_info'][0]['lToken']
        stoken = re.findall(r"stoken=(.+)", stoken_str)
        ltoken = re.findall(r"stoken=(.+)", ltoken_str)
        return stoken

    def get_cookie_token(self, uid):
        """通过stoken来获取cookie_token的值"""
        url = 'https://devapi-takumi.mihoyo.com/auth/api/getCookieAccountInfoBySToken?stoken={token}&uid={uid}'.format(
            token=self.get_token(uid),uid=uid)
        res = requests.get(url)

    def get_cookie(self,uid):
        """cookie的值由account_id(uid);cookie_token;ltoken拼接而成"""


if __name__ == '__main__':
    a = GetCookie()
    a.get_cookie_token(17365)
