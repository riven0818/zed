import json

from Common.Log import logger
import re
class Assert():
    '''判断实际值和期望值是否相等'''
    def __init__(self):
        pass
    def assert_equal(self,actual: dict,expected: dict):
        try:
            if isinstance(actual,str) or isinstance(expected,str):
                if actual == expected:
                    logger.info(r'实际结果：{}和预期结果：{}相等，满足要求,用例执行成功...'.format(actual,expected))
        except:
            logger.info('实际结果和测试结果不等，用例执行失败！！！')

    def assert_in(self,actual,expected,name,response_code=None,ex_status_code=None):
        '''

        :param actual: #实际值
        :param expected: #预期值
        :param name: #用例名称
        :param response_code: #实际返回状态码
        :param ex_status_code: #预期状态码
        :return:
        '''
        # try:
        #     if isinstance(actual,dict) and isinstance(expected,dict):
        #         res = None
        #         for key in expected:
        #             if (key in expected) and (expected[key] == actual[key]):
        #                 res = True
        #             else:
        #                 res = False
        #         assert res is True
        #         return True
        #     else:
        #         assert expected in actual
        #         return True
        # except:
        #     logger.info('dd')
        try:
            if isinstance(actual, dict) and isinstance(expected, dict):
                if response_code == ex_status_code:
                    for key in expected:
                        if (key in actual) and (expected[key] == actual[key]):
                            logger.info('用例:[{}] 执行成功!!!***实际结果: {}包含预期结果: {}\n'.format(name,actual,expected))
                        else:
                            logger.error('用例：【{}】 实际结果: {}不包含或部分包含预期结果：{}，用例不通过，请检查不匹配项!'.format(name,actual,expected))
                else:
                    logger.error('状态码错误，预期状态码为：{}   实际状态码为：{}'.format(expected['code'],response_code))
            else:
                logger.error('预期结果类型：{}或实际结果类型：{}格式有错误，请排查！'.format(type(expected),type(actual)))
        except:
            logger.error('实际结果或预期结果格式不正确，或者实际结果不包含预期结果，请排查！！！')

art = Assert()