# -*- coding:utf-8 -*-
#@Time : 2020/5/1 18:58
#@Author: Triomphe
#@File : port_scan.py

import os,sys

from modules import mod_get_rootPath

#根目录
root_path =mod_get_rootPath.get_root_path()
"""
注释: 调用masscan 扫描IP获取端口
return : list ,返回Ip地址 存活端口

"""
def portscan(scan_ip):
    temp_ports = [] #设定一个临时端口列表
    os.system(root_path+'/extools/masscan.exe ' + scan_ip + ' -p 1-65535 --rate 2000 -oL masscanResult.txt ')
    #提取json文件中的端口
    with open('masscanResult.txt', 'r') as f:
        for line in f:
            if not line.startswith('#'):
                temp = line.split()
                temp1 = temp[2]
                temp_ports.append(str(temp1))

    if len(temp_ports) > 50:
        temp_ports.clear()       #如果端口数量大于50，说明可能存在防火墙，属于误报，清空列表
    #小于50则放到总端口列表里
    print(temp_ports)
    return temp_ports

