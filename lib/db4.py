#coding:utf-8
import pymysql
import sys
sys.path.append("..") #提升包搜索路径
from config import config as cf

#获取连接方法

def get_db_conn():
    coon= pymysql.connect(host=cf.db_host,port=cf.db_port,user=cf.db_user,passwd=cf.db_password,db=cf.db,charset='utf8')

    return coon
#查询操作
def query_db(sql):

    coon=get_db_conn()
    cur=coon.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cf.logging.debug(sql)
    cf.logging.debug(result)
    cur.close()
    coon.close()
    return result

#修改操作
def change_db(sql):
    conn = get_db_conn()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        cf.logging.error(str(e))
    finally:
        cur.close()
        conn.close()



# def check_user(name):
#    result=query_db("select * from user where name='{}'".format(name))
#    print(result)
#
# def del_user(name):
#     sql="delect * from user where name='{}'".format(name)
#     change_db(sql)


if __name__=='__main__':
    #add_user('cyf','123456')
    # check_user("cyf")
    result = query_db("select * from user where name='张三'")
    print(result)