#多线程的应用
import threading,os,bs4,requests,sys
os.makedirs('xkcd',exist_ok=True)
def dowoloadXkcd(start,end):
    for num in range(start,end):
        url = 'http://xkcd.com/%s/' % num
        print('Downloading page ' + url)
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text,'html.parser')
        imgs = soup.select('#comic img')
        if len(imgs) > 0:
            imgurl = 'http:' + imgs[0].get('src')
            res = requests.get(imgurl)
            res.raise_for_status()
            imgFile = open(os.path.join('./xkcd',os.path.basename(imgurl)),'wb')
            for chunk in res.iter_content(100000):
                imgFile.write(chunk)
            imgFile.close()
#多线程下载
print('start of task')
downloadThreads = []
for i in range(1,30,10):
    downloadThread = threading.Thread(target=dowoloadXkcd,args=[i,i+10])
    downloadThreads.append(downloadThread)
    downloadThread.start()

for theadItem in downloadThreads:
    theadItem.join()

print('end of task')


