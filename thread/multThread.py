#多线程,加锁
import threading
balance=0
lock=threading.Lock()
def change_it(n):
    global balance
    balance = balance+n
    balance = balance-n

def run(n):
    for x in range(1000000):
        try:
            lock.acquire()
            change_it(n)
        finally:
            lock.release()

t1=threading.Thread(target=run,args=(5,))
t2=threading.Thread(target=run,args=(8,))

t1.start()
t2.start()
L=[]
L.append(t1)
L.append(t2)
for t in L:
    t.join()

print(balance)

#因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核
#不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响