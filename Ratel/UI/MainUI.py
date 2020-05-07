# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import logging
import customWidget

from modules.mod_get_rootPath import get_root_path

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.root_path =get_root_path()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1101, 755)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #设置左边布局
        with open(self.root_path+'/UI/QSS/tabStyle.qss','r',encoding='utf-8') as f:
            self.tabStyle =f.read()
            f.close()

        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(4, 5, 4, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("MaintabWidget")
        self.tabWidget.setStyleSheet(self.tabStyle)


        self.tab_infoGather = QWidget()
        self.tab_infoGather.setObjectName("tab_infoGather")
        self.gridLayout_2 = QGridLayout(self.tab_infoGather)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget_infoGathe = QTabWidget(self.tab_infoGather)
        self.tabWidget_infoGathe.setObjectName("tabWidget_infoGathe")

        #子域名扫描-----------------------------------------
        self.tab_subDomainScan = QWidget()
        self.tab_subDomainScan.setObjectName("tab_subDomainScan")
        self.gridLayout_4 = QGridLayout(self.tab_subDomainScan)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.label_sds_1 = QLabel(self.tab_subDomainScan)
        self.label_sds_1.setObjectName("label_sds_1")
        self.gridLayout_4.addWidget(self.label_sds_1, 0, 0, 1, 1)

        self.lineEdit_sds = QLineEdit(self.tab_subDomainScan)
        self.lineEdit_sds.setObjectName("lineEdit_sds")
        self.gridLayout_4.addWidget(self.lineEdit_sds, 0, 1, 1, 1)

        self.pushButton_sds_start = QPushButton(self.tab_subDomainScan)
        self.pushButton_sds_start.setObjectName("pushButton_sds_start")
        self.gridLayout_4.addWidget(self.pushButton_sds_start, 0, 2, 1, 1)

        self.pushButton_sds_stop = QPushButton(self.tab_subDomainScan)
        self.pushButton_sds_stop.setObjectName("pushButton_sds_stop")
        self.gridLayout_4.addWidget(self.pushButton_sds_stop, 0, 3, 1, 1)

        self.checkBox_sds_threadNum = QCheckBox(self.tab_subDomainScan)
        self.checkBox_sds_threadNum.setObjectName("checkBox_sds_threadNum")
        self.gridLayout_4.addWidget(self.checkBox_sds_threadNum, 0, 4, 1, 1)

        self.label_sds_2 = QLabel(self.tab_subDomainScan)
        self.label_sds_2.setText('线程数')
        self.label_sds_2.setObjectName("label_sds_2")
        self.gridLayout_4.addWidget(self.label_sds_2, 0, 5, 1, 1)

        self.comboBox_sds = QComboBox(self.tab_subDomainScan)
        self.comboBox_sds.setObjectName("comboBox_sds")
        self.gridLayout_4.addWidget(self.comboBox_sds, 0, 6, 1, 1)


        self.tableWidget_sds = QTableWidget(self.tab_subDomainScan)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_sds.sizePolicy().hasHeightForWidth())
        self.tableWidget_sds.setSizePolicy(sizePolicy)
        self.tableWidget_sds.setColumnCount(4) #设置列数
        self.tableWidget_sds.setObjectName("tableWidget_sds")
        # self.tableWidget_sds.setRowCount(0) #设置行数
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_sds.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget_sds.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget_sds.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tableWidget_sds.setHorizontalHeaderItem(3, item)
        # self.tableWidget_sds.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_sds.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_sds.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_sds.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        # self.tableWidget_sds.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tableWidget_sds.verticalHeader().setDefaultSectionSize(6)

        self.gridLayout_4.addWidget(self.tableWidget_sds, 1, 0, 1, 7)

        self.progressBar_sds =QProgressBar(self.tab_subDomainScan)
        self.progressBar_sds.setObjectName("progressBar_sds")
        self.gridLayout_4.addWidget(self.progressBar_sds, 2, 0, 1, 7)

        self.tabWidget_infoGathe.addTab(self.tab_subDomainScan, "")



        self.tab_12 = QWidget()
        self.tab_12.setObjectName("tab_12")
        self.gridLayout_5 = QGridLayout(self.tab_12)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_3 = QLabel(self.tab_12)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 6, 0, 1, 1)
        self.comboBox_6 = QComboBox(self.tab_12)
        self.comboBox_6.setObjectName("comboBox_6")
        self.gridLayout_5.addWidget(self.comboBox_6, 4, 1, 1, 1)
        self.tableWidget_2 = QTableWidget(self.tab_12)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.gridLayout_5.addWidget(self.tableWidget_2, 7, 0, 1, 6)
        self.checkBox = QCheckBox(self.tab_12)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_5.addWidget(self.checkBox, 3, 4, 1, 1)
        self.label_7 = QLabel(self.tab_12)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 4, 0, 1, 1)
        self.checkBox_2 = QCheckBox(self.tab_12)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_5.addWidget(self.checkBox_2, 3, 5, 1, 1)
        self.lineEdit_2 = QLineEdit(self.tab_12)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_5.addWidget(self.lineEdit_2, 2, 1, 1, 3)
        self.label_5 = QLabel(self.tab_12)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 6, 4, 1, 1)
        self.label_2 = QLabel(self.tab_12)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 2, 0, 1, 1)
        self.pushButton_5 = QPushButton(self.tab_12)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_5.addWidget(self.pushButton_5, 2, 4, 1, 1)
        self.label_6 = QLabel(self.tab_12)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 3, 0, 1, 1)
        self.pushButton_6 = QPushButton(self.tab_12)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_5.addWidget(self.pushButton_6, 2, 5, 1, 1)
        self.checkBox_3 = QCheckBox(self.tab_12)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_5.addWidget(self.checkBox_3, 4, 4, 1, 1)
        self.label_4 = QLabel(self.tab_12)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 6, 3, 1, 1)
        self.listWidget_2 = QListWidget(self.tab_12)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout_5.addWidget(self.listWidget_2, 3, 3, 2, 1)
        self.comboBox_5 = QComboBox(self.tab_12)
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout_5.addWidget(self.comboBox_5, 3, 1, 1, 1)
        self.listWidget = QListWidget(self.tab_12)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_5.addWidget(self.listWidget, 3, 2, 2, 1)
        self.checkBox_4 = QCheckBox(self.tab_12)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_5.addWidget(self.checkBox_4, 4, 5, 1, 1)
        self.tabWidget_infoGathe.addTab(self.tab_12, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName("tab_13")
        self.tabWidget_infoGathe.addTab(self.tab_13, "")
        self.gridLayout_2.addWidget(self.tabWidget_infoGathe, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_infoGather, "")
        self.tab_infoDisclose = QWidget()
        self.tab_infoDisclose.setObjectName("tab_infoDisclose")
        self.gridLayout_3 = QGridLayout(self.tab_infoDisclose)
        self.gridLayout_3.setObjectName("gridLayout_3")

        """
        信息泄露查询UI--------------------------------------------
        """
        self.lineEdit_id = QLineEdit(self.tab_infoDisclose)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.gridLayout_3.addWidget(self.lineEdit_id, 0, 0, 1, 3)

        self.comboBox_id = QComboBox(self.tab_infoDisclose)
        self.comboBox_id.setObjectName("comboBox_id")
        self.comboBox_id.setMaximumWidth(150)
        self.gridLayout_3.addWidget(self.comboBox_id, 0, 3, 1, 1)


        self.pushButton_id_search = QPushButton(self.tab_infoDisclose)
        self.pushButton_id_search.setObjectName("pushButton_id_search")
        self.pushButton_id_search.setMaximumWidth(110)
        self.gridLayout_3.addWidget(self.pushButton_id_search, 0, 4, 1, 1)

        self.pushButton_id_addKeywords = QPushButton(self.tab_infoDisclose)
        self.pushButton_id_addKeywords.setObjectName("pushButton_id_addKeywords")
        self.pushButton_id_addKeywords.setMaximumWidth(110)
        self.gridLayout_3.addWidget(self.pushButton_id_addKeywords, 1, 0, 1, 1)

        self.pushButton_id_importData = QPushButton(self.tab_infoDisclose)
        self.pushButton_id_importData.setObjectName("pushButton_id_importData")
        self.pushButton_id_importData.setMaximumWidth(110)
        self.gridLayout_3.addWidget(self.pushButton_id_importData, 1, 1, 1, 1)

        self.signAreaWidget = QWidget(self.tab_infoDisclose)
        self.signAreaWidget.setStyleSheet("QWidget#signAreaWidget{border:2px solid #808a87 }")
        self.signAreaWidget.setObjectName("signAreaWidget")
        self.horizontalLayout = QHBoxLayout(self.signAreaWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_id = QLabel(self.signAreaWidget)
        self.label_id.setObjectName("label_id")
        self.label_id.setMaximumWidth(80)
        self.horizontalLayout.addWidget(self.label_id)
        #选择数据库的某个表
        self.comboBox_id_table = QComboBox(self.signAreaWidget)
        self.comboBox_id_table.setObjectName("comboBox_id_table")
        self.horizontalLayout.addWidget(self.comboBox_id_table)
        #选择数据库的某列
        self.comboBox_id_column = QComboBox(self.signAreaWidget)
        self.comboBox_id_column.setObjectName("comboBox_id_column")
        self.horizontalLayout.addWidget(self.comboBox_id_column)
        #关键字
        self.comboBox_id_keywords = QComboBox(self.signAreaWidget)
        self.comboBox_id_keywords.setObjectName("comboBox_id_keywords")
        self.horizontalLayout.addWidget(self.comboBox_id_keywords)
        #标记按钮
        self.pushButton_id_addSign = QPushButton(self.signAreaWidget)
        self.pushButton_id_addSign.setObjectName("pushButton_id_addSign")
        self.horizontalLayout.addWidget(self.pushButton_id_addSign)
        self.gridLayout_3.addWidget(self.signAreaWidget, 1, 2, 1, 3)

        self.tableWidge_id = QTableWidget(self.tab_infoDisclose)
        self.tableWidge_id.setObjectName("tableWidge_id")
        self.tableWidge_id.setColumnCount(0)
        self.tableWidge_id.setRowCount(0)
        self.gridLayout_3.addWidget(self.tableWidge_id, 2, 0, 1, 5)

        self.tabWidget.addTab(self.tab_infoDisclose, "")

        """
        ------------------------------------------------------------------------------------------
        漏洞扫描 vulnerability scan 
        """
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_6 = QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.comboBox_vs = QComboBox(self.tab_3)
        self.comboBox_vs.setObjectName("comboBox_vs")
        self.gridLayout_6.addWidget(self.comboBox_vs, 0, 1, 1, 1)
        self.lineEdit_vs = QLineEdit(self.tab_3)
        self.lineEdit_vs.setObjectName("lineEdit_vs")
        self.gridLayout_6.addWidget(self.lineEdit_vs, 0, 0, 1, 1)
        self.pushButton_vs = QPushButton(self.tab_3)
        self.pushButton_vs.setObjectName("pushButton_vs")
        self.gridLayout_6.addWidget(self.pushButton_vs, 0, 2, 1, 1)
        self.tableWidget_vs = QTableWidget(self.tab_3)
        self.tableWidget_vs.setObjectName("tableWidget_vs")
        self.tableWidget_vs.setColumnCount(0)
        self.tableWidget_vs.setRowCount(10)
        self.gridLayout_6.addWidget(self.tableWidget_vs, 1, 0, 1, 3)
        self.tabWidget.addTab(self.tab_3, "")

        """
        --------------------------------------------------------------------------------
        """

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 1101, 26))
        self.menubar.setObjectName("menubar")
        self.menutest1 = QMenu(self.menubar)
        self.menutest1.setObjectName("menutest1")

        #菜单栏
        MainWindow.setMenuBar(self.menubar)

        #状态栏
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menutest1.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_infoGathe.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_sds_1.setText(_translate("MainWindow", "域名"))
        self.pushButton_sds_start.setText(_translate("MainWindow", "开始"))
        self.pushButton_sds_stop.setText(_translate("MainWindow", "停止"))
        self.checkBox_sds_threadNum.setText(_translate("MainWindow", "test1"))
        item = self.tableWidget_sds.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "域名"))
        item = self.tableWidget_sds.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "IP地址"))
        item = self.tableWidget_sds.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Web服务器"))
        item = self.tableWidget_sds.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "状态码"))
        self.tabWidget_infoGathe.setTabText(
            self.tabWidget_infoGathe.indexOf(self.tab_subDomainScan),
            _translate("MainWindow", "子域名扫描"))
        self.label_3.setText(_translate("MainWindow", "扫描信息"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.label_7.setText(_translate("MainWindow", "超时"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "域名"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.label_6.setText(_translate("MainWindow", "线程数"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.checkBox_4.setText(_translate("MainWindow", "CheckBox"))
        self.tabWidget_infoGathe.setTabText(self.tabWidget_infoGathe.indexOf(self.tab_12), _translate("MainWindow", "后台扫描"))
        self.tabWidget_infoGathe.setTabText(self.tabWidget_infoGathe.indexOf(self.tab_13), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_infoGather), _translate("MainWindow", "信息搜集"))
        self.pushButton_id_addKeywords.setText(_translate("MainWindow", "添加关键字"))
        self.pushButton_id_search.setText(_translate("MainWindow", "搜索"))
        self.label_id.setText(_translate("MainWindow", "标记关键字"))
        self.pushButton_id_addSign.setText(_translate("MainWindow", "标记"))
        self.pushButton_id_importData.setText(_translate("MainWindow", "导入数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_infoDisclose), _translate("MainWindow", "信息泄露查询"))
        self.pushButton_vs.setText(_translate("MainWindow", "开始扫描"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "漏洞扫描"))
        self.menutest1.setTitle(_translate("MainWindow", "test1"))
