#简单的http请求
import json
import requests
import myModules
url = 'http://app.video.baidu.com/xda?terminal=pc&position=dasoupinzhuanPCSearchup&id=dasoupinzhuanPCSearchup&site=http%3A%2F%2Fvideo.baidu.com%3A8080%2Fv%3Fword%3D%25E5%25AE%259D%25E9%25A9%25AC%26ct%3D301989888%26rn%3D27%26pn%3D0%26db%3D0%26s%3D0%26fbl%3D800%26ie%3Dutf-8&refer=&keywords=%E5%AE%9D%E9%A9%AC'
res = requests.get(url)
print(json.loads(res.text))
print(myModules.getOddSum())

