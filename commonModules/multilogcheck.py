#利用多线程,遍历线上机器日志
import paramiko
import threading
import Queue
import sys

username = 'video'
passwd   = 'video@2017'

class MyTask(object):
    
    def __init__(self, name, info):
        self.name = name
        self.info = info

    def dump(self):
        print(self.name, self.info)

class Worker(threading.Thread):
    def __init__(self, queue, res):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.queue = queue

    def run(self):
        while not self.thread_stop:
            #print("thread%d %s: waiting for tast" %(self.ident,self.name)) 
            try:
                q = self.queue
                task = q.get(block=True, timeout=2)
            except Queue.Empty:
                #print("Nothing to do!i will go home!")  
                self.thread_stop=True  
                break 
            
            self.do_job(task, res)
        print("Exiting: thread %d" % (self.ident))
    
    def do_job(self, task, res):

        cmd_map = {
            "ral": "cd /home/video/odp/log/ral/ && tail -n 2 ral-worker.log.wf",
            "hhvm": "cd /home/video/odp/log/hhvm/ && tail -n 2 hhvm-error.log",
            #"access": "cd /home/video/odp/log/ && cat access_log | grep test26=smh",
            #"access": "cd /home/video/odp/log/webserver/ && cat access_log | grep liukai=test",
            #"idc": "cat /home/video/odp/hhvm/conf/hhvm.hdf  | grep current_idc ",
            #"test": "cat /home/video/odp/log/ad/ad.log.2018030719 | grep 'ad/bidding' | grep '19:01' |  awk -F'cost' '{print $2}' | awk -F'[][]' 'BEGIN{a=0;b=0}{a++;if($2>290){b++;}} END{print a,b,b/(a+1)}'",
        }

        result_detail = {

            task.info : {}
        
        }

        for k,cmd in cmd_map.items():

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(task.info.strip(),22,username,passwd)
            stdin, stdout, stderr = ssh.exec_command(cmd)
            
            #print stdout.readlines()[0].strip(), ip.strip()
            stdout_info = stdout.readlines()

            print("Debug:", stdout_info)

            detail = stdout_info[0].strip() if len(stdout_info)>0 else ""

            result_detail[task.info][k] = {
                
                    'detail':detail
                    #'detail':stdout_info
            }

        res.put(result_detail)
        


if __name__ == "__main__":

    q = Queue.Queue()    
    
    res = Queue.Queue()
    ip_list = [
    ]

    file_name = sys.argv[1] if len(sys.argv)>1 else 'bj.check'

    #with open('123.check', 'r') as f:
    with open('bj.check', 'r') as f:
        ips = f.readlines()

    for ip in ips:
        ip_list.append(ip.strip())


    for ip in ip_list:
        name = "name:%s" % (ip,)
        task = MyTask(name, ip)
        task.dump()
        q.put(task)

    
    works = []
    for i in range(10):
        worker = Worker(q, res)
        worker.start()
        works.append(worker)
    
    for i in range(len(works)):
        works[i].join()

    print("all works done")
    

    res_list = []
    while not res.empty():
        
        name = res.get()
        res_list.append(name)

    print(len(res_list))

    for i in range(len(res_list)):

        for k, v in res_list[i].items():
            
            print(k)

            for cmd, detail in v.items():
                
                print ("\t\t",cmd)
                print ("\t\t",detail)
        



