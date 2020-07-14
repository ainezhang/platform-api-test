from utils.http import HTTP


class LeiLvActivity(HTTP):
    def hotlist(self, params_a):
        url = '/post/wapi/hotReplyList'
        params_a = params_a
        cookie = 'account_id=58364; cookie_token=fQN4Sf3dTEB9ca5dygQiOFRrM5Y7Em9h8XxvWdge; login_ticket=wP8Pi5aVU9WX2Paa20vVX8z7N4yEEkp6NNBDwvkt; ltoken=VtqAP82FUCWlF83NQlfyDmCBlb1W3g05KiYwZRMx; ltuid=58364; _ga=GA1.2.1551336199.1594280350; UM_distinctid=173318bdd1d1cb-0f5bb3234a83048-4a7d1612-5a900-173318bdd1ea28'
        headers = {
            "cookie": cookie}
        res = self.get(url, params=params_a, headers=headers)
        return res.json()
