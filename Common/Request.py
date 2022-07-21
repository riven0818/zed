import requests
from Config import global_conf
from Common.Log import logger
class Request():
    def __init__(self):
        pass
    def send_request(
            self,
            url: str,
            method: str,
            data=None,
            json=None,
            params=None,
            headers=None,
            files=None,
            ** kwargs
    ):
        '''

        :param url: 请求接口
        :param method: 请求方法
        :param data: 请求参数
        :param params: 请求路径参数
        :param headers: 请求头
        :param files: 文件
        :param kwargs: 其他参数
        :return:
        '''
        self.url = global_conf.url + url
        self.headers = headers
        self.data = data
        self.params = params
        self.json = json
        self.files = files
        pass
        try:
            if method == 'get':
                res = requests.get(url=self.url,headers=self.headers,data=self.data,json=self.json,params=self.params)
                # if res[0]['errMsg'] == '用户未登录':
                #     logger.error('token已过期，请重新获取！！！')
                #     exit()
            elif method == 'post':
                res = requests.post(url=self.url,data=self.data,json=self.json,headers=self.headers,params=params,files=self.files)
                # print(res)
                # if res[0]['errMsg'] == '用户未登录':
                #     logger.warning('token已过期，请重新获取！！！')
                # else:
                #     logger.error(res)
            elif method == 'put':
                res = requests.put(url=self.url,headers=self.headers)
            elif method == 'delete':
                res = requests.delete(url=self.url,headers=headers)
            else:
                print('please add new method ...')
        except Exception :
            logger.error()
        else:
            logger.error('unkown error')
        #logger.info('实际结果为：{}'.format(res.json()))
        return res.json(),res.status_code

req = Request()
