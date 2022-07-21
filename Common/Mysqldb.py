import pymysql
from Config import global_conf as conf
#连接数据库
db = pymysql.Connect(host=conf.dbHost,port=conf.dbPort,user=conf.dbUser,password=conf.dbPwd,database=conf.dbName,charset="")
#创建游标对象
cur = db.cursor()
#数据库类
class Mysql():
    def __init__(self):
        pass
    def queryDB(self,db_name:str,tb_name:str,q_field=None,conditions=None)->'返回值注释':
        '''

        :param db_name: 数据库名称
        :param tb_name: 表名称
        :param q_field: 表字段名称
        :param conditions: 查询条件
        :return: res查询结果
        '''
        sql = 'select {} from {}.{} where {}'.format(q_field,db_name,tb_name,conditions)
        print('\nsql语句为：\n',sql)
        cur.execute(sql)
        res = cur.fetchall()
        print(res)
        cur.close()
        return res
    def deleteDB(self,db_name:str,tb_name:str,del_field:str):
        '''

        :param db_name: 数据库名称
        :param tb_name: 表名称
        :param del_field: 表字段名称
        :return:
        '''
        sql = 'delete from {}.{} where {}'.format(db_name,tb_name,del_field)
        print('\nsql语句为：\n',sql)
        cur.execute(sql)
        cur.connection.commit()
        cur.close()
    def changeDB(self,db_name:str,tb_name:str,chg_field:str,new_val,conditions):
        '''

        :param db_name: 数据库名称
        :param tb_name: 表名称
        :param chg_field: 修改的字段名称
        :param new_val: 修改字段新的值
        :param conditions: 条件
        :return:
        '''
        sql = "update {}.{} set {} = '{}' where {}".format(db_name,tb_name,chg_field,new_val,conditions)
        print('\nsql语句为：\n',sql)
        cur.execute(sql)
        cur.connection.commit()
        cur.close()
    def insertDB(self,db_name:str,tb_name:str,insert_field,val):
        '''注意哪些是非空字段

        :param db_name: 数据库名称
        :param tb_name: 表名称
        :param insert_field: 要插入的字段，多表字段格式为，"A,B,..."逗号隔开
        :param val: 表字段数据，和insert_field对应，多数值格式为："'value1','value2',..."逗号隔开
        :return:
        '''
        sql =  "insert into {}.{}({}) values({})".format(db_name,tb_name,insert_field,val)
        print('\nsql语句为：\n', sql)
        cur.execute(sql)
        cur.connection.commit()
        cur.close()

mysql = Mysql()
if __name__ == '__main__':
    t =mysql.queryDB(db_name='shuoan',tb_name='public_message',q_field='id',conditions='title = "autotest_2022623114116"')
    print(t)
    # mysql.deleteDB(db_name='shuoan',tb_name='public_message',del_field='id = 57')
    # mysql.changeDB(db_name='shuoan',tb_name='public_message',chg_field='img_id',new_val='123',conditions='id = 106')
    # mysql.insertDB(db_name='shuoan',tb_name='public_message',insert_field='title,content',val="'自动化数据库测试','aha'")
    cur.close()