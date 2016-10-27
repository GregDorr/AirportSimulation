#!/usr/bin/python
from time import sleep
from PriorityQueue import PriorityQueue
from Information import Information


# reads the file input from the user and adds it to the priority queue
def read_file():
    TotalTime = 10
    with open("Compilers_Python.txt", "r") as fo:
        for line in fo:
            # splitting the string into pieces
            string = line.split(',')
            # setting the information values
            ID = string[0].strip()
            sub_time = int(string[1].strip())
            req_start = (string[2].strip())
            length = int(string[3].strip())

            TotalTime += length

            # creating a new information object and pushing to queue
            Queue.add(ID, sub_time, req_start, length)

    fo.close()
    return TotalTime


# displaying the queue at each time
def time():
    time = 0
    Queue.queue[0].actualStartTime = time

    while time < TotalTime:
        print("At time " + str(time) + "the queue would look like: " )
        # if the current plane has taken off
        Queue.increase_time(time)
        if takenOff(time) == 1:
            sleep(1)
            time += 1
            if Queue.length != 0:
                Queue.queue[0].actualStartTime = time
                print("\tplane took off")
            else:
                print("\tplane took off")
                break
        else:
            # wait 1 second then increase time
            sleep(1)
            time += 1
    return


def takenOff(time):
    temp = Queue.peek()
    if (temp.length == time) or (temp.actualStartTime+temp.length) == time:
        temp.actualEndTime = time
        result = Queue.pop()
        string = str(result.Id) + "(" + str(result.actualStartTime) + "-" + str(result.actualEndTime) + ")"
        string2 = ''.join(string)
        results.append(string2)
        return 1
    return 0


# MAIN
Queue = PriorityQueue()
displayQueue = []
up = None
results =[]
TotalTime = read_file()
print(str(TotalTime))
print(Queue.display())
time()
print(results)

