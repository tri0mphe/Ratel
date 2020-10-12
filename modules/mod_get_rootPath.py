# -*- coding:utf-8 -*-
#@Time : 2020/5/3 14:48
#@Author: Triomphe
#@File : mod_get_rootPath.py


import os

def get_root_path():
    """
    获取根路径
    :return:根路径
    """
    return os.path.dirname(os.path.split(os.path.realpath(__file__))[0])
