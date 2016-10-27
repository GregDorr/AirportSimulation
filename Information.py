#!/usr/bin/python

class Information:
    Id = None
    subTime = None
    slotReq = None
    length = None
    actualStartTime = 0
    actualEndTime = 0

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

    # display the start and end time with the id
    def display_results(self):
        output = self.Id + " (" + str(self.actualStartTime) + "-", str(self.actualEndTime) + ")"
        return ''.join(output)

