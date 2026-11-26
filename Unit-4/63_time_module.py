import time
start = time.time()
print('Current time:',time.ctime(start))
time.sleep(1)
print('Time taken:',round(time.time()-start,2),'seconds')
