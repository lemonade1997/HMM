import pandas as pd
import csv
from multiprocessing import Pool
import time
import urllib.request
import chardet


    
def getdata(url):
    tb = pd.read_html(url)[0] #经观察发现所需表格是网页中第1个表格，故为[0]
    tb.to_csv(r'E:\xhyxx\work2\AQI.csv', mode='a', encoding='utf-8', header=0, index=0)
    time.sleep(0.5)
    #print('第'+str(i)+'页抓取完成')
 
#引入进程池 
def myprocesspool(num=1):
    pool = Pool(num)
    results = pool.map(getdata,urls)
    pool.close()
    pool.join()
    return results
 
if __name__=='__main__':
    urls=[]
    url = "http://www.tianqihoubao.com/aqi/anqing-202001.html"

    data = urllib.request.urlopen(url).read()
    print(chardet.detect(data))
    
    for i in range(12,13):  # 爬取数据
        tmp = 'http://www.tianqihoubao.com/aqi/anqing-2019%s.html' % (str(i))
        urls.append(tmp)
       
    myprocesspool(1)
    