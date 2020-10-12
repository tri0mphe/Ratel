# -*- coding:utf-8 -*-
#@Time : 2020/3/12 19:26
#@Author: Triomphe
#@File : mod_mysql_tool.py

import pymysql
import logging

from modules import mod_get_config
"""
Mysql 工具类
"""
class MySqlTools():
    def __init__(self):
        super().__init__()

    def connect(self):
        """
        连接数据库
        """
        self.cf=mod_get_config.getConfig('db')
        try:
            self.db =pymysql.connect(host=self.cf['db_host'],user=self.cf['db_user'],password=self.cf['db_pass'],database=self.cf['db_name'],port=int(self.cf['db_port']))
            self.cursor =self.db.cursor()
            logging.info('连接数据库成功')
        except:
            logging.error('连接数据库失败')


    def createSQLTable(self,tbname):
        """
        创建通用数据表，默认第一列为主键，名称:ID，类型:INTEGER, 自增
        :param tbname: 数据表名称
        :return: True 成功 False 失败
        """
        curse =self.db.cursor()
        # CREATE TABLE if not exists 表名 (ID INTEGER PRIMARY KEY AUTOINCREMENT);
        command="CREATE TABLE if not exists {} (Myid INT NOT NULL AUTO_INCREMENT, PRIMARY KEY (Myid)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin; ".format(tbname)
        try:
            res =self.cursor.execute(command)
            if res==0:
                return True
            else:
                return False
        except Exception as e:
            raise e



    def createTable(self,tbname,parm):
        """
        有参数的创建数据表
        :param tbname: 表名
        :param parm:字符串格式的要创建的参数
        :return:
        """
        curse = self.db.cursor()
        command = "CREATE TABLE if not exists {} ({}) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin; ".format(tbname,parm)
        # command = u"CREATE TABLE if not exists {} (ID INTEGER PRIMARY KEY AUTOINCREMENT);".format(tbname)
        try:
            res = self.cursor.execute(command)
            if res == 0:
                return True
            else:
                return False
        except Exception as e:
            raise e


    def getSQLTableColumn(self,tablename, column):
        # SELECT 列名 FROM 表名;

        """
        获取某一列的所有值
        :param tablename: 表名
        :param column:列名
        :return:
        """
        command = "SELECT {} FROM {};".format(
            column, tablename)
        value_list = []
        self.cursor.execute(command)
        result =self.cursor.fetchall()
        for row in result:
            value_list.append(row[0])
        return value_list


    #select colunm from tabname where flname =flparam
    def getDataByFiltername(self,tbname,flname,flparam):
        value_list = []
        command ="SELECT * FROM %s WHERE %s = '%s';" % (tbname,flname,flparam)
        print(command)
        self.cursor.execute(command)

        result =self.cursor.fetchall()
        for row in result:
            value_list.append(row)
        return value_list

    def getOneDataByFiltername(self,colname,tbname,flname,flparam):
        value_list = []
        command ="SELECT %s FROM %s WHERE %s = '%s';" % (colname,tbname,flname,flparam)
        print(command)
        self.cursor.execute(command)

        result =self.cursor.fetchall()
        for row in result:
            value_list.append(row)
        return value_list


    def getDataByKeywrods(self,kname):
        command="""SELECT tname,colname FROM keywords as A,table_list as B ,search_table as C where
         (A.kid=C.kid and B.tid=C.tid and kname="{}");""".format(kname)
    #    print(command)
        self.cursor.execute(command)
        value_list = []
        result =self.cursor.fetchall()
        for row in result:
            tem =(row[0],row[1])
            value_list.append(tem)
        return  value_list


    #获取表的所有字段名称
    def getColumnName(self,tbname):
        #select COLUMN_NAME from information_schema.COLUMNS where table_name = 'your_table_name';
        value_list = []
        command = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '{}' and table_schema='{}';".format(tbname,self.cf['db_name'])
        self.cursor.execute(command)
        result = self.cursor.fetchall()
        for row in result:
            value_list.append(row[0])
        return value_list



    #数据库中是否存在表
    def isExistTable(self,tabname):
        command = "SELECT table_name FROM " \
                  "information_schema.TABLES " \
                  "WHERE table_name ='{}';".format(tabname)
        try:
            result =self.cursor.execute(command)
            if result == 0:
                return False
            return True
        except Exception as e:
            pass

    #插入数据
    """
    columns:需要一个列表
    values:需要是一个列表
    """
    def insertData(self,tabname,columns,values):
        #将列表 转换为 字符串
        tem= ["'"+str(i)+"'" for i in values]
        values =",".join(tem)
        tem =[str(i) for i in columns]
        columns=",".join(tem)
        command ="INSERT INTO {} ({}) VALUES ({});".format(
            tabname,columns,values)
        try:
            self.cursor.execute(command)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            return False

    #关闭数据库
    def closeDatabase(self):
        self.db.close()
