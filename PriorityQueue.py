
from Information import *


class PriorityQueue:

    Queue = None

    def __init__(self):
        self.Queue = []

    def push(self, other):
        self.Queue.append(other)

    def pop(self):
        return self.Queue.pop(0)

