# **gdut-check-results**

## 功能

每隔一小时，自动登录教务管理系统，查询自己成绩是否有更新，如果有更新，则登录 163 邮箱，向 qq 邮箱发送更新后的成绩单。

最好把 qq 邮箱与微信绑定，这样微信就能收到消息了。

## 登录教学管理系统

一开始就在这一步卡死了。
由于正宗的教学管理系统 [http://222.200.98.147/](http://222.200.98.147/) 只允许校园网访问，我的服务器又不是校园网自然访问不了。

于是开始尝试一些奇技淫巧。
微信上有个官方公众号不用校园网也可访问自己成绩，用 fiddler 抓包，分析。这是一条路。
但我并不采用，因为要登录微信，这点有点不爽。

后来，我发现学校留了一条后路给我。[http://jxfw.gdut.edu.cn/login!welcome.action](http://jxfw.gdut.edu.cn/login!welcome.action) ，同一个教学管理系统，但不是校园网也可以登录，估计知道的人很少。

问题又来了，该死的验证码。然而左下角有个「使用统一认证中心登录」，看到了这条链接：[http://jxfw.gdut.edu.cn/new/ssoLogin](http://jxfw.gdut.edu.cn/new/ssoLogin)，sso，single sign on，单点登录，这是个好东西，一处登录，处处登录。用这个中心认证服务器登录不需要验证码！

## SMTP 登录邮箱

我用的是 163 邮箱，其他邮箱应该也差不多。
需要注意的是这里的邮箱密码指的是授权码，是第三个客户端登录的密码，而不是我们邮箱网站登录的那个。

## 判断是否有更新

抓包可知，成绩单接口是 [http://jxfw.gdut.edu.cn/xskccjxx!getDataList.action](http://jxfw.gdut.edu.cn/xskccjxx!getDataList.action)，返回的是 json 数据，有个 total 字段指的是出成绩的科目数，以此判断是否有更新。

若更新，则把成绩单爬下来，发送到 qq 邮箱。

## 使用方法

```python
# login.py

data = {
	'username': 'xxxx',    # 学号
	'password': 'xxxx',    # 默认是身份后六位
	'lt': lt,
	'dllt': 'userNamePasswordLogin',
	'execution': execution,
	'_eventId': 'submit',
	'rmShown': '1',
}
```

```python
# mail.py

def send_mail(score):
	from_addr = 'xxxx@163.com'	# 发送邮件的 163 邮箱
	password = 'xxxx'            # 163 邮箱授权码
	to_addr = 'xxxx@qq.com'		# 接受邮件的 qq 邮箱
```

```python
# main.py

interval = sleeptime(1,0,0)		# 查询间隔，三个参数对应时、分、秒，默认每小时查一次
```

## 效果图




![1528633749880-723579ba-e4a8-465a-b424-8c72bf9fd380.png | left | 250x444](https://cdn.yuque.com/yuque/0/2018/png/104735/1528634187645-b770c2f5-e50c-448b-a180-24e1167cc571.png "")