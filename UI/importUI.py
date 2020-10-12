from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import  QTimer
from PyQt5.QtWidgets import *
import json
import threading
from modules.mod_mysql_tool import MySqlTools
from utility import listUtil

class Ui_ImportWindow(object):
    def setupUi(self,MainWindow):
        self.curTableName=""
        self.sqldb = MySqlTools()
        self.sqldb.connect()
        # 设置宽度
        MainWindow.resize(450, 250)
        #使得窗口永远在最上面
        MainWindow.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.centralwidget = QWidget(MainWindow)
        self.hLayout = QGridLayout(self.centralwidget)
        self.hLayout.setAlignment(Qt.AlignHCenter)
        #选择文件按钮
        lab =QLabel("使用说明：\n1.创建关于导入数据的表名 2.检查表名是否可用\n"
                    " 3.导入数据")
        fileBtn =QPushButton("导入数据")
        fileBtn.clicked.connect(self.importData)

        self.ledit =QLineEdit("请输入表名")


        checkBtn =QPushButton("检查")
        checkBtn.clicked.connect(self.checkTableName)

        self.label =QLabel("test")
        self.label.setAlignment(Qt.AlignBottom)


        self.hLayout.addWidget(lab,0,0,1,3)
        self.hLayout.addWidget(self.ledit,1,0,1,1)
        self.hLayout.addWidget(checkBtn,1,1,1,1)
        self.hLayout.addWidget(fileBtn,1,2,1,1)

        self.hLayout.addWidget(self.label)



    #打开文件
    def importData(self):
        if self.ledit.text() =="":
            QMessageBox.information(self, "Tip", "表名不能为空")
            return False
        reply = QMessageBox.information(self,'提示','目前只支持json格式导入,格式为[{},{},...]',QMessageBox.Yes|QMessageBox.No)
        if reply ==QMessageBox.Yes:
            self.fileNmae =QFileDialog()
            file=self.fileNmae.getOpenFileName(self,'Open file','/','JSON configuration file (*.json)')
            # print(file)
            #导入数据
            self.label.setText("开始导入数据,请等待")
            thread =threading.Thread(target=self.importDatas(file[0],self.ledit.text()))
            thread.setDaemon(True)
            thread.start()

    def checkTableName(self):
        text =self.ledit.text()
        if self.sqldb.isExistTable(text):
            QMessageBox.information(self,"Tip","当前表名存在,请换一个.")
        elif self.ledit.text()=="":
            QMessageBox.information(self,"Tip","不能为空")
        else:
            QMessageBox.information(self,"Tip","表名可用")

    def importDatas(self,filenames, tabname):
        sqldb = MySqlTools()
        sqldb.connect()
        result = []
        self.label.setText("正在导入数据,请稍等................")
        try:
            with open(filenames, 'r', encoding='utf-8') as f:
                data = f.read()
                # 解决错误问题
                if data.startswith(u'\ufeff'):
                    data = data.encode('utf8')[3:].decode('utf8')
            f.close()
            # print(data)
            try:
                result = json.loads(data)

            except TypeError:
                print("json格式错误")
        except IOError:
            print("读取文件失败")

        # 如果表名不存在
        if not sqldb.isExistTable(tabname):
            self.curTableName=tabname
            fields = listUtil.listValueLen(result)
            list = []
            keylist = []
            for i in fields:
                if fields[i] != 0:
                    keylist.append(i)
                    list.append(" " + i + " varchar(" + str(fields[i]) + ")")
            parameter = ",".join(list)
            flag = sqldb.createTable(tabname, parameter)
            # 创建成功返回true

            if flag:
                print("开始导入数据")
                for i in range(len(result)):
                    values = []
                    for j in keylist:
                        values.append(str(result[i][j]))
                    sqldb.insertData(tabname, keylist, values)
            self.label.setText("数据导入成功")

            #将表名放入数据库
            columns=["tname"]
            values=[tabname]
            sqldb.insertData("table_list",columns,values)
