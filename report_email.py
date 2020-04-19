#!/usr/bin/env python3

import os
import datetime
import reports
import emails


source_text_folder = os.path.abspath('./supplier-data/descriptions')
files = os.listdir(source_text_folder)

data_list = []
for file in files:
    with open(os.path.join(source_text_folder, file), 'r') as f:
        name = f.readline().strip()
        weight = f.readline().strip().split()[0] + ' lbs'
        f.close()
        data_list.append('name: {}<br/>weight: {}'.format(name, weight))

pdf_header = 'Processed Update on {}'.format(datetime.date.today().strftime('%B %d, %Y'))
pdf_body = '<br/><br/>'.join(data_list)

if __name__ == '__main__':
    reports.generate_report('/tmp/processed.pdf', pdf_header, pdf_body)
    sender = 'automation@example.com'
    recipient = 'username@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    attachment_path = '/tmp/processed.pdf'
    emails.send(emails.generate_email(sender, recipient, subject, body, attachment_path))
