# 该文件对请求方法进行封装
import requests


class HTTP(object):
    def __init__(self, base_url=None):
        self.session = requests.session()
        self.session.timeout = 10
        self.base_url = base_url

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
