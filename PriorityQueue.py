
from Information import Information


class PriorityQueue:

    # variables
    queue = [Information]       # main list
    tempQueue = [Information]   # secondary temporary list
    length = None               # length of the main list
    tempQueueLength = 0         # length of the secondary list

    # default constructor
    def __init__(self):
        self.queue = []
        self.tempQueue = []
        self.length = 0
        self.tempQueueLength = 0

    # add a information object to the queue
    def add(self, ID, sub_time, req_start, length):
        if self.length == 0:
            self.queue.append(Information(ID, sub_time, req_start, length))
            self.length += 1

    # if the submission time is less then the first element
        elif self.queue[0].subTime < sub_time:

            # if the temp array is empty
            if self.tempQueueLength == 0:
                self.tempQueue.append(Information(ID, sub_time, req_start, length))
                self.tempQueueLength += 1

            # if it's not empty
            else:
                self.sort_by_sub_time(self.tempQueue, self.tempQueueLength,Information(ID, sub_time, req_start, length))
                self.tempQueueLength += 1
        # if the submission time is the same as the first object
        else:
            self.sort_by_sub_time(self.queue, self.length, Information(ID, sub_time, req_start, length))
            self.length += 1

    # pop off an object from the queue
    def pop(self):
        self.length -= 1
        return self.queue.pop(0)

    # to check on the first element
    def peek(self):
        if self.length != 0:
            return self.queue[0]
        else:
            return 0

    # sorts the list by the submission time
    # it then returns the array you sort
    def sort_by_sub_time(self, array, size, obj):
        for x in range(0, size, 1):
            if obj.subTime < array[x].subTime:
                array.insert(x, obj)
                break
        array.append(obj)
        return array

    # sorts based on time
    # when an elements submission time is equal to the time
    # they queue will look at when it's requesting to take off
    # and accommodate accordingly
    def increase_time(self, time):
        for x in range(0, self.length, 1):
            for y in range(0, self.tempQueueLength, 1):

                # if the submission time is equal to the current time
                if self.tempQueue[y].subTime == time:
                    # comparing the requested times
                    if self.queue[x].slotReq > self.tempQueue[y].slotReq:
                        # swapping elements where needed
                        self.queue.insert(x, self.tempQueue[y])
                        self.tempQueue.remove(self.tempQueue[y])
                        self.tempQueueLength -= 1
                        self.length += 1