from utils.http_req import HTTP


class ScoreLottery(HTTP):
    def __init__(self, uid):
        HTTP.__init__(self, uid)

    def judgePointLimit(self):
        """米油币是否充足"""
        url = 'https://devapi-takumi.mihoyo.com/event/excalibur/judgePointLimit'
        res = self.get(url)
        return res.json()

    def lottery(self, **kwards):
        """抽奖"""
        url = 'https://devapi-takumi.mihoyo.com/event/excalibur/lottery'
        data = kwards
        res = self.post(url, json=data)
        return res.json()

    def exchange(self, **kwards):
        """兑换"""
        url = 'https://devapi-takumi.mihoyo.com/event/excalibur/exchange'
        data = kwards
        res = self.post(url, json=data)
        return res.json()

    def award(self, act_id, current_page):
        """奖品列表"""
        url = 'https://devapi-takumi.mihoyo.com/event/excalibur/award?act_id={}&current_page={}&page_size=10'.format(
            act_id, current_page)
        res = self.get(url)
        return res.json()

    def lottery_info(self, act_id):
        """获取剩余抽奖信息"""
        url = 'https://devapi-takumi.mihoyo.com/event/excalibur/info?act_id={}'.format(act_id)
        res = self.get(url)
        return res.json()

    def lottery_home(self, act_id):
        """获取抽奖配置信息"""
        url = 'https://devapi-takumi.mihoyo.com/event/excalibur/home?act_id={}'.format(act_id)
        res = self.get(url)
        return res.json()

    def sub_package(self, act_id, id):
        """n选1子礼包"""
        url = 'https://devapi-takumi.mihoyo.com/event/excalibur/sub_package?act_id={}&id={}'.format(act_id, id)
        res = self.get(url)
        return res.json()

    def searchLogistic(self, act_id, id):
        """n选1子礼包（未完成）"""
        url = 'https://devapi-takumi.mihoyo.com/event/excalibur/sub_package?act_id={}&id={}'.format(act_id, id)
        res = self.get(url)
        return res.json()

    def com_address(self):
        """获取用户社区地址"""
        url = 'https://devapi-takumi.mihoyo.com/event/excalibur/community/address'
        res = self.get(url)
        return res.json()


if __name__ == '__main__':
    s = ScoreLottery(17365)
    s.com_address()
