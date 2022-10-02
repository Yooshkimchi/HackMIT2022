# Oliver Rayner
# October 2022
 
# HackMIT 2022 Calendar thingy
 
from ics import Calendar, Event
from datetime import datetime
import sys
import mysql.connector
 
def main() :
       try:
               print("hi")
 
               connection = mysql.connector.connect(host='k8s-324c59a3-a2808d6e-94c9bbd386-b8e58f07e9b1e251.elb.us-east-2.amazonaws.com', user='SQLAdmin', password='Watermelon1!', database='SQLUser.test',)
               print("hi")
 
               cursor = connection.cursor()
               print("hi")
 
               mySql_insert_query = """INSERT INTO SQLUser.test (ID, Status, Priority, StartTime, ValidTimes, DateOf, Duration, Content) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """
              
               record = (1, 1, 5, 720, 'all free', '10/1', 60, 'testing')
              
               cursor.execute(mySql_insert_query, record)
              
               connection.commit()
 
               print("hi")
       except:
               print("couldn't")
 
if __name__ == '__main__':
   main()
