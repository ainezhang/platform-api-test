# 该文件用来读取测试数据
import json
import os

from utils.log import get_logger
log = get_logger('data')
# 向上两级找到项目的根目录
base_dir = os.path.dirname(os.path.dirname(__file__))


def load_json(file_name):
    file_path = os.path.join(base_dir, 'data', file_name)
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)
    log.debug(f'文件路径:{file_path} 数据:{data}')
    return data


if __name__ == '__main__':
    print(load_json('data.json'))
