#-*-coding:utf8-*-

import MySQLdb
import sys
#配置信息
reload(sys)
sys.setdefaultencoding('utf-8')

user = ''
password = ''
host = ''
db = ''
charset = ''
conn = None

#连接数据库
def getConn():
    conn = MySQLdb.connect(user=user, passwd=password, host=host, db=db, charset=charset)
    return conn

#查询操作
def getResult(sql, N=0):
    cur = conn.cursor()
    cur.execute(sql)
    if N == 0:
        result = cur.fetchall()
    elif N == 1:
        result = cur.fetchone()
    else:
        result = cur.fetchmany(N)
    cur.close()
    return result

#插入操作
def insertResult(sql, values=None):
    cur = conn.cursor()
    if values is None:
        tag = cur.execute(sql)
    else:
        tag = cur.executemany(sql, values)
    conn.commit()
    cur.close()
    if tag > 0:
        return True
    else:
        return False

#删除操作
def deleteResult(sql):
    cur = conn.cursor()
    tag = cur.execute(sql)
    conn.commit()
    cur.close()
    if tag > 0:
        return True
    else:
        return False

#关闭数据库连接
def colseConn():
    conn.close()
