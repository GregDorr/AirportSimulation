
from Information import *


class PriorityQueue:

    queue = None
    length = None

    # default constructor
    def __init__(self):
        self.queue = []
        self.length = 0

    # add a information object to the queue
    def add(self, other):
        self.queue.append(other)
        self.length += 1

    # pop off an object from the queue
    def pop(self):
        self.length -= 1
        return self.queue.pop(0)

    def get_item_index(self, number):
        return self.queue[number]
