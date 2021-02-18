import time as t

time_now = t.localtime()

print(str(time_now.tm_year) + '-' + str(time_now.tm_mon) + '-' + str(time_now.tm_mday))

print(t.localtime())

t.sleep(5)

time_now_2 = t.time()
delivery_time = time_now_2 + (86400 * 7)
print(t.localtime(delivery_time))

start_time = t.time()

