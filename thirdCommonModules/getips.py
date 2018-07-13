import requests,json
ret=requests.get('http://server.zeus.xiaodutv.cn:8900/zeusapi/v1/node/?id=143')
datas=json.loads(ret.text)
iplist=''
ad_odp_bj=0
ad_odp_gz=0
odp_ex_bj=0
odp_ex_gz=0
for data in datas['data']['machines']:
    if data['hostname'].find('ad-odp') != -1:
        if data['hostname'].find('bj') != -1:
            ad_odp_bj+=1
        elif data['hostname'].find('gz') != -1:
            ad_odp_gz+=1
    elif data['hostname'].find('odp-ex') != -1:
        print(data['ip'])
        # if data['hostname'].find('bj') != -1:
        #     odp_ex_bj+=1
        # elif data['hostname'].find('gz') != -1:
        #     odp_ex_gz+=1

# print('ad_odp_bj:%s,ad_odp_gz:%s,odp_ex_bj:%s,odp_ex_gz:%s' % (ad_odp_bj,ad_odp_gz,odp_ex_bj,odp_ex_gz))