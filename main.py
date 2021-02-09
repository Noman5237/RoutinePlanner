from random import shuffle, choice

from Time import Time
from Event import Event

sleepHours = [
    Event("Sleep", Time(22, 0), Time(0, 0)),
    Event("Sleep", Time(0, 0), Time(5, 0)),
]

prayerHours = [
    Event("Fazr", Time(5, 30), Time(5, 45)),
    Event("Zuhr", Time(13, 30), Time(14, 0)),
    Event("Asr", Time(16, 0), Time(16, 15)),
    Event("Maghrib", Time(18, 0), Time(18, 15)),
    Event("Isha", Time(21, 15), Time(22, 0)),
]


def collide(ev, events):
    for e in events:
        conditions = [
            ev.start.getHourNMin() <= e.start < (ev.start.getHourNMin() + ev.duration),
            e not in ev.collidedEvents
        ]
        if all(conditions):
            return e
    else:
        return False


subjectsByName = {
    "Physics": ["1"] * 3,
    "Calculus": ["1"] * 3,
    "Statistics": ["1"] * 3,
    "Android Development": ["2"] * 2,
    "Java": ["2"] * 2,
    "Microservices": ["1"] * 3,
    "Game Design": ["3"] * 6,
    "CP": ["6"] * 7,
    "Arabic": ["1"] * 4,
    "Academics": ["2"] * 7,
    "Others": ["1"] * 7
}

subjectsByHours = {}
totalEvents = 0


def prepareEvents():
    global totalEvents
    for subject, hours in subjectsByName.items():
        for hour in hours:
            if hour not in subjectsByHours:
                subjectsByHours[hour] = []
            subjectsByHours[hour].append(subject)
            totalEvents += 1

    for hours in subjectsByHours.values():
        shuffle(hours)


lastRandomSubjects = []


def getRandomSubject(hour=-1):
    modifiedSubjects = [item for item in subjectsByHours.items() if len(item[1]) > 0]
    hour = int(hour)
    if hour > -1:
        modifiedSubjects = [item for item in modifiedSubjects if int(item[0]) * 3600 <= hour]

    if len(modifiedSubjects) > 0:
        hour, subjects = choice(modifiedSubjects)
        return tuple((subjects.pop(), hour))
    else:
        return None


weeklySchedule = []

if __name__ == '__main__':
    i = 0
    event = None
    lastEvent = Event("", Time(), Time())
    randomSubjectNHour = None
    free = True
    prepareEvents()
    print(subjectsByHours)
    while i < totalEvents:
        if free:
            randomSubjectNHour = getRandomSubject()
            event = Event(randomSubjectNHour[0], lastEvent.end,
                          lastEvent.end + Time.FromString(randomSubjectNHour[1]))
        sleepEvent = collide(event, sleepHours)
        if sleepEvent is not False:
            timeConstraintAlternative = getRandomSubject(sleepEvent.start - event.start.getHourNMin())
            if timeConstraintAlternative is None:
                event.delegateForward(sleepEvent.end)
            else:
                event = Event(timeConstraintAlternative[0], lastEvent.end,
                              lastEvent.end + Time.FromString(timeConstraintAlternative[1]))
                subjectsByHours[randomSubjectNHour[1]].append(randomSubjectNHour[0])
            free = False
            continue
        prayerEvent = collide(event, prayerHours)
        if prayerEvent is not False and prayerEvent:
            event.collidedEvents.append(prayerEvent)
            event.extendDuration(prayerEvent.duration)
            free = False
            continue

        weeklySchedule.append(event)
        lastEvent = event
        i += 1
        free = True

    for event in weeklySchedule:
        print(event)
