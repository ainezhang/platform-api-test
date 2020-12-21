from time import sleep

import pytest

# 验证抽奖接口
from score_lottery import ScoreLottery


class TestScene01:

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_physical_choice(self):
        """获取配置信息-判断米油币是否充足-单抽(实物n选1)-获取奖品列表-n选1子礼包 -（获取社区地址信息）-兑换-(发货)-查看物流信息-获取奖品列表"""
        act_id = "e202011051758461"
        uid = 59555
        # 判断米油币是否充足
        res_judge = ScoreLottery(uid).judgePointLimit()
        assert res_judge['data']['is_over'] is False
        # 抽奖，单抽(实物n选1)
        res_lottery = ScoreLottery(uid).lottery(
            act_id=act_id,
            cnt=1
        )
        assert res_lottery.get('retcode') == 0
        assert len(res_lottery["data"]["list"]) == 1
        # 获取奖励列表
        res_award = ScoreLottery(uid).award(act_id, 1)
        print(res_award.get('data')['list'])
        # 获取n选1子礼包
        res_package = ScoreLottery(uid).sub_package(act_id, 1)
        print(res_package.get('retcode'))
        # 获取社区地址
        res_address = ScoreLottery(uid).com_address()
        address_com = res_address.get('data')['list']
        # print(res_address.get('data')['list'])
        # 兑换
        res_exchange = ScoreLottery(uid).exchange(
            act_id=act_id,
            type=20,
            id=109,
            address=address_com
        )
        print(res_exchange.get('message'))
        sleep(3)
        # 获取奖励列表
        res_award = ScoreLottery(uid).award(act_id, 1)
        print(res_award.get('data')['list'])

    def test_physical(self):
        """获取配置信息-判断米油币是否充足-单抽(虚拟n选1)-获取奖品列表-n选1子礼包 -（获取社区地址信息）-兑换-(发货)-查看物流信息-获取奖品列表"""
        act_id = "e202011051758461"
        uid = 59555
        # 判断米油币是否充足
        res_judge = ScoreLottery(uid).judgePointLimit()
        assert res_judge['data']['is_over'] is False
        # 抽奖，单抽(虚拟n选1)
        res_lottery = ScoreLottery(uid).lottery(
            act_id=act_id,
            cnt=1
        )
        assert res_lottery.get('retcode') == 0
        assert len(res_lottery["data"]["list"]) == 1
        # 获取奖励列表
        res_award = ScoreLottery(uid).award(act_id, 1)
        print(res_award.get('data')['list'])
        # 获取n选1子礼包
        res_package = ScoreLottery(uid).sub_package(act_id, 1)
        print(res_package.get('retcode'))
        # 兑换
        res_exchange = ScoreLottery(uid).exchange(
            act_id=act_id,
            type=20,
            id=109,
            game_role=game_role
        )
        print(res_exchange.get('message'))
        sleep(3)
        # 获取奖励列表
        res_award = ScoreLottery(uid).award(act_id, 1)
        print(res_award.get('data')['list'])


class TestScene02(object):
    """获取配置信息-判断米油币是否充足-单抽(虚拟n选1)-获取奖品列表-n选1子礼包 -兑换-获取奖品列表"""

    def test00(self):
        pass


class TestScene03(object):
    """获取配置信息-判断米油币是否充足-单抽(实物)-获取奖品列表-n选1子礼包 -兑换-(发货)-查看物流信息-获取奖品列表"""

    def test000(self):
        pass


class Test01(object):
    @pytest.mark.smoke
    def test_sinle_lottery(self, lottery_cnt):
        # 验证单抽，返回正确
        res_lottery = lottery_cnt.lottery(
            act_id='e202011190014201',
            cnt=1
        )
        print(res_lottery)
        assert res_lottery.get('retcode') == 0
        assert len(res_lottery["data"]["list"]) == 1


def test_total_lottery(lottery_cnt):
    # 验证十连抽，返回正确
    res_lottery = lottery_cnt.lottery(
        act_id='e202011190014201',
        cnt=10
    )
    assert res_lottery.get('retcode') == 0
    assert len(res_lottery["data"]["list"]) == 10


def test4():
    """米游币充足，抽奖成功"""
    pass


def test5():
    """米游币不足，抽奖失败"""
    pass


def test3():
    """黑名单用户，抽奖失败"""
    pass


def test6():
    """不满足后台配置的抽奖门槛，抽奖失败，给出对应提示"""
    pass


def test7():
    """米游币发放超过上限，接口提示"""
    pass


def test01():
    """实物n选1兑换，兑换成功"""
    pass


def test02():
    """虚拟n选1兑换，兑换成功"""
    pass


def test03():
    """虚拟商品兑换兑换，兑换成功"""
    pass


def test04():
    """实物商品兑换兑换，兑换成功"""
    pass


def test05():
    """实物商品兑换兑换，兑换成功"""
    pass


if __name__ == '__main__':
    Scene01().aa()
