#!/usr/bin/env python3

import socket
import psutil
import emails


sender = 'enter@your.addresses'
recipient = 'enter@your.addresses'
body = 'Please check your system and resolve the issue as soon as possible.'

cpu = psutil.cpu_percent()
mem = psutil.virtual_memory().available
disk = psutil.disk_usage('/').percent

# CPU usage is over 80% - Error - CPU usage is over 80%
if cpu >= 80:
    subject = 'Error - CPU usage is over 80%'
    emails.send(emails.generate_email(sender, recipient, subject, body))

# available memory is less than 500MB - Error - Available memory is less than 500MB
if mem <= 500*1024*1024:
    subject = 'Error - Available memory is less than 500MB'
    emails.send(emails.generate_email(sender, recipient, subject, body))

# Available disk space is lower than 20% - Error - Available disk space is less than 20%
if disk >= 80:
    subject = 'Error - Available disk space is less than 20%'
    emails.send(emails.generate_email(sender, recipient, subject, body))

# hostname "localhost" cannot be resolved to "127.0.0.1" - Error - localhost cannot be resolved to 127.0.0.1
try:
    socket.gethostbyname('localhost')
except socket.error:
    subject = 'Error - localhost cannot be resolved to 127.0.0.1'
    emails.send(emails.generate_email(sender, recipient, subject, body))
