from threading import Thread, Lock
from queue import Queue
import requests
from lxml import etree
import proxy_ip
import json

lock=Lock()
headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'}
q=Queue()
base_url = r"https://www.qiushibaike.com/text/{}"
proxies=proxy_ip.get_ip()
for i in range(50):
    q.put(base_url.format(i+1))


class Mythread(Thread):
    def __init__(self, q,num):
        super(Mythread,self).__init__()
        self.url_queue=q
        self.num=num


    def run(self):
        print("MyThread%d is running" %self.num,end="")
        for i in range(3):     #每隔3秒爬取一次，免的太快让人家觉得不爽！！！
            print(".",end="",flush=True)
            time.sleep(1)
        print("\n",end="")
        while not self.url_queue.empty():
            url = self.url_queue.get()
            response = requests.get(url,headers=headers,proxies=proxies)    
            html=etree.HTML(response.text, etree.HTMLParser())
            content=html.xpath("//div[@class='content']/span/text()")
            lock.acquire()
            with open("./text.txt","a+") as f:
                f.write(json.dumps(content))
                f.write("\n")
            lock.release()
            
            
if __name__ == "__main__":
    for i in range(1,4):
        mythread = Mythread(q,i)
        mythread.start()

    

        
        
        



        
        
        
