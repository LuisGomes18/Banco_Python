# pylint: disable=W0621
# pylint: disable=C0103


def login():
    """
    Prompts the user for a username and password, and checks if they match a predefined
    set of credentials. If the credentials match, access is granted; otherwise, access is denied.

    Usage:
    1. Call the login() function.
    2. Enter a username and password when prompted.

    Example:
    >>> login()
    Username: luis
    Password: luis
    Access Granted
    """
    VERMELHO = '\033[31m'
    VERDE = '\033[32m'
    ORIGINAL = '\033[0m'

    username = str(input('\n Username: '))
    password = str(input(' Password: '))
    if username == 'luis' and password == 'luis':  #! TMP
        print(VERDE + "\nAccess Granted\n" + ORIGINAL)
    else:
        print(VERMELHO + "\nAccess Denied\n" + ORIGINAL)
