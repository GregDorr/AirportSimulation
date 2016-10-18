#!/usr/bin/python

class Information:

    Id = None
    subTime = None
    timeSlotRequested = None
    length = None
    ActualStartTime = None
    ActualEndTime = None

    def __init__(self, Id, subTime, timeSlotRequested, length):
        self.Id = Id
        self.subTime = subTime
        self.timeSlotRequested = timeSlotRequested
        self.length = length

    def __str__(self):
        tup = "Id: ", self.Id, ", subTime: ", self.subTime, ", Slot: ", self.timeSlotRequested, ", Duration: ", self.length
        return ''.join(tup)
