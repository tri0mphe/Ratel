# -*- coding:utf-8 -*-
#@Time : 2020/4/17 14:48
#@Author: Triomphe
#@File : Scan11.py

import logging
import queue
import threading
from PyQt5.QtCore import pyqtSignal, QObject
from subDomainScan import BruteForce

import  time
"""
queue_in 表示输入队列,处理爆破的文件关键字
domain : 子域名后面部分
fileName : 文件绝对路径(str)
继承线程,run里面是子线程运行的逻辑代码
"""

class MyProducer(threading.Thread):
    currentTryNum=0
    def __init__(self,queue_in,domain,fileName):
        super(MyProducer, self).__init__()
        self.q=queue_in
        self.domain=domain
        self.file=fileName
        self.thread_stop=False
    def run(self):
        while not self.thread_stop:
            try:
                # print(self.file)
                with open(self.file,'r') as f:
                    for row in f:
                        row =row.replace('\n','')
                        text=str(row)+'.'+self.domain
                        self.q.put(text)
                        self.currentTryNum+=1

                f.close()
            except Exception as e:
                logging.error(e)
                self.thread_stop=True #子线程结束

    def stop(self):
        try:
            print('到xxxxxxxx')
            if self.is_alive():
                self.thread_stop=True
        except Exception as e:
            print(e)


class MyConsumer(threading.Thread):
    def __init__(self,queue_in,queue_out):
        super(MyConsumer, self).__init__()
        self.qin=queue_in
        self.qout=queue_out
        self.thread_stop=False

    def run(self):
        while not self.thread_stop:
            try:
                args= self.qin.get(block=True,timeout=20)
                res= BruteForce.bf_subdomain(args)
                if res:
                    self.qout.put(res)
                self.qin.task_done()
            except Exception as e2:
                print(e2)
                break
        print('成功退出了')
    def stop(self):
        if not self.thread_stop:
            self.thread_stop=True
        return True

class Worker_sds(QObject):
    _signal_showInfo=pyqtSignal(list)
    _signal_progressBar=pyqtSignal(int)
    def __init__(self,num,domain,file):
        super(Worker_sds, self).__init__()
        self.qin=queue.Queue(60)
        self.qout=queue.Queue(60)
        self.tnum =num  #线程数量
        self.file=file
        self.threads=[]
        self.producer=MyProducer(self.qin,domain,self.file)
        self.thread_stop =False

    def work(self):
        for i in range(self.tnum):
            t=MyConsumer(self.qin,self.qout)
            t.setDaemon(True)
            self.threads.append(t)
            t.start()
        self.producer.setDaemon(True)
        self.producer.start()
        self.showInfo()

    def showInfo(self):
        while not self.thread_stop:
            res=self.qout.get()
            self._signal_showInfo.emit(res)
            logging.debug(self.producer.currentTryNum)
            self._signal_progressBar.emit(self.producer.currentTryNum)

    def stop(self):
        try:
            if not self.thread_stop:
                self.thread_stop=True
            if not self.producer.thread_stop:
                self.producer.stop()
            for i in self.threads:
                print(i)
                i.stop()
        except Exception as e:
            print(e)
        return
