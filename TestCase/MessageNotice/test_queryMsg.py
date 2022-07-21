import pytest

from Common.YamlRW import yml
from Config import global_conf as conf
from Common.Request import req
from Common.Assert import art
from Common.Mysqldb import mysql
from Common.Log import logger
import datetime

data = yml.readYaml(f_path=conf.casePath_msg)
class Test_MSG():

    @pytest.mark.parametrize('args',data)
    def test_msg(self,args):
        #定义消息标题名称
        title = 'autotest_' + str(datetime.datetime.now().year) + str(datetime.datetime.now().month) + \
                str(datetime.datetime.now().day) + str(datetime.datetime.now().hour) + \
                str(datetime.datetime.now().minute) + \
                str(datetime.datetime.now().second)
        #请求相关参数
        url = args['requests']['api']
        method = args['requests']['method']
        if args['requests']['data'] != None:
            args['requests']['data']['title'] = title
        else:
            pass
        json = args['requests']['data']
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
msg = Test_MSG()
if __name__ == '__main__':
    msg.test_msg()