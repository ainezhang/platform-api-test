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



class GetCookie():
    def get_token(self, uid):
        '''测试环境stoken默认为永久有效'''
        url = 'http://47.103.40.66/communityUtils/getCookie/?uid={}&env=dev'.format(uid)
        res = requests.get(url)
        stoken_str = res.json()['data']['cookie_info'][0]['sToken']
        ltoken_str = res.json()['data']['cookie_info'][0]['lToken']
        stoken = re.findall(r"stoken=(.+)", stoken_str)[0]
        ltoken = re.findall(r"ltoken=(.+)", ltoken_str)[0]
        return (stoken, ltoken)

    def get_cookie_token(self, uid):
        """通过stoken来获取cookie_token的值"""
        stoken = self.get_token(uid)[0]
        url = 'https://devapi-takumi.mihoyo.com/auth/api/getCookieAccountInfoBySToken?stoken={}&uid={}'.format(
            stoken, uid)
        res = requests.get(url)
        cookie_token = res.json()['data']['cookie_token']
        return cookie_token

    def get_cookie(self, uid):
        """cookie的值由account_id(uid);cookie_token;ltoken拼接而成"""
        ltoken = self.get_token(uid)[1]
        cookie = "account_id={};cookie_token={};ltoken={}".format(uid, self.get_cookie_token(uid), ltoken)
        print(cookie)
        return cookie


if __name__ == '__main__':
    a = GetCookie()
    # a.get_cookie_token(17365)
    a.get_cookie(17365)
