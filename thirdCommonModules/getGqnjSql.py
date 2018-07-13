# import requests,json
# ret=requests.get('http://erp.xiaodutv.com/newhome/index.php?/hr/getleave')
# datas=json.loads(ret.text)
# sql = 'insert into holiday_record(`user_id`,`run_id`,`type`,`start`,`end`,`len`,`time`,`startTime`,`endTime`) values '
# arr=[]
# sparr = ['杨燕琳','闫学松','石蕴','王悦','高一铭','鲁伟','吴晓','李皓亮','王超','李海峰','李烨民','韩伟扬','郝静','姜婷','魏博','段黄军','张昕怡']
# for data in datas:
#     if data['name'] not in sparr:
#         arr.append("(%s,0,'daixinnianjia','2018-07-10 上午','过期未休年假',%s,'2018-07-10 17:00:00','2018-07-10 09:00:00','2018-07-10 17:00:00')" % (data['uid'],data['sy']))
#
# print(arr)
arr=[]
sql = 'insert into holiday_record(`user_id`,`run_id`,`type`,`start`,`end`,`len`,`time`,`startTime`,`endTime`) values '
sparr = ['杨燕琳','闫学松','石蕴','王悦','高一铭','鲁伟','吴晓','李皓亮','王超','李海峰','李烨民','韩伟扬','郝静','姜婷','魏博','段黄军','张昕怡']
with open('../data/test1.txt','r') as f:
    while True:
        line = f.readline()
        line=line.split()
        if line and line[1] not in sparr:
            arr.append("(%s,0,'daixinnianjia','2018-07-10 上午','过期未休年假',%s,'2018-07-10 17:00:00','2018-07-10 09:00:00','2018-07-10 17:00:00')" % (line[0],line[2]))
        if not line:
            break

print(sql + ','.join(arr) + ';')