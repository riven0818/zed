'''
编写人：朱斌
工号：zd2228
部门：ICT/研发二部
'''
from Common.YamlRW import yml
from Config import global_conf as conf
from Common.Request import req
from Common.Log import logger
from Common.Assert import art
class Test_taskMgr():
    #初始化参数
    data = yml.readYaml(f_path=conf.casePath_taskManage)
    url = data[0]['requests']['api']
    method = data[0]['requests']['method']
    header = {
        "Access-Token": yml.readYaml(f_path=conf.casePath_token)['Access_Token']
    }
    expected = data[0]['validate']
    casename = data[0]['caseName']
    status_code = data[0]['status_code']
    #创建任务
    def test_createTask(self):
        pass
    #查询任务
    def test_getTaskInfo(self):
        res = req.send_request(url=self.url,method=self.method,headers=self.header)
        art.assert_in(actual=res[0],expected=self.expected,name=self.casename,response_code=res[1],ex_status_code=self.status_code)


