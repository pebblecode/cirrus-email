import boto3
import six

from flask import current_app, flash
from flask._compat import string_types

def send_email(to_email_addresses, email_body, subject, from_email, from_name, tags, reply_to=None, region='eu-west-1'):
    if isinstance(to_email_addresses, string_types):
        to_email_addresses = [to_email_addresses]

    client = boto3.client('ses', region_name=region)
    
    response = client.send_email(
        Source="%s <%s>" % (from_name, from_email),
        Destination={'ToAddresses': to_email_addresses},
        Message={
        'Subject': {
            'Data': subject
        },
        'Body': {
            'Html': {
                'Data': email_body
            }
        }
        })

    current_app.logger.info("Sent response: {result} tags: {tags}", extra={'result': response, 'tags':tags})
    
