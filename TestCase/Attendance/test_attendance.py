'''
编写人：朱斌
工号：zd2228
部门：ICT/研发二部
'''
import allure
import pytest

from Common.YamlRW import yml
from Config import global_conf as conf
from Common.Request import req
from Common.Log import logger
from Common.Assert import art
class Test_Attendance():
    data = yml.readYaml(f_path=conf.casePath_attendance)
    @allure.title('时间段查询')
    def test_attendance(self):
        tmp = attend.data
        url = tmp[0]['requests']['api']
        method = tmp[0]['requests']['method']
        json = tmp[0]['requests']['data']
        headers = {
            "Access-Token": yml.readYaml(f_path=conf.casePath_token)['Access_Token'],
            "Content-Type": conf.DEFAULT_HEADERS['Content-Type']
        }
        expected = tmp[0]['validate']
        casename = tmp[0]['caseName']
        status_code = tmp[0]['status_code']
        res = req.send_request(url=url,method=method,json=json,headers=headers)
        if res[0]['errMsg'] == '用户未登录':
            logger.error('token已过期，请重新获取！！！')
        else:
            art.assert_in(actual=res[0],expected=expected,name=casename,response_code=res[1],ex_status_code=status_code)
    @allure.title('部门查询')
    def test_query_department(self):
        tmp = attend.data
        url = tmp[1]['requests']['api']
        method = tmp[1]['requests']['method']
        json = tmp[1]['requests']['data']
        headers = {
            "Access-Token": yml.readYaml(f_path=conf.casePath_token)['Access_Token'],
            "Content-Type": conf.DEFAULT_HEADERS['Content-Type']
        }
        expected = tmp[1]['validate']
        casename = tmp[1]['caseName']
        status_code = tmp[1]['status_code']
        res = req.send_request(url=url, method=method,json=json, headers=headers)
        if res[0]['errMsg'] == '用户未登录':
            logger.error('token已过期，请重新获取！！！')
        else:
            art.assert_in(actual=res[0], expected=expected, name=casename, response_code=res[1],
                          ex_status_code=status_code)
    @allure.title('姓名查询')
    def test_query_name(self):
        tmp = attend.data
        url = tmp[2]['requests']['api']
        method = tmp[2]['requests']['method']
        json = tmp[2]['requests']['data']
        headers = {
            "Access-Token": yml.readYaml(f_path=conf.casePath_token)['Access_Token'],
            "Content-Type": conf.DEFAULT_HEADERS['Content-Type']
        }
        expected = tmp[2]['validate']
        casename = tmp[2]['caseName']
        status_code = tmp[2]['status_code']
        res = req.send_request(url=url, method=method,json=json, headers=headers)
        if res[0]['errMsg'] == '用户未登录':
            logger.error('token已过期，请重新获取！！！')
        else:
            art.assert_in(actual=res[0], expected=expected, name=casename, response_code=res[1],
                          ex_status_code=status_code)
    @allure.title("职位查询")
    def test_query_position(self):
        tmp = attend.data
        url = tmp[3]['requests']['api']
        method = tmp[3]['requests']['method']
        json = tmp[3]['requests']['data']
        headers = {
            "Access-Token": yml.readYaml(f_path=conf.casePath_token)['Access_Token'],
            "Content-Type": conf.DEFAULT_HEADERS['Content-Type']
        }
        expected = tmp[3]['validate']
        casename = tmp[3]['caseName']
        status_code = tmp[3]['status_code']
        res = req.send_request(url=url, method=method, json=json, headers=headers)
        if res[0]['errMsg'] == '用户未登录':
            logger.error('token已过期，请重新获取！！！')
        else:
            art.assert_in(actual=res[0], expected=expected, name=casename, response_code=res[1],
                          ex_status_code=status_code)
attend = Test_Attendance()

if __name__ == '__main__':
    pytest.main(['-vs','./attendance.py'])