#简单的倒计时
import subprocess,time
lefttime = 60
while lefttime > 0 :
    print(lefttime)
    time.sleep(1)
    lefttime -= 1
subprocess.Popen(['open','../data/test.mp3'])