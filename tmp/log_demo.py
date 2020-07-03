import logging
import os

# 获取当前运行脚本的绝对路径
base_dir = os.path.dirname(os.path.dirname(__file__))

handler1 = logging.StreamHandler()
handler2 = logging.FileHandler(
    filename=os.path.join(base_dir, 'logs', 'run.logs'),
    encoding='utf-8',
    mode='a'
)
logging.basicConfig(
    # 日志级别
    level=logging.DEBUG,
    # 日志格式
    # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
    # 打印日志的时间
    datefmt='%a, %d %b %Y %H:%M:%S',
    # 日志文件存放的目录（目录必须存在）及日志文件名
    filename=os.path.join(base_dir, 'logs', 'run.logs'),
    # 追加模式 'w'覆盖
    filemode='w',
    # handlers=[handler1, handler2]
)
logging.debug('调试信息')
logging.info('正常信息')
logging.warning('警告信息')
logging.error('出错')
logging.critical('严重出错')
try:
    open('abc.txt')
except Exception as ex:
    logging.exception(ex)  # error级别，包含追溯信息
