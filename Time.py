class Time:
    hour = 0
    minute = 0
    day = 0

    def __init__(self, hour=0, minute=0, day=0):
        self.hour = hour
        self.minute = minute
        self.day = day

    @classmethod
    def FromSecond(cls, secs=0):
        mins = secs // 60
        hours = mins // 60
        mins -= hours * 60
        days = hours // 24
        hours -= days * 24
        return cls(hours, mins, days)

    @classmethod
    def FromString(cls, s):
        values = s.split(":")
        t = Time()
        if len(values) > 0:
            t.hour = int(values[0])
        if len(values) > 1:
            t.minute = int(values[1])
        if len(values) > 2:
            t.day = int(values[2])

        return t

    def __int__(self):
        return ((self.day * 24 + self.hour) * 60 + self.minute) * 60

    def __add__(self, other):
        secs = int(self) + int(other)
        return self.FromSecond(secs)

    def __sub__(self, other):
        secs = int(self) - int(other)
        return self.FromSecond(secs)

    def __eq__(self, other):
        return int(self) == int(other)

    def __gt__(self, other):
        return int(self) > int(other)

    def __lt__(self, other):
        return int(self) < int(other)

    def __ge__(self, other):
        return self > other or self == other

    def __le__(self, other):
        return self < other or self == other

    def __repr__(self):
        return str(self.day) + ":" + str(self.hour) + ":" + str(self.minute)

    def getHourNMin(self):
        return Time(self.hour, self.minute)

    def setHourNMin(self, t):
        self.hour = t.hour
        self.minute = t.minute
