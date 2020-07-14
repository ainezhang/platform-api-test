"""项目的一些钩子方法"""
import os
from utils.notify import send_mail

base_dir = os.path.dirname(__file__)


def pytest_addoption(parser):  # 添加一个自定义运行参数
    parser.addoption('--send-email', action='store', help=None)

# def pytest_terminal_summary(config):
#     send_email = config.getoption('--send-email')
#     if send_email:
#         report_path = os.path.join(base_dir, 'reports', 'report.html')
#         send_mail(
#             subject='接口测试报告',
#             body='Hi, 请查看附件。',
#             receivers=['liying.zhang@mihoyo.com'],
#             attachments=[report_path]
#         )
