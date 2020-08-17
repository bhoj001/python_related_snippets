"""
author: Bhoj Bahadur Karki
Date: 2020-August-15th
Description: Observer design pattern

In this pattern, objects are represented as observers that wait for an event to trigger.
An observer attaches to the
subject once the specified event occurs. As the event occurs,
the subject tells the observers that it has occurred.
"""

import threading
import time


class Downloader(threading.Thread):

    def run(self):
        print("downloading...")
        for i in range(1, 5):
            self.i = i
            time.sleep(2)
            print("fun fun")
        return "Hellow world"


class Worker(threading.Thread):
    def run(self):
        # print("worker")
        for i in range(1, 5):
            print("working running ... {}{} \n".format(i, t.i))
            time.sleep(1)
            t.join()

        print("done")


t = Downloader()
t.start()

print("----------sleep---------")
time.sleep(1)

t1 = Worker()
t1.start()

t2 = Worker()
t2.start()

t3 = Worker()
t3.start()
