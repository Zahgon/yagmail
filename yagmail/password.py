try:
    import keyring
except (ImportError, NameError, RuntimeError):
    pass


def handle_password(user, password):  # pragma: no cover
    """ Handles getting the password"""
    pass


def register(username, password):
    """ Use this to add a new gmail account to your OS' keyring so it can be used in yagmail """
    pass
