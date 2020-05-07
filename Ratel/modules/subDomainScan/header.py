# -*- coding:utf-8 -*-
#@Time : 2020/4/15 16:18
#@Author: Triomphe
#@File : header.py

import requests

# target='www.baidu.com , qq.com'
def header(target):
    """
    :param target: 域名
    :return: 字典,需要的http头信息
    """
    response={}
    if not target.startswith('http'):
        target ='http://'+target
    try:
        res=requests.head(target)
        #过滤掉500 502 等等
        if str(res.status_code).startswith('5'):
            response.update({'Enable':False})
            return response
        if 'Server' not in res.headers.keys():
            response.update({'Server':'Unknown'})
        else:
            response.update({'Server':res.headers['Server']})
        response.update({'Enable':True,'code':res.status_code})

    except:
        response.update({'Enable':False})
    return response

