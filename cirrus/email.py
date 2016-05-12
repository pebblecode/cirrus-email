import boto.ses

from flask import current_app


def send_email(to_email_addresses, email_body, subject, from_email, from_name, tags, reply_to=None):
    if isinstance(to_email_addresses, string_types):
        to_email_addresses = [to_email_addresses]

    # TODO: this seems strange to have to pass credentials from here.
    conn = boto.ses.connect_to_region(
        region=current_app.config['AWS_DEFAULT_REGION'],
        aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'])
    
    result = conn.send_email(
        source="%s <%s>" % (from_name, from_email),
        subject=subject,
        html_body=html,
        to_addresses=to_email_addresses,
        format='html')

    current_app.logger.info("Sent mail: " + result)
    
    