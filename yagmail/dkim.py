from email.mime.base import MIMEBase
from typing import NamedTuple

try:
    import dkim
except ImportError:
    dkim = None
    pass


class DKIM(NamedTuple):
    domain: bytes
    private_key: bytes
    include_headers: list
    selector: bytes


def add_dkim_sig_to_message(msg: MIMEBase, dkim_obj: DKIM) -> None:
    pass
