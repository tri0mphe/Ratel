# -*- coding:utf-8 -*-
#@Time : 2020/5/3 14:51
#@Author: Triomphe
#@File : mod_get_config.py

import configparser
from modules import mod_get_rootPath
import logging

def getConfig(section, key=None):
    """
    获取配置信息
    :param section: ini的section
    :param key:  默认为None 则返回整个section,否则返回section的某个key
    :return:
    """
    config = configparser.ConfigParser()
    try:
        path = mod_get_rootPath.get_root_path()+ '/config/config.ini'
    except Exception as e:
        logging.error("getConfig : "+e)
    config.read(path,encoding='utf-8')
    if key!=None:
        return config.get(section,key)
    else:
        result=config[section]
        return result
