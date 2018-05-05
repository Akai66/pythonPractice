import os,requests,bs4,logging
#logging.disable(logging.CRITICAL)
logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
try:
    os.makedirs('xkcd',exist_ok=True)
    url = 'http://xkcd.com/10/'
    while not url.endswith('#'):
        #下载页面
        logging.debug('start to download page:%s' % url)
        res = requests.get(url)
        res.raise_for_status()
        #下载图片
        soup = bs4.BeautifulSoup(res.text,'html.parser')
        imgs = soup.select('#comic img')
        if len(imgs) > 0:
            #开始下载图片
            imgurl = 'http:' + imgs[0].get('src')
            logging.debug('start to download image:%s' % imgurl)
            res = requests.get(imgurl)
            res.raise_for_status()
            imgFile = open(os.path.join('./xkcd',os.path.basename(imgurl)),'wb')
            for chunk in res.iter_content(100000):
                imgFile.write(chunk)
            imgFile.close()
            logging.debug('finish to download image:%s' % imgurl)
        else:
            logging.debug('this page no image:%s' % url)
        logging.debug('finish to download page:%s' % url)
        #获取前一个页面的url
        prevs = soup.select('a[rel="prev"]')
        url = 'http://xkcd.com' + prevs[0].get('href')
    logging.debug('down')
except Exception as exc:
    logging.error('there is a problem:%s' % str(exc))