#!/usr/bin/python


# This class holds the information coming in from each plane
class Information:

    Id = None               # The plane's id
    subTime = None          # the sub mission time
    slotReq = None          # the slot they request
    length = None           # the length of time they request
    actualStartTime = 0     # the time when they actually started
    actualEndTime = 0       # the time they actually take off

    # constructor that accepts an id, submission time
    # time slot requested and the length
    def __init__(self, Id, subTime, slotReq, length):
        self.Id = Id
        self.subTime = subTime
        self.slotReq = slotReq
        self.length = length

    # method that displays the string version of each object
    def __str__(self):
        tup = str(self.Id), ",", str(self.subTime), ",", str(self.slotReq), ",", str(self.length)
        return ''.join(tup)

