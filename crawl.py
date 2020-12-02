from threading import Thread
from queue import Queue
import requests
from lxml import etree
import json

headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'}
q=Queue()
base_url = r"https://www.qiushibaike.com/text/{}"
proxies={"https":"https://61.160.210.223:808"}
for i in range(50):
    q.put(base_url.format(i+1))


class Mythread(Thread):
    def __init__(self, q):
        super(Mythread,self).__init__()
        self.url_queue=q


    def run(self):
        while not self.url_queue.empty():
            url = self.url_queue.get()
            response = requests.get(url,headers=headers,proxies=proxies)    
            html=etree.HTML(response.text, etree.HTMLParser())
            content=html.xpath("//div[@class='content']/span/text()")
            print(content)
            



if __name__ == "__main__":
    for i in range(1,4):
        mythread = Mythread(q)
        mythread.start()

    

        
        
        



        
        
        
