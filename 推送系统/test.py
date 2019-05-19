import redis,threading,queue
pool = redis.ConnectionPool(encoding='utf-8',decode_responses=True)
cache = redis.Redis(connection_pool=pool)
import time
start = time.time()

# ids = cache.lrange('account',0,-1)
end = time.time()
task_queue = queue.Queue(1000)

def worker(thread_name):
    '''执行任务'''
    print( thread_name, 'started')
    while True:
        task = task_queue.get()
        print( task, '推送完成')
        break


def Produce(thread_name):
    print( thread_name, 'started')
    while True:
        id = cache.lrange("account",0,-1)
        print(id, '推送完成')
        # task_queue.put(id)
        break

def main():
    '''执行任务'''
    tsk = []

    for x in range(5):
         t = threading.Thread(target=Produce,args=('Produce %s'%x,))
         t.start()
         tsk.append(t)


    for y in range(5):
        t =  threading.Thread(target=worker,args=('woker %s'%y,))
        t.start()
        tsk.append(t)

    for t in tsk:
          t.join()




if __name__ == '__main__':
     main()
     print('耗时%0.2fs' % (end - start))  # 耗时 0.25s
