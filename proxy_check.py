from proxy_checker import ProxyChecker
from time import sleep
import threading

with open('proxy.txt') as file:
    proxyList = file.read().split('\n')

check_count = 0
thread_count = 0
def check(count):
    global thread_count
    thread_count +=1
    if count == 0:
        pass
    else:
        count+=1
    check = count
    checker = ProxyChecker()
    print(checker.check_proxy(proxyList[check]))
    if checker.check_proxy(proxyList[check]) == 'False':
        pass
    else:
        with open('live.txt','a') as file:
            file.write(proxyList[check] + '\n')
    thread_count -=1

while True:
    if thread_count ==0:
        for i in range(10):
            threading.Thread(target=check,args=(check_count,)).start()
            sleep(1)
