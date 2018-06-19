from datetime import datetime,timezone,timedelta
import re
#获取当前日期和时间
print(datetime.now())
#获取指定日期和时间
dt=datetime(2017,5,6,12,30)
print(dt)
#datetime转换为timestamp
ts=dt.timestamp()
print(ts)
#timestamp转换为datetime
dt=datetime.fromtimestamp(ts)
print(dt)
#str转换为datetime
dt=datetime.strptime('2018-06-11 20:10:00','%Y-%m-%d %H:%M:%S')
print(dt)
#datetime转换为str
dtstr=dt.strftime('%a, %b %d %H:%M')
print(dtstr)

#练习
def to_timestamp(dt_str, tz_str):
     dt=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
     tz=re.match(r'^UTC([+-]\d{1,2}):(\d{1,2})',tz_str)
     h=int(tz.group(1))
     m=int(tz.group(2))
     tz_utc=timezone(timedelta(hours=h,minutes=m))
     dt=dt.replace(tzinfo=tz_utc)
     return dt.timestamp()

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2
print('ok')


