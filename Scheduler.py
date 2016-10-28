#!/usr/bin/python
from time import sleep
from PriorityQueue import PriorityQueue


class Scheduler:

    # variables
    Queue = None    # holds priority queue
    results = []    # list to the results
    TotalTime = 0   # total time it takes for all the planes to take off

    # default constructor
    def __init__(self):
        self.Queue = PriorityQueue()
        self.results = []
        self.TotalTime = self.read_file()

    # reads the file input from the user and adds it to the priority queue
    # this method returns the total time
    def read_file(self):
        self.TotalTime = 10
        with open("Compilers_Python.txt", "r") as fo:
            for line in fo:
                # splitting the string into pieces
                string = line.split(',')
                # setting the information values
                ID = string[0].strip()
                sub_time = int(string[1].strip())
                req_start = (string[2].strip())
                length = int(string[3].strip())

                # adds to the total time
                self.TotalTime += length

                # creating a new information object and pushing to queue
                self.Queue.add(ID, sub_time, req_start, length)
        return self.TotalTime

    # takes in the current time
    # returns the queue at different times
    def displayQueue(self, time):
        # string to output
        displayString = ("At time " + str(time) + " the queue would look like: ")

        for x in range(0, self.Queue.length, 1):
            # if theres only one element in the queue
            if x == 0:
                displayString += (str(self.Queue.queue[x].Id) + "(Started at " + str(self.Queue.queue[x].actualStartTime) + ")")
            else:
                startTime = self.Queue.queue[x - 1].length + self.Queue.queue[x - 1].actualStartTime + 1
                self.Queue.queue[x].actualStartTime = startTime
                displayString += (", " + str(self.Queue.queue[x].Id) + "(Scheduled for " + str(startTime) + ")")

        return ''.join(displayString)

    # displaying the queue at each time
    def start(self):
        time = 0
        self.Queue.queue[0].actualStartTime = time

        while time < self.TotalTime:
            # updates the queue
            self.Queue.increase_time(time)

            # for displaying a string
            displayString = self.displayQueue(time)

            # for displaying the queue and the
            print(displayString)
            del displayString

            # if the current plane has taken off
            if self.takenOff(time) == 1:
                sleep(1)
                time += 1
                if self.Queue.length != 0:
                    self.Queue.queue[0].actualStartTime = time
                    print("\tplane took off")
                else:
                    print("\tplane took off")
                    break

            else:
                # wait 1 second then increase time
                sleep(1)
                time += 1
        # print out the results before ending
        print(''.join(self.results))

        return

    # checks if the plane thats up, has taken off or not
    # if it has it pops the queue
    def takenOff(self, time):
        temp = self.Queue.peek()
        if temp.actualStartTime + temp.length == time:
            temp.actualEndTime = time
            result = self.Queue.pop()
            string = str(result.Id) + "(" + str(result.actualStartTime) + "-" + str(result.actualEndTime) + "), "
            string2 = ''.join(string)
            self.results.append(string2)
            return 1
        return 0

