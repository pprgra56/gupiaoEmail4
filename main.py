# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import tushare as ts
import pandas as pd

#发送邮件
def sendEmail(title,title2,text):

    email_user = 'pprgra56@126.com'
    email_pass = 'ShiT52115211'
    # 第三方 SMTP 服务
    mail_host = "smtp.126.com" # 设置服务器
    mail_user = "pprgra56@126.com" # 用户名
    mail_pass = "ICAHEIMKOIKDUWCO" # 口令
    sender = 'pprgra56@126.com'
    receivers = ['pprgra56@126.com'] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    message = MIMEText(text, 'plain', 'utf-8')
    message['From'] = Header(title) # 27
    message['To'] = Header("MINE")
    subject = title2 # 54
    message['Subject'] = Header(subject, 'utf-8')
    try:

        smtpObj = smtplib.SMTP()

        smtpObj.connect(mail_host, 25) # 25 为 SMTP 端口号

        smtpObj.login(mail_user, mail_pass)

        smtpObj.sendmail(sender, receivers, message.as_string())

        print("fasong ok")

    except smtplib.SMTPException:

        print("fasong buok")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    
    # 显示所有列

    pd.set_option('display.max_columns', None)

    # 显示所有行

    pd.set_option('display.max_rows', None)


    token = "4f04c552120afb0d76d0aaedb27e8ed2274373a6fba1a567439ea846"

    pro = ts.pro_api(token)

    df =pro.stock_company(tscode='600518',exchange='SZSE',fields='ts_code,chairman,manager,province,city')

    yibo = 20000

    erbo = 30000

    shanbo = 50000

    ts_code = '002676.SZ'

    time_begin = '20220610'

    time_end = '20220614'

    info = pro.daily(ts_code=ts_code, start_date=time_begin, end_date=time_end)

    print(info)
    sendEmail('PyCharm',"96_你好,世界",info['high'][0])
    
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
