from Event import Event
from datetime import datetime, timedelta


def iCalenderEvent(event: Event, dayStart: datetime):
    eventStart = dayStart + timedelta(days=event.start.day, hours=event.start.hour, minutes=event.start.minute)
    endTime = dayStart + timedelta(days=event.end.day, hours=event.end.hour, minutes=event.end.minute)
    eventStart = eventStart.strftime("%Y%m%dT%H%M%S")
    endTime = endTime.strftime("%Y%m%dT%H%M%S")
    ics = f"""
    BEGIN:VEVENT
    DTSTART;TZID=Asia/Dhaka:{eventStart}
    DTEND;TZID=Asia/Dhaka:{endTime}
    UID:{event.name}a{event.start.day}b{event.start.hour}c{event.start.minute}@google.com
    SEQUENCE:1
    STATUS:CONFIRMED
    SUMMARY:{event.name}
    TRANSP:OPAQUE
    BEGIN:VALARM
    ACTION:DISPLAY
    TRIGGER:-P0DT0H5M0S
    END:VALARM
    END:VEVENT
    """
    return ics
