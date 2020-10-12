# -*- coding:utf-8 -*-
#@Time : 2020/4/16 22:35
#@Author: Triomphe
#@File : my_thread.py


#threading 继承的多线程
import threading
import logging
from PyQt5.QtCore import *
"""
    func
"""
class MyThread(threading.Thread):
    def __init__(self,queue,func):
        threading.Thread.__init__(self)
        self.queue=queue
        self.func=func
        self.thread_stop=False

    def run(self):
        while True:
            try:
                #args为func的参数.
                args= self.queue.get(block=True,timeout=20)
                # print(args)
                try:
                    self.func(*args)
                    self.queue.task_done()
                except Exception as e:
                    logging.debug('多线程尝试执行函数失败')
                    self.queue.task_done()
            except Exception as e2:
                print('多线程尝试获取队列数据失败')
                break

    def stop(self):
        print()
        self.thread_stop = True