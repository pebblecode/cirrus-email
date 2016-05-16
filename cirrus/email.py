import boto.ses
import six

from flask import current_app, flash
from flask._compat import string_types

def send_email(to_email_addresses, email_body, subject, from_email, from_name, tags, reply_to=None, region='eu-west-1'):
    if isinstance(to_email_addresses, string_types):
        to_email_addresses = [to_email_addresses]

    conn = boto.ses.connect_to_region(region)
    
    result = conn.send_email(
        source="%s <%s>" % (from_name, from_email),
        subject=subject,
        body=None,
        html_body=email_body,
        to_addresses=to_email_addresses,
        format='html')

    current_app.logger.info("Sent {result}", extra={'result': result})
