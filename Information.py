#!/usr/bin/python


class Information:
    Id = None
    subTime = None
    slotReq = None
    length = None
    actualStartTime = None
    actualEndTime = None

    # constructor that accepts an id, submission time
    # time slot requested and the length
    def __init__(self, Id, subTime, slotReq, length):
        self.Id = Id
        self.subTime = subTime
        self.slotReq = slotReq
        self.length = length

    # method that displays the string version of each object
    def __str__(self):
        tup = "Id: ", self.Id, ", subTime: ", self.subTime, ", Slot: ", self.slotReq, ", Duration: ", self.length
        return ''.join(tup)

    # method to set the actual start time
    def set_time_start(self, start):
        self.actualStartTime = start

    # method to set the actual end time
    def set_time_end(self, end):
        self.actualEndTime = end

    # returns the object
    def get_information(self):
        return self

    # returns the id
    def get_id(self):
        return self.Id

    # returns the submission time
    def get_subTime(self):
        return self.subTime

    # returns slot requested
    def get_slotReq(self):
        return self.slotReq

    # returns the length
    def get_length(self):
        return self.length

    # returns start time
    def get_start_time(self):
        return self.actualStartTime

    # returns end time
    def get_end_time(self):
        return self.actualEndTime