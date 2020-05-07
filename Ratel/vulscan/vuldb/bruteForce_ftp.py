# -*- coding:utf-8 -*-
#@Time : 2020/5/2 16:53
#@Author: Triomphe
#@File : bruteForce_ftp.py

# coding:utf-8
import ftplib

def get_plugin_info():
    plugin_info = {
        "name": "FTP弱口令",
        "info": "导致敏感信息泄露，严重情况可导致服务器被入侵控制。",
        "level": "高危",
        "type": "弱口令",
        "keyword": "server:ftp",
        "source": 1,
    }
    return plugin_info


def check(ip, port=21, timeout=5):
    pass_list=[]
    with open(ROOT_PATH+"/data/password_dict/pass.txt") as f:
        for line in f:
            line=line.replace('\n','')
            pass_list.append(line)
    # print(ROOT_PATH)
    user_list = ['ftp', 'www', 'admin', 'root', 'db', 'wwwroot', 'data', 'web']

    for user in user_list:
        for pass_ in pass_list:
            ftp = ftplib.FTP()
            ftp.timeout = timeout
            try:
                ftp.connect(ip, int(port))
                ftp.login(user, pass_)
                if pass_ == '': pass_ = "null"
                if user == 'ftp' and pass_ == 'ftp':
                    return "21 端口存在可匿名登录"
                return "存在弱口令 账号:{} , 密码:{}".format(user,pass_)
            except Exception as e:
                print("bruteForce_ftp:"+str(e))
                return
