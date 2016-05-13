import boto.ses

from flask import current_app


def send_email(to_email_addresses, email_body, subject, from_email, from_name, tags, reply_to=None, region='eu-west-1'):
    if isinstance(to_email_addresses, string_types):
        to_email_addresses = [to_email_addresses]

    conn = boto.ses.connect_to_region(region=region)
    
    result = conn.send_email(
        source="%s <%s>" % (from_name, from_email),
        subject=subject,
        html_body=html,
        to_addresses=to_email_addresses,
        format='html')

    current_app.logger.info("Sent mail: " + result)
    
    