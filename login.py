import requests
from bs4 import BeautifulSoup

headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWeb'
		'Kit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
}

ss = requests.Session()

def sso():
	url = 'http://authserver.gdut.edu.cn/authserver/login'
	payload = {'service': 'http://jxfw.gdut.edu.cn/new/ssoLogin'}

	rsp = ss.get(url, params=payload, headers=headers)
	
	soup = BeautifulSoup(rsp.text, 'html.parser')
	try:
		lt = soup.form.find_all('input')[2].get('value')
	except Exception:
		return
	execution = soup.form.find_all('input')[4].get('value')

	data = {
		'username': 'xxxx',
		'password': 'xxxx',
		'lt': lt,
		'dllt': 'userNamePasswordLogin',
		'execution': execution,
		'_eventId': 'submit',
		'rmShown': '1',
	}
	ss.post(url, params=payload, headers=headers, data=data)

if __name__ == '__main__':
	sso()
