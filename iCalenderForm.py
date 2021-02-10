from Event import Event
from datetime import datetime, timedelta


def iCalenderEvent(event: Event, dayStart: datetime):
    eventStart = dayStart + timedelta(days=event.start.day, hours=event.start.hour, minutes=event.start.minute)
    endTime = dayStart + timedelta(days=event.end.day, hours=event.end.hour, minutes=event.end.minute)
    eventStart = eventStart.strftime("%Y%m%dT%H%M%S")
    endTime = endTime.strftime("%Y%m%dT%H%M%S")
    ics = f"""BEGIN:VEVENT
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
END:VEVENT"""
    return ics


def iCalenderCalender(name, desc):
    return f"""BEGIN:VCALENDAR
PRODID:-//Google Inc//Google Calendar 70.9054//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:{name}
X-WR-TIMEZONE:Asia/Dhaka
X-WR-CALDESC:{desc}
BEGIN:VTIMEZONE
TZID:Asia/Dhaka
X-LIC-LOCATION:Asia/Dhaka
BEGIN:STANDARD
TZOFFSETFROM:+0600
TZOFFSETTO:+0600
TZNAME:+06
DTSTART:19700101T000000
END:STANDARD
END:VTIMEZONE"""
