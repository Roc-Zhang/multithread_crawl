from threading import Thread
from Queue import Queue
import requests
headers={'User-Agent': 'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'}
q=Queue()
base_url="https://www.qiushibaike.com/text/{}"
for i in range(50):
    q.put(base_url.format(i+1))


class Mythread(Thread):
    def __init__(self,name,q):
        super(Mythread,self).__init__()
        self.name=name
        self.url_queue=q

    def run(self):
        while not self.url_queue.empty():
            url=self.url_queue.get()
            response=requests.get(url,headers=headers)
            print("%s getting url:%s content \n" %(self.name,url))


if __name__=="__main__":
    for i in range(1,4):
        mythread=Mythread("thread{}".format(i),q)
        mythread.start()


        
        
        
