import time
import random
import hashlib
from yagmail.compat import text_type
from yagmail.error import YagAddressError
from email.utils import formataddr


def resolve_addresses(user, useralias, to, cc, bcc):
    """ Handle the targets addresses, adding aliases when defined """
    pass


def make_addr_alias_user(email_addr):
    pass


def make_addr_alias_target(x, addresses, which):
    pass


def add_subject(msg, subject):
    pass


def add_recipients_headers(user, useralias, msg, addresses):
    # Quoting the useralias so it should match display-name from https://tools.ietf.org/html/rfc5322 ,
    # even if it's an email address.
    # msg["From"] = '"{0}" <{1}>'.format(useralias.replace("\\", "\\\\").replace('"', '\\"'), user)
    # formataddr can support From chinese useralias, just like: mail_user = {'notice@test.com': '中文测试'}
    pass


def add_message_id(msg, message_id=None, group_messages=True):
    pass
