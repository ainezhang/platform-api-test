import logging
import os
from datetime import datetime

# 获取当前运行脚本的绝对路径
base_dir = os.path.dirname(os.path.dirname(__file__))


def get_logger(name):
    today = datetime.now().strftime('%Y%m%d')
    logger = logging.Logger(name)

    handler1 = logging.StreamHandler()
    logger.setLevel(logging.DEBUG)
    handler2 = logging.FileHandler(
        filename=os.path.join(base_dir, 'logs', f'{today}.log'),
        encoding='utf-8',
        mode='a'
    )
    fmt = logging.Formatter(
        '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
    )
    handler1.setFormatter(fmt)
    handler2.setFormatter(fmt)
    logger.addHandler(handler1)
    logger.addHandler(handler2)
    return logger


if __name__ == '__main__':
    log = get_logger('utils')
    log.debug('调试信息')
    log.info('正式信息')
