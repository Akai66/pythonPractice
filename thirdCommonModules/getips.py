import requests,json
ret=requests.get('http://server.zeus.xiaodutv.cn:8900/zeusapi/v1/node/?id=143')
datas=json.loads(ret.text)
iplist=''
for data in datas['data']['machines']:
    print(data['ip'])