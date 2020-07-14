"""用来读取数据"""
import os
import yaml

from utils.log import get_logger

log = get_logger('data')

# 向上两级找到项目的根目录
base_dir = os.path.dirname(os.path.dirname(__file__))


def load_yaml(file_name):
    file_path = os.path.join(base_dir, 'data', file_name)
    with open(file_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    log.debug(f'文件路径: {file_path} 数据: {data}')
    return data


if __name__ == '__main__':
    print(load_yaml('data.yaml'))
