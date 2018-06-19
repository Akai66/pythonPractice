import requests
r = requests.get('https://www.douban.com/')
print(r.status_code)
# print(r.text)
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)
print(r.status_code)
print(r.encoding)
# print(r.text)
# print(r.content)
r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())
r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})

#post请求
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
#requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数
url='http://www.baidu.com'
params = {'key': 'value'}
r = requests.post(url, json=params) # 内部自动序列化为JSON
upload_files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=upload_files)
#获取响应头
r.headers
#获取cookies
r.cookies['ts']
#要在请求中传入Cookie，只需准备一个dict传入cookies参数
cs = {'token': '12345', 'status': 'working'}
r = requests.get(url, cookies=cs)
#要指定超时，传入以秒为单位的timeout参数
r = requests.get(url, timeout=2.5)# 2.5秒后超时