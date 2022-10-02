# Oliver Rayner
# October 2022

# HackMIT 2022 Calendar thingy

from ics import Calendar, Event
from datetime import datetime
import sys

def sort_events(calendar) :
    ''' First we need to sort the events by day. '''

    sorted = {}
    events = calendar.events
    for event in events :
        begin = event.begin
        end = event.end
        duration = event.duration.seconds   # Duration in seconds
        weekday = begin.datetime.weekday()

        date = (event.begin.date().month, event.begin.date().day, event.begin.date().year)
        if date in sorted :
            sorted[date]['events'].append((event, duration))
        else :
            sorted[date] = { 
                'events' : [(event, duration)], 
                'weekday': weekday,
                }
    return sorted

def free_time(sorted_events, minutes_interval = 15) :
    ''' Find the times in a day which are not occupied by an event. '''

    for day, schedule in sorted_events.items() :

        open_time = [ t for t in range(0, 60*24, minutes_interval) ]  # Splits day up into list

        events = schedule['events']
        for event in events :

            duration = event[1]
            hour_begin, minute_begin = event[0].begin.datetime.time().hour, event[0].begin.datetime.time().minute
            hour_end, minute_end = event[0].end.datetime.time().hour, event[0].end.datetime.time().minute

            open_time = open_time[:int(hour_begin * (60/minutes_interval))] + [ 'X' for _ in range(int(duration/60/minutes_interval)) ] + open_time[int(hour_end * (60/minutes_interval)):]

        sorted_events[day]['open_time'] = open_time
    
    return sorted_events


def main() :

    file_name = sys.argv[1] if len(sys.argv) > 1 else 'calendar.ics'

    with open(file_name, 'r') as f :
        text = "".join( _ for _ in f.readlines())
        calendar = Calendar(text)
    
    event_dict = sort_events(calendar)
    event_dict = free_time(event_dict)
    try:
        june_12 = event_dict[(9, 25, 2022)]
        print(june_12)
    except:
        print("all free")
        


if __name__ == '__main__':
    main()