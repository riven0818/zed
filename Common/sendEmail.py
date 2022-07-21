#发送邮件到指定邮箱
"""
python对SMTP支持有 smtplib 和 email 两个模块
email负责构造邮件
smtplib负责发送邮件，他对smtp协议进行了简单的封装
"""
import smtplib
from email.mime.text import MIMEText  # 邮件正文
from email.header import Header  # 邮件头
from email.mime.multipart import MIMEMultipart

def send_email(receives,title):
    '''

    :param receives: 接收者邮箱地址，多个邮箱格式为列表，如['xxx','xxxx',...]
    :param title: 邮件的标题
    :return:
    '''
    #登陆服务器
    smtp_obj = smtplib.SMTP_SSL("smtp.exmail.qq.com", '465')  # 发送人邮箱中的SMTP服务器  端口号
    smtp_obj.login("zhubin@zeditech.com","Riven@0818")  # 发件人邮箱账号和邮箱密码
    #smtp_obj.set_debuglevel(1)  # 显示调试信息
    print('发送对象的邮箱为：',receives)
    msg = MIMEMultipart()
    msg["From"] = Header("载德科技")  # 发送者
    msg["To"] = Header("朱斌", 'utf-8')  # 接受者
    msg['Subject'] = Header(title, 'utf-8')  # 主题

    # 读取文件
    f = open('../report.html', 'r')  # 更改成自己报告的的路径
    str_html = f.read()
    f.close()

    # 正文
    msg.attach(MIMEText(str_html,'html','utf-8'))
    # 构造附件
    att1 = MIMEText(open('../report.html', 'rb').read(), 'base64', 'utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    att1['Content-Disposition'] = 'attachment; filename= "index.html"'
    msg.attach(att1)

    # 发邮件
    #smtp_obj = smtplib.SMTP('localhost')
    smtp_obj.sendmail("zhubin@zeditech.com",receives, msg.as_string())
    print('email seed success')
    # smtp_obj.quit()

if __name__ == '__main__':
    send_email(receives=['zhubin@zeditech.com','1358207838@qq.com'],title='allure测试报告')