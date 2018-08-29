import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os


def sendmail(send_to = "xxxxxxxxx@qq.com"):
    result_dir = "./report"
    if not os._exists(result_dir):
        os.mkdir(result_dir)
    lists = os.listdir(result_dir)

    lists.sort(key=lambda fn:os.path.getmtime(result_dir+'/'+fn))

    print("发送的文件是"+lists[-1])

    filename=os.path.join(result_dir,lists[-1])

    smtpserver = "smtp.sina.com"
    user = "wdid17@sina.com"
    password = "xxxxxx"

    sender = "wdid17@sina.com"
    receiver = send_to
    subject = "开始测试Python SMTP"

    # 发送的附件
    sendfile = open(filename, 'rb').read()

    att = MIMEText(sendfile, 'base64', 'utf-8')
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment;filename="%s"' % lists[-1]
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = Header(subject, 'utf-8')
    msgRoot['From'] = Header(user)
    msgRoot.attach(att)
    msgRoot.attach(MIMEText('发送测试报告结果', 'plain', 'utf-8'))
    smtp = smtplib.SMTP()
    # 开始发邮件
    print("发送邮件给%s"%receiver)
    smtp.connect(smtpserver)
    print("建立连接")
    smtp.login(user, password)
    print("用户登录")
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    print("发邮件")
    smtp.quit()
    print("退出")

if __name__ == "__main__":
    sendmail()
