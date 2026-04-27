"""
Adapted from:
http://blog.macuyiko.com/post/2016/how-to-send-html-mails-with-oauth2-and-gmail-in-python.html

1. Generate and authorize an OAuth2 (generate_oauth2_token)
2. Generate a new access tokens using a refresh token(refresh_token)
3. Generate an OAuth2 string to use for login (access_token)
"""
import os
import base64
import json
import getpass

try:
    from urllib.parse import urlencode, quote, unquote, parse_qs, urlsplit
    from urllib.request import urlopen
except ImportError:
    from urllib import urlencode, quote, unquote, urlopen
    from urlparse import parse_qs, urlsplit

try:
    input = raw_input
except NameError:
    pass

GOOGLE_ACCOUNTS_BASE_URL = 'https://accounts.google.com'
REDIRECT_URI = 'http://localhost'


def command_to_url(command):
    pass


def url_format_params(params):
    pass


def generate_permission_url(client_id):
    pass


def call_authorize_tokens(client_id, client_secret, authorization_code):
    pass


def call_refresh_token(client_id, client_secret, refresh_token):
    pass


def generate_oauth2_string(username, access_token, as_base64=False):
    pass


def get_authorization(google_client_id, google_client_secret):
    pass


def refresh_authorization(google_client_id, google_client_secret, google_refresh_token):
    pass


def get_oauth_string(user, oauth2_info):
    pass


def get_oauth2_info(oauth2_file: str, email_addr: str):
    pass
