from Time import Time


class Event:
    name = ""
    start: Time
    end: Time
    duration: Time
    collidedEvents: [Time]

    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end
        self.duration = end - start
        self.collidedEvents = []

    def delegateForward(self, newStartTime):
        if newStartTime < self.start.getHourNMin():
            self.start.day += 1
        self.start.setHourNMin(newStartTime)
        self.end = self.start + self.duration

    def extendDuration(self, extension):
        self.duration += extension
        self.end += extension

    def __repr__(self):
        return self.name + "{" + str(self.start) + "," + str(self.end) + "}"
