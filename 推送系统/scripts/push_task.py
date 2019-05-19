#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/5/18 9:55
# coding: utf8
'''推送任务脚本'''

import queue
import threading
import time
task_queue = queue.Queue(100)


def worker():
    '''执行任务'''
    thread_name = threading.currentThread().getName()
    print( thread_name, 'started')
    while True:
        task = task_queue.get()
        task.start()
        print( task, '推送完成')


def main():
    '''提交任务到队列'''
    while True:
        task = AccountAccount.objects.filter(subscribed='1').first()
        if not task:
            time.sleep(10)
            django.db.close_old_connections()
            continue
        task.subscribed = '0'
        task.save()
        task_queue.put(task)


def run():
    '''执行任务'''
    for _ in range(20):
        thread = threading.Thread(target=worker)
        #thread.setDaemon(True)
        thread.start()

    while True:
        main()
