'''
编写人：朱斌
工号：zd2228
部门：ICT/研发二部
'''
import pytest
import yaml
from Common.Request import req
from Config import global_conf as conf
def get_yaml():
    with open(conf.casePath_login, encoding='utf-8') as f:
        val = yaml.load(f,Loader=yaml.FullLoader)
    return val

class Test_Login():
    @pytest.mark.parametrize('args',get_yaml())
    def test_login(self,args):
        url = args['requests']['api']
        data = args['requests']['data']
        method = args['requests']['method']
        res = req.send_request(url=url,method=method,data=data)
        print(res[0])
        token = {
            "Access_Token": res[0]['data']['token']
        }
        ##将获取的token写入yaml，供后续使用
        with open(conf.casePath_token, mode='w', encoding='utf-8') as f:
            yaml.dump(token, stream=f, allow_unicode=True)










