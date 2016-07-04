import boto3
import six

from flask import current_app, flash
from flask._compat import string_types

def send_email(from_address, to_addresses, subject, body_text, **kwargs):
    """
    Sends an email via Amazon SES service

    Args:
        from_address (str): The from email address.
        to_addresses (:list:`str`]): The addressees email addresses.
        subject (str): The subject line.
        body_text (str): The text content of the email body

        **kwargs:
            from_email_name (str): The senders name. Defaults to None.
            tags (:list:`str`): Tags for the log message emitted. Defaults to None.
            reply_to_addresses (:list:`str`): The reply to addresses. Defaults to None.
            region (str): The aws region. Defaults to 'eu-west-1'.
            body_html (str): The html body content. Defaults to None.
            char_set (str): The character set encoding for the message body. Defaults to 'UTF-8'.
            cc_addresses (:list:`str`): The cc addresses. Defaults to None.
            bcc_addresses (:list:`str`): The bcc addresses. Defaults to None.

    """

    options = {
            'from_email_name': None,
            'tags': None,
            'reply_to_addresses': None,
            'region': 'eu-west-1',
            'body_html': None,
            'char_set': 'UTF-8',
            'cc_addresses': None,
            'bcc_addresses': None
            }

    options.update(kwargs)

    if isinstance(to_addresses, string_types):
        to_addresses = [to_addresses]

    if options['from_email_name'] is not None:
        source = "{0} <{1}>".format(options['from_email_name'], from_address)
    else:
        source = from_address

    mail_data = {
            'Source': source,
            'Destination': {
                'ToAddresses': to_addresses
                },
            'Message': {
                'Subject': {
                    'Data': subject,
                    'Charset': options['char_set']
                    },
                'Body': {
                    'Text': {
                        'Data': body_text,
                        'Charset': options['char_set']
                        }
                    }
                }
            }

    if options['reply_to_addresses'] is not None:
        mail_data['ReplyToAddresses'] = options['reply_to_addresses']

    if options['body_html'] is not None:
        mail_data['Message']['Body']['Html'] = {
                'Data': options['body_html'],
                'Charset': options['char_set']
                }

    client = boto3.client('ses', region_name=options['region'])
    response = client.send_email(**mail_data)
    current_app.logger.info("Sent response: {result} tags: {tags}", extra={'result': response, 'tags':options['tags']})

