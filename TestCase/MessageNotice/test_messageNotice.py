'''
编写人：朱斌
工号：zd2228
部门：ICT/研发二部
'''
import pytest

from Common.YamlRW import yml
from Config import global_conf as conf
from Common.Request import req
from Common.Assert import art
from Common.Mysqldb import mysql
from Common.Log import logger
import datetime
class Test_MSG():
    data = yml.readYaml(f_path=conf.casePath_msg)
    #读取要删除的消息的测试数据
    data1 = yml.readYaml(f_path=conf.casePath_del_msg)
    # 定义消息标题名称
    title = 'autotest_' + str(datetime.datetime.now().year) + str(datetime.datetime.now().month) + \
            str(datetime.datetime.now().day) + str(datetime.datetime.now().hour) + \
            str(datetime.datetime.now().minute) + \
            str(datetime.datetime.now().second)
    @pytest.mark.parametrize('args',data)
    def test_msg(self,args):

        #请求相关参数
        url = args['requests']['api']
        method = args['requests']['method']
        if args['requests']['data'] != None:
            args['requests']['data']['title'] = cls.title
        else:
            pass
        json = args['requests']['data']

        if args['requests']['params'] != None:
            args['requests']['params']['title'] = cls.title
        else:
            pass
        params = args['requests']['params']
        headers = {
            "Access-Token": yml.readYaml(f_path=conf.casePath_token)['Access_Token'],
            "Content-Type": conf.DEFAULT_HEADERS['Content-Type']
        }
        expected = args['validate']
        casename = args['caseName']
        status_code = args['status_code']

        res = req.send_request(url=url,method=method,json=json,headers=headers,params=params)


        if res[0]['errMsg'] == '用户未登录':
            logger.error('token已过期，请重新获取！！！')
        else:
            art.assert_in(actual=res[0],expected=expected,name=casename,response_code=res[1],ex_status_code=status_code)
    @pytest.mark.parametrize('args',data1)
    def test_delMsg(self,args):
        # 获取要删除的消息id
        result = mysql.queryDB(db_name=conf.dbName, tb_name='public_message', q_field='id',
                               conditions='title = "{}"'.format(cls.title))
        print(result)
        #请求参数
        url = args['requests']['api']
        method = args['requests']['method']
        params = args['requests']['params']
        if args['requests']['data'] != None:
            args['requests']['data']['id'] = result[0][0]
        else:
            pass
        json = args['requests']['data']
        headers = {
            "Access-Token": yml.readYaml(f_path=conf.casePath_token)['Access_Token'],
            "Content-Type": conf.DEFAULT_HEADERS['Content-Type']
        }
        expected = args['validate']
        casename = args['caseName']
        status_code = args['status_code']
        res = req.send_request(url=url, method=method, json=json, headers=headers, params=params)
        if res[0]['errMsg'] == '用户未登录':
            logger.error('token已过期，请重新获取！！！')
        else:
            art.assert_in(actual=res[0],expected=expected,name=casename,response_code=res[1],ex_status_code=status_code)

cls = Test_MSG