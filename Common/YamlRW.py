import os

import yaml
import os
import re
class Yaml():
    def __init__(self):
        # self.framework_path = os.getcwd()
        # self.pt = re.sub(r"\\","/",self.framework_path,count=0)
        # self.fw_path = re.sub(r"zed.*$",'',self.pt)
        # print(self.fw_path)
        pass
    def readYaml(self,f_path):
        '''

        :param f_path: 要读取的文件路径，如：xxx/x.yaml
        :return:
        '''
        #f_paths = self.fw_path + f_path
        with open(f_path,encoding='utf-8') as f:
            yaml_data = yaml.load(f,Loader=yaml.FullLoader)
        return yaml_data


    def wirteYaml(self,w_ypath,w_val):
        '''

        :param w_ypath: 要写入yaml的路劲和文件名，如：xxx/x.yaml
        :param w_val: 要写入yaml文件的数据
        :return:
        '''
        with open(w_ypath,encoding='utf-8') as f:
            yaml.dump(w_val,stream=f,allow_unicode=True)

    def dataHandle(self,case_path: str):
        '''用于处理测试数据，生成带测试用例名称的列表，供后续allure报告的生成使用

        :param case_path: 用例路径
        :return:
        '''
        data = yml.readYaml(f_path=case_path)
        new_data = []
        for i in range(len(data)):
            tmp = (data[i],data[i]['caseName'])
            new_data.append(tmp)
        return new_data

yml = Yaml()