#!/usr/bin/python
from time import sleep
from PriorityQueue import PriorityQueue
from Information import Information

Queue = PriorityQueue()


def readFile():
    fo = open("Compilers_Python.txt", "r")

    var = 1

    while var:
        try:
            sleep(1)
            test = fo.next().split(",")
        except StopIteration:
            print("end of file")
            break
        else:
            id = test[0].strip()
            subTime = test[1].strip()
            reqStart = test[2].strip()
            reqDuration = test[3].strip()
            Queue.add(Information(id, subTime, reqStart, reqDuration))
    fo.close()
    return


# displaying the queue at each time
def display_queue(queue):
    time = 0
    while queue.length != 0:
        print(Queue.pop())
        sleep(1)
        time += 1

readFile()

display_queue(Queue)

