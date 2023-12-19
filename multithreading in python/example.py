# Example of multithreading in python
"""
Program to find a square and cube of number using threading
"""


import threading


def find_square(num):
    print("Square {}".format(num * num))


def find_cube(num):
    print("Cube {}".format(num * num * num))


if __name__ == "__main__":
    num = int(input("enter a number:"))
    s1 = threading.Thread(target=find_square, args=(num,))
    s2 = threading.Thread(target=find_cube, args=(num,))

    s1.start()
    s1.join()

    s2.start()
    s2.join()

    print("Done!!")



"""
-------------Output--------------
enter a number:10
Square 100
Cube 1000
Done!!

"""