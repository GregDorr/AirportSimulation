
from Information import Information


class PriorityQueue:

    queue = [Information]
    length = None

    # default constructor
    def __init__(self):
        self.queue = []
        self.length = 0

    # add a information object to the queue
    def add(self, ID, sub_time, req_start, length):
        if self.length == 0:
            self.queue.append(Information(ID, sub_time, req_start, length))
            self.length += 1
        else:
            self.sort_by_sub_time(Information(ID, sub_time, req_start, length))
            self.length += 1

    # pop off an object from the queue
    def pop(self):
        self.length -= 1
        return self.queue.pop(0)

    def peek(self):
        if self.length != 0:
            return self.queue[0]
        else:
            return 0

    # sorts the list by the submission time
    def sort_by_sub_time(self, obj):
        for x in range(0, self.length, 1):
            if obj.subTime < self.queue[x].subTime:
                self.queue.insert(x, obj)
                break
        self.queue.append(obj)

    # sorts based on time
    def increase_time(self, time):
        for x in range(0, self.length, 1):
            if self.queue[x].slotReq < time:
                continue
            elif self.queue[x].slotReq == time:
                self.compare_swap(x, self.queue[x])

    # swaps positions of elements in the queue
    def compare_swap(self, index, obj):
        for x in range(0, self.length, 1):
            if x == 0:
                continue
            elif x == index:
                continue
            elif obj.slotReq < self.queue[x].slotReq:
                temp = self.queue[x]
                self.queue[x] = obj
                self.queue[index] = temp

    def display(self):
        string=[]
        for x in range(0, self.length, 1):
            string.append(str(self.queue[x]))
        return string

    def get_slotReq(self, index):
        return self.queue[index].slotReq
