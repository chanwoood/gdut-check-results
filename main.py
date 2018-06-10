import requests
import json
import time
import datetime

from mail import send_mail
from login import ss, headers, sso

total = 4	# 表示当前教务系统中成绩记录条数

def main():
	global total

	data = {
		'xnxqdm': '201702',
		'page': 1,
		'rows': 50,
		'sort': 'xnxqdm',
		'order': 'asc',
	}

	url = 'http://jxfw.gdut.edu.cn/xskccjxx!getDataList.action'
	rsp = ss.post(url, headers=headers, data=data)
	score = rsp.json()

	try:
		newtotal = score.get('total')
		if newtotal:
			print('{}查询成功！'.format(datetime.datetime.utcnow()))
		if newtotal > total:	# 条数增加，有更新！
			total = newtotal
			msg = {}
			for item in score.get('rows'):
				subject = item.get('kcmc')
				six = item.get('zcj')
				msg[subject] = six

			send_mail(json.dumps(msg, indent=2, ensure_ascii=False))
	except Exception as e:
		send_mail(str(e))
		exit(1)

def sleeptime(hour, min, sec):
	return hour * 3600 + min * 60 + sec

if __name__ == '__main__':
	interval = sleeptime(1,0,0)		# 查询间隔
	while True:
		sso()
		main()
		time.sleep(interval)
