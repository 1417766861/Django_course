#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/5/18 12:30
import redis,threading,queue,time
pool = redis.ConnectionPool(encoding='utf-8',decode_responses=True)

cache = redis.Redis(connection_pool=pool)
start = time.time()

ids = cache.lrange("account", 0, -1)

for id in ids:
    print(id)
   # time.sleep(0.000000001)

end = time.time()
print('耗时%0.2fs' % (end - start))  # 耗时 0.25s
# task_queue.put(id)






