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