# from threading import *
# from time import *
# class mythread:
#     def maketea(self):
#         self.task1()
#         self.task2()
#         self.task3()
#     def task1(self):
#         print("add sugar and powder")
#         sleep(2)
#         print("done")
#     def task2(self):
#         print("add milk")
#         sleep(3)
#         print("done")
#     def task3(self):
#         print("filter it")
#         print("done")
# o1 = mythread()
# t1 = Thread(target=o1.maketea())
# t1.start()

# from threading import *
# from time import *
# class th(Thread):
#     def __init__(self, str):
#         self.str = str
#     def movie(self):
#         for i in range(1,6):
#             print(self.str,":",i)
#             #sleep(0.1)
# o1 = th("ticket1")
# o2 = th("ticket2")
# t1 = Thread (target=o1.movie)
# t2 = Thread (target=o2.movie)
# t1.start()
# t2.start()

from threading import Thread
from time import *
class mythread(Thread):
    def run(self):
        for i in range(1,5):
            print(i)
            sleep(0.1)
o1 = mythread()
o2 = mythread()
t1 = Thread(target=o1.run)
t2 = Thread(target=o2.run)
t1.start()
t1.join(1)
t2.start()