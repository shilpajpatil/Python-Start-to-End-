

# Multithreading in python

"""
Thread : thread is an entity within a process that can be sheduled for exicution.
"""

import threading     #import module
import time          # time for checking each thread time

def new_fun():
    print(threading.active_count())  # count currenlt active or running threads
    print()
    print(threading.enumerate())     #returns all the thread objects currently alive
    print()
    print(threading.current_thread())   # to check current thread
    print("hello from main thread")


def func():
    time.sleep(2)
    print("Hello from fun /n", threading.current_thread().getName())  # it will print thread name


def sleeping_fun():
    time.sleep(2)
    print("Hello from sleeping_fun ")


new_fun()

if __name__ == "__main__":

    x = threading.Thread(target=new_fun)    # here we create a object of thread class. it  takes target as a argument.target is a function to be exicuted by the thread where as args is argument to pass that function

    y = threading.Thread(target=func)

    z = threading.Thread(target=sleeping_fun(), name='brand_new_thread')

    x.start()   # to start thread class
    x.join()    # when the thread starts current program keeps on exicuting In current program it waits to complete x then it run y

    y.start()
    y.join()

    z.start()
    z.join()

