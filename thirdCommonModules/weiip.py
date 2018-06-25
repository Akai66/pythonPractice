import requests
from random import randint
import time
params={'id':'955'}
headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}
times=0
for i in range(500):
    headers['X-Forwarded-For'] = '%s.%s.%s.%s' % (str(randint(1,255)),str(randint(1,255)),str(randint(1,255)),str(randint(1,255)))
    r = requests.get('http://kpindao99.com/t.php',params=params,headers=headers)
    print('clientip:%s is complete' % headers['X-Forwarded-For'])
    times=times+1
    time.sleep(10)
print('complete %s times' % times)

