# -*- coding:utf-8 -*-
#@Time : 2020/3/12 23:30
#@Author: Triomphe
#@File : customWidget.py


# 目前废除

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
class CustomItemWidget(QWidget):

    def __init__(self,parent=None):
        super(CustomItemWidget,self).__init__(parent)

        #结局UI问题
        self.initUI()
        #解决逻辑问题
        self.initSet()
    def initUI(self):

        #垂直布局
        myLayout =QVBoxLayout()
        myLayout.setSpacing(0)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        self.setMaximumWidth(1)
        sizePolicy.setVerticalStretch(5)

        self.setSizePolicy(sizePolicy)
        self.setStyleSheet("QWidget{background:white}")
        self.setFixedSize(120,120)
        imgLab=QLabel()
        imgLab.setFixedSize(80,80)
        textlab=QLabel()

        img =QPixmap('./exit.png')
        #设置图片自适应
        imgLab.setScaledContents(True)
        imgLab.setPixmap(img)

        textlab.setText("test")
        textlab.setAlignment(Qt.AlignCenter)

        myLayout.addWidget(imgLab,alignment=Qt.AlignCenter)
        myLayout.addWidget(textlab)
        myLayout.setContentsMargins(0,0,0,0)
        self.setLayout(myLayout)

    def initSet(self):
        pass


    # 重写paintEvent 否则不能使用样式表定义外观
    def paintEvent(self, evt):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)


    def mousePressEvent(self, QMouseEvent):
        print("test")

    def enterEvent(self, QEvent):
        self.setStyleSheet("QWidget{background:#f0f0f0}")
    def leaveEvent(self, QEvent):
        self.setStyleSheet(" QWidget{background:white}")

