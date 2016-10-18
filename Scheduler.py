#!/usr/bin/python
from PriorityQueue import PriorityQueue
from Information import Information

Queue = PriorityQueue()


def readFile():
    fo = open("Compilers_Python.txt", "r")

    var = 1

    while var:
        try:
            test = fo.next().split(",")
        except StopIteration:
            var = 0
            print("end of file")
            break
        else:
            id = test[0].strip()
            subTime = test[1].strip()
            reqStart = test[2].strip()
            reqDuration = test[3].strip()
            print(id)
            print(subTime)
            print(reqStart)
            print(reqDuration)
            Queue.push(Information(id, subTime, reqStart, reqDuration))

    fo.close()
    return


readFile()
print(Queue.pop())
print(Queue.pop())
print(Queue.pop())
