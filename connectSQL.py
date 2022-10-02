# Oliver Rayner
# October 2022

# HackMIT 2022 Calendar thingy

from ics import Calendar, Event
from datetime import datetime
import sys
import mysql.connector

def main() :
        connection = mysql.connector.connect(user='SQLAdmin', password='Watermelon1!',
        database='SQLUser.test',
        host='k8s-324c59a3-a2808d6e-94c9bbd386-b8e58f07e9b1e251.elb.us-east-2.amazonaws.com')
        print("hi")
