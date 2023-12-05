import argparse
import pathlib
from collections import namedtuple
import os
import logging

logging.basicConfig(filename='directory_info.txt', filemode='w', level=logging.INFO)

def get_direct_path() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument('directory_path')
    args = parser.parse_args()
    return args.directory_path

def get_direct_info(dir_path):
    for file in dir_path.iterdir():
        file_info = File(file.name, file.suffix, file.is_dir(), os.path.dirname(file))
        logger.info(file_info)
        if file.is_dir():
            path = pathlib.Path(f'{os.path.dirname(file)}\{file.name}')
            get_direct_info(path)

if __name__ == '__main__':
    File = namedtuple('File', ['file_name', 'extension', 'catalog', 'parent_directory'])
    logger = logging.getLogger(__name__)
    direct_path = pathlib.Path(get_direct_path())
    get_direct_info(direct_path)
