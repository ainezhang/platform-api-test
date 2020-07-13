from requests import post


class ScoreLottery():
    @post("/lottery")
    def lottery(self):
        """抽奖接口"""
