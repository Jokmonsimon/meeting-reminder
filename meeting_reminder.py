#!/usr/bin/env python3

# To trigger the error, LANG=en_US.UTF-8

import datetime
import email
import smtplib
import sys

def usage():
    print("send_reminders: Send Meeting Reminder")
    print()
    print("invocation:")
    print("     send_reminders 'date|Meeting Title|Emails' ")
    return 1

def dow(date):
    dateobj = datetime.datetime.strtime(date, r"%d/%m?%Y")
    return dateobj.strftime("%A")

def message_template(date, title):
    message = email.message.EmailMessage()
    weekday = dow(date)
    # message['Subject'] = f'Meeting Reminder: "{title}"'
    message['Subject'] = "Meeting Reminder: {}".format(title)
    message.set_content(f'''
     Hi all!
      This is a quick mail to remind you all that we have a meeting about:
       "{title}" 
       the {weekday} {date}.
       See you there.
       ''')
    return message