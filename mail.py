from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_mail(score):
	from_addr = 'xxxx@163.com'	# 发送邮件的 163 邮箱
	password = 'xxxx'
	to_addr = 'xxxx@qq.com'		# 接受邮件的 qq 邮箱
	smtp_server = 'smtp.163.com'

	msg = MIMEText(score, 'plain', 'utf-8')
	msg['From'] = _format_addr('教务系统 <%s>' % from_addr)
	msg['To'] = _format_addr('成绩单 <%s>' % to_addr)
	msg['Subject'] = Header('我的成绩单', 'utf-8').encode()

	server = smtplib.SMTP_SSL(smtp_server, 465)
	server.set_debuglevel(1)
	server.login(from_addr, password)
	server.sendmail(from_addr, [to_addr], msg.as_string())
	server.quit()