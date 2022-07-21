'''
编写人：朱斌
工号：zd2228
部门：ICT/研发二部
'''
import allure
import pytest
import yaml
from Common.Request import req
from Common.Assert import art
from Config import global_conf as conf
def read_yaml():
    with open(conf.casePath_sysManage,encoding='utf-8') as f:
        val = yaml.load(f,Loader=yaml.FullLoader)
    return val
def read_token():
    with open(conf.casePath_token,encoding='utf-8') as f:
        val = yaml.load(f,Loader=yaml.FullLoader)
    return val
@allure.epic('系统管理')
class Test_sysMgr():
    @allure.title('系统管理')
    @allure.tag('系统管理相关测试')
    @pytest.mark.parametrize('args',read_yaml())
    def test_get_data(self,args):
        url = args['requests']['api']
        params = args['requests']['params']
        method = args['requests']['method']
        headers = {
            "Access-Token": read_token()['Access_Token']
        }
        status_code = args['status_code']
        result = req.send_request(url=url,method=method,data='',params=params,headers=headers)
        art.assert_in(actual=result,expected=args['validate'],name=args['caseName'],response_code=result[1],ex_status_code=status_code)
if __name__ == '__main__':
    pytest.main(['vs','./sysMnage.py'])