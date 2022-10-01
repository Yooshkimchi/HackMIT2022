# Oliver Rayner
# October 2022

# HackMIT 2022 Calendar thingy

from ics import Calendar, Event

def main() :

    with open('calendar.ics', 'r') as f :
        text = "".join( _ for _ in f.readlines())
        calendar = Calendar(text)
    
    print(calendar.events)


if __name__ == '__main__' :
    main()