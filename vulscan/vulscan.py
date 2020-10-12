# -*- coding:utf-8 -*-
#@Time : 2020/4/27 16:05
#@Author: Triomphe
#@File : vulscan.py

import importlib
import os
import sys

from PyQt5.QtCore import QObject, pyqtSignal

from vulscan.port_scan import portscan
from modules.mod_get_rootPath import get_root_path
sys.path.append(os.path.abspath(
    os.path.dirname(__file__))+'/vuldb')

#根目录
ROOT_PATH =get_root_path()

class Vulscan(QObject):
    _signal =pyqtSignal(dict)
    _signal_finish=pyqtSignal()
    script_plugin_list=[]
    open_prot_list=[]

    def __init__(self,target_ip):
        super(Vulscan, self).__init__()
        #文件位置
        self.root_path =get_root_path()
        self.target_ip =target_ip

        self.init()

    def init(self):
        file_list = os.listdir(self.root_path + '/vulscan/vuldb')
        for filename in file_list:
            try:
                if filename.endswith('.py') and filename.split('.')[1] == 'py':
                    self.script_plugin_list.append(filename.split('.')[0])
            except Exception as e:
                print("error : "+str(e))
        #给每个插件设置 声明根目录


    #开始进行扫描
    def start_scan(self):
        try:
            self.open_prot_list=portscan(self.target_ip)
        except Exception as e:
            print(e)
            self.open_prot_list=['80']

        self.poc_check()

    #漏洞验证
    def poc_check(self):
        for plugin in self.script_plugin_list:
            res=importlib.import_module(plugin)
            setattr(res,"ROOT_PATH",ROOT_PATH)
            #先使用默认端口,如果存在就不使用端口扫描的进行检测
            result_info=res.check(self.target_ip)
            if result_info!=None:
                text=res.get_plugin_info()
                text['result_info']=result_info
                self._signal.emit(text)
            else:
                #使用masscan 扫描后对所有存活端口进行扫描
                for port in self.open_prot_list:
                    result_info=res.check(self.target_ip,port=port)
                    if result_info != None and result_info !="":
                        text=res.get_plugin_info()
                        text['result_info']=result_info
                        self._signal.emit(text)
        #表示完成了.
        self._signal_finish.emit()
