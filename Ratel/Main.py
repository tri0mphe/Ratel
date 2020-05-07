# -*- coding:utf-8 -*-
#@Time : 2020/3/8 16:18
#@Author: Triomphe
#@File : Main.py

import os,sys
import re
from logging import config
import json

from PyQt5.Qt import *
from PyQt5.QtCore import *

from MainUI import Ui_MainWindow
from importUI import Ui_ImportWindow
from modules import mod_get_rootPath
from modules import mod_mysql_tool
from subDomainScan.Scan import *
from vulscan.vulscan import Vulscan

class MyWindow(Ui_MainWindow,QMainWindow):
    close_signal =pyqtSignal()
    showinfo_siganl =pyqtSignal()
    _signal_sds_stop=pyqtSignal()

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        #获取根目录
        self.root_path =mod_get_rootPath.get_root_path()
        print(self.root_path)
        # 连接数据库
        self.sqldb = mod_mysql_tool.MySqlTools()
        self.sqldb.connect()
        logging.config.fileConfig(self.root_path+'/logs/log.conf',disable_existing_loggers=False)
        logger =logging.getLogger('root')

        self.setupUi(self)
        self.setup()


    #完成所有的逻辑
    def setup(self):
        #信息泄露的所有逻辑
        self.initInfoDisclose()
        #子域名扫描逻辑
        self.initSubDomainScan()

        self.initVulnerabilityScan()

    #初始化子域名扫描------------------------------------

    def initSubDomainScan(self):
        self.sds_initThreadsNum()
        #当前表格的行数
        self.TableCurrentRow_sds=0
        self.progressBar_sds.setMaximum(1751390)
        self.tableWidget_sds.setRowCount(14)
        self.pushButton_sds_start.clicked.connect(self.sds_startScan)
        self.pushButton_sds_stop.clicked.connect(self.sds_stopAllThread)
        self.pushButton_sds_stop.setEnabled(False)

    def sds_initThreadsNum(self):
        ThreadList=[10,20,30,50,80,100,200]
        for i in  ThreadList:
            self.comboBox_sds.addItem(str(i))
        self.comboBox_sds.setCurrentIndex(3)

    def sds_startScan(self):
        if self.lineEdit_sds.text() =="":
            self.statusbar.showMessage('输入域名处不能为空')
            return False
        else:
            domain =self.lineEdit_sds.text()
            if domain.startswith('www.'):
                domain=domain.replace('www.','')
            elif domain.startswith('http'):
                QMessageBox.information(self,'提示','请输入正确格式.如http://baidu.com,则输入baidu.com')
                return False

            #设置开始按钮不可以点击了
            self.pushButton_sds_stop.setEnabled(True)
            self.pushButton_sds_start.setEnabled(False)
            #清空内容
            self.tableWidget_sds.clearContents()
            self.TableCurrentRow_sds=0


            threadNum=int(self.comboBox_sds.currentText())

            self.thread=QThread()

            self.worker=Worker_sds(threadNum, domain, self.root_path + 'data/subdomain_wordlist')
            self.worker._signal_showInfo.connect(self.sds_showInfo2)
            self.worker._signal_progressBar.connect(self.sds_progressBarShow)
            self._signal_sds_stop.connect(self.worker.stop)
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.work)
            # self.thread.finished.connect(self.worker.stop)
            self.thread.start()

            return True
            #1751390

    def sds_progressBarShow(self,int):
        self.progressBar_sds.setValue(int)

    def sds_showInfo2(self,list):
        result=[]
        result.append(list[0]['domainname'])
        result.append(list[0]['ip'])
        result.append(list[0]['Server'])
        result.append(list[0]['code'])

        for j in range(4):
            content =QTableWidgetItem("{}".format(result[j]))
            self.tableWidget_sds.setItem(self.TableCurrentRow_sds, j, content)
        self.TableCurrentRow_sds+=1
        if self.tableWidget_sds.rowCount()<=self.TableCurrentRow_sds:
            self.tableWidget_sds.setRowCount(self.tableWidget_sds.rowCount()+5)
        # print(list[0])

    def sds_stopAllThread(self):
        self._signal_sds_stop.emit()
        self.thread.quit()
        self.pushButton_sds_stop.setEnabled(False)
        self.pushButton_sds_start.setEnabled(True)




    #初始化 漏洞扫描-------------------------------------------------------------
    def initVulnerabilityScan(self):
        self.vs_isRuning=0
        self.TableCurrentRow_vs=0
        self.vs_initTable()
        self.pushButton_vs.clicked.connect(self.vs_scan)



        #test=Vulscan('47.101.152.200')

    #初始化表格
    def vs_initTable(self):
        with open(self.root_path+'/config/config.json','r',encoding='utf-8') as f:
            data =f.read()
        f.close()
        keys =json.loads(data)
        self.vs_headerItems=keys['vul_scan_keys']

        column_count=len(self.vs_headerItems)
        self.tableWidget_vs.setColumnCount(column_count)
        self.tableWidget_vs.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_vs.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.tableWidget_vs.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)

        for i in range(column_count):
            item=QTableWidgetItem()
            item.setForeground(QColor(255,0,0))
            item.setText("{}".format(str(self.vs_headerItems[i])))
            self.tableWidget_vs.setHorizontalHeaderItem(i,item)


    def vs_scan(self):
        #开始为0,表示停止
        if self.lineEdit_vs.text()=='':
            QMessageBox.information(self, '提示', '扫描的内容不能为空', QMessageBox.Yes)
            return
        if self.vs_isRuning ==0:
            self.pushButton_vs.setText('停止扫描')
            self.vs_isRuning=1
            #^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$
            pattern = re.compile(r'^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$')
            if re.match(pattern,self.lineEdit_vs.text()) != None:
                self.vulScanner=Vulscan(self.lineEdit_vs.text())
                self.thread_vs=QThread()
                self.vulScanner._signal.connect(self.vs_showInfo)
                self.vulScanner._signal_finish.connect(self.vs_finishScan)
                self.vulScanner.moveToThread(self.thread_vs)
                self.thread_vs.started.connect(self.vulScanner.start_scan)
                self.thread_vs.start()
            else:
                self.statusbar.showMessage('输入的IP地址格式不正确,请重新输入')
                self.pushButton_vs.setText('开始扫描')
                self.vs_isRuning=0
                return
            return
        else:
            self.pushButton_vs.setText('开始扫描')
            self.vs_isRuning=0
            self.thread_vs.quit()

    def vs_showInfo(self,dict):
        try:
            for i in range(len(self.vs_headerItems)):
                item=QTableWidgetItem()
                item.setText("{}".format(dict[self.vs_headerItems[i]]))
                self.tableWidget_vs.setItem(self.TableCurrentRow_vs, i, item)
            self.TableCurrentRow_vs+=1
            if self.tableWidget_vs.rowCount()<=self.TableCurrentRow_vs:
                self.tableWidget_vs.setRowCount(self.tableWidget_vs.rowCount()+5)
        except Exception as e:
            print(e)


    def vs_finishScan(self):
        self.statusbar.showMessage('扫描已完成.')
        #调用vs_scan 相当于结束扫描
        self.vs_scan()

    # 初始化 信息泄露------------------------------------------------------------------------------

    def initInfoDisclose(self):
        self.id_updateSelectCombox()
        self.id_updateMarkComboxTable()

        self.pushButton_id_search.clicked.connect(self.id_searchData)
        self.pushButton_id_addKeywords.clicked.connect(self.id_addNewKeywords)
        self.pushButton_id_addSign.clicked.connect(self.id_markKeywords)
        #当表发生变化时候,更新列的下拉框
        self.comboBox_id_table.currentIndexChanged.connect(self.id_comTableChanged)
    def id_markKeywords(self):
        if self.comboBox_id_table.currentIndex()!=0 \
                and self.comboBox_id_column.currentIndex()!=0 \
                and self.comboBox_id_keywords.currentIndex()!=0:
            columns =["colname","kid","tid"]
            #获取关键字的kid
            tem=self.sqldb.getOneDataByFiltername("kid","keywords","kname",
                                                  self.comboBox_id_keywords.currentText())
            kid=tem[0][0]
            #获取表的tid
            tem=self.sqldb.getOneDataByFiltername("tid", "table_list", "tname",
                                                  self.comboBox_id_table.currentText())
            tid=tem[0][0]
            values=[self.comboBox_id_column.currentText(),kid,tid]
            res=self.sqldb.insertData("search_table",columns,values)
            if res:
                self.statusbar.showMessage(
                    "将"+self.comboBox_id_keywords.currentText()+
                    "与"+self.comboBox_id_column.currentText()+"标记成功")
            else:
                self.statusbar.showMessage("已存在此标记")

    #标记的时候选择的表名发生变化
    def id_comTableChanged(self):
        if self.comboBox_id_table.currentIndex() !=0:
            res=self.sqldb.getColumnName(self.comboBox_id_table.currentText())
            self.comboBox_id_column.clear()
            for i in res:
                self.comboBox_id_column.addItem(i)

    def id_updateMarkComboxTable(self):
        self.comboBox_id_table.clear()
        self.comboBox_id_column.clear()
        self.comboBox_id_table.addItem("选择数据库")
        result=self.sqldb.getSQLTableColumn("table_list","tname")
        for i in result:
            self.comboBox_id_table.addItem(i)


    #更新两个选择关键字处的下拉框内容
    def id_updateSelectCombox(self):
        self.comboBox_id.clear()
        self.comboBox_id_keywords.clear()
        self.comboBox_id.addItem("请选择关键字")
        self.comboBox_id_keywords.addItem("请选择关键字")
        #从数据库拿出复选框的所有按钮
        data=self.sqldb.getSQLTableColumn("keywords","kname")
        for row in data:
            self.comboBox_id.addItem(row)
            self.comboBox_id_keywords.addItem(row)


    #信息泄露添加新的关键字
    def id_addNewKeywords(self):
        keyword, okPressed = QInputDialog.getText(self, "添加新的关键字", "请输入新的关键字：")
        if okPressed and keyword != '':
            res=self.sqldb.getSQLTableColumn("keywords","kname")
            if keyword in res:
                self.statusbar.showMessage('关键字已存在')
                return
            else:
                columns=["kname"]
                values=[keyword]
                #如果添加成功就更新combobox_id
                if self.sqldb.insertData("keywords",columns,values):
                    self.statusbar.showMessage('关键字添加成功')
                    self.id_updateSelectCombox()
                return True
        else:
            if keyword=='' and okPressed:
                self.statusbar.showMessage('输入的关键字不能为空')
                return False

    #数据查询
    def id_searchData(self):
        if self.lineEdit_id.text()=="":
            reply = QMessageBox.information(self, '提示', '搜索的内容不能为空', QMessageBox.Yes )
            return False
        elif self.comboBox_id.currentIndex() == 0:
            reply = QMessageBox.information(self, '提示', '请选择要搜索的关键字', QMessageBox.Yes)
            return False
        logging.info('尝试信息泄露查询')
        #获取拥有关键字信息的所有表名
        tablelist =self.sqldb.getDataByKeywrods(self.comboBox_id.currentText())
        currentRow =0
        self.tableWidge_id.clear()
        #row[0] 表名 row[1] 列名
        try:
            for row in tablelist:
                #title获取这个表的所有列 result 获取搜索结果
                title=self.sqldb.getColumnName(row[0])
                result=self.sqldb.getDataByFiltername(row[0],row[1],self.lineEdit_id.text())

                #行数和列数,查询结果不为空
                if len(result) !=0:
                    self.rowNum =len(result)+1 #标题+查询结果
                    self.colNum=len(title)

                    self.tableWidge_id.setRowCount(self.rowNum)
                    self.tableWidge_id.setColumnCount(self.colNum)
                    for j in range(self.colNum):
                        content =QTableWidgetItem("{}".format(title[j]))
                        content.setForeground(QBrush(QColor(255, 0, 0)))
                        self.tableWidge_id.setItem(currentRow,j,content)
                    currentRow+=1
                    for i in range(len(result)):
                        for j in range(self.colNum):
                            content =QTableWidgetItem("{}".format(result[i][j]))
                            self.tableWidge_id.setItem(currentRow+i, j, content)
                        currentRow+=1

        except Exception as e:
            print(e)
        #提示查询完成
        self.statusbar.showMessage('查询完成')


def closeEvent(self, event):
        self.close_signal.emit()
        self.close()


#导入数据的窗口
class ImportWindow(Ui_ImportWindow,QWidget):
    def __init__(self, parent=None):
        super(ImportWindow, self).__init__(parent)
        self.setupUi(self)


    def handle_click(self):
        if not self.isVisible():
            self.show()
        pass
    def handle_close(self):
        self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    imWin =ImportWindow()

    myWin.pushButton_id_importData.clicked.connect(imWin.handle_click)
    myWin.close_signal.connect(imWin.close)
    myWin.show()
    sys.exit(app.exec_())
