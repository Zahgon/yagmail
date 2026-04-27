import datetime
import email.encoders
import io
import json
import mimetypes
import os
import sys
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

from yagmail.dkim import add_dkim_sig_to_message
from yagmail.headers import add_message_id
from yagmail.headers import add_recipients_headers
from yagmail.headers import add_subject
from yagmail.utils import raw, inline

PY3 = sys.version_info[0] > 2


def dt_converter(o):
    pass


def serialize_object(content):
    pass


def prepare_message(
    user,
    useralias,
    addresses,
    subject,
    contents,
    attachments,
    headers,
    encoding,
    prettify_html=True,
    message_id=None,
    group_messages=True,
    dkim=None,
):
    # check if closed!!!!!! XXX
    """Prepare a MIME message"""
    pass


def prepare_contents(contents, encoding):
    pass


def get_mime_object(is_marked_up, content_string, encoding):
    pass
