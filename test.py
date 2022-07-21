import re

import pytest
import requests

from Common.YamlRW import yml
from Config import global_conf as conf
expected = {'code':200,'success':True}
# for key in expected:
#     print(key)
#     print(expected[key])
print(expected['code'])

line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
    print ("matchObj.group() : ", matchObj.group())
    print ("matchObj.group(1) : ", matchObj.group(1))
    print ("matchObj.group(2) : ", matchObj.group(2))
    
else:
    print ("No match!!")

tup = ((70,),)
print(tup[0][0])
data = yml.readYaml(f_path=conf.casePath_img_msg)
print('data值：',data)
print(data[0]['caseName'])

# tub = (data[0],data[0]['caseName'])
# print(tub)
new_data = []
for i in range(len(data)):
    tub= data[i],data[i]['caseName']
    new_data.append(tub)

print(new_data)

url = 'http://192.168.9.192:9998/publicMessage/getMessages.idol'
# data = {
#     "userAccount": "admin",
#     "pwd": "21232f297a57a5a743894a0e4a801fc3"
# }
# res = requests.post(url=url,data=data)
res = requests.get(url=url)
#print(res.json())

def ytest(name:str,age:'是个大于0的整数'=52)->'返回值为空':
    headers = {
        "Access-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmODI3YmYxOGVkZDc0MzEyOWI3ODI3Mzg0MGEwMWIyZiIsInVzZXJJZCI6ImY4MjdiZjE4ZWRkNzQzMTI5Yjc4MjczODQwYTAxYjJmIiwidGltZXN0YW1wIjoxNjU3ODcxOTcxNTg5fQ.WlyBjCuy6vSfnSzfcJlc59jOx8OrVAtsUjih5yT333M"
    }
    res =requests.get(url='http://192.168.9.192:9998/publicMessage/getMessages.idol',headers=headers)
    return res
if __name__ == '__main__':
    ytest(name='rose',age=33)