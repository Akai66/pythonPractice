#threadLocal
import threading
local_school = threading.local()
def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def run(name):
    local_school.student=name
    process_student()

t1=threading.Thread(target=run,args=('Alice',),name='Thread-A')
t2=threading.Thread(target=run,args=('Bob',),name='Thread-B')

t1.start()
t2.start()
L=[]
L.append(t1)
L.append(t2)
for t in L:
    t.join()


