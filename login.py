"""login module

This module implements a basic login system.

Functions:
- fazer_login(numero_conta, password, contas): Checks if login credentials are valid.
- login_conta(): Facilitates the user login process.

"""
from json import JSONDecodeError
from extras import carregar_dados


def fazer_login(numero_conta, password, contas):
    """Check if login credentials are valid.

    Args:
    numero_conta (str): The account number to be checked.
    password (str): The password to be checked.
    contas (list): A list of dictionaries containing account information.

    Returns:
    bool: True if login is successful, False otherwise.

    """
    for conta in contas:
        if conta["numero"] == numero_conta and conta["password"]:
            return True
    return False


def login_conta():
    """Facilitate the user login process.

    This function prompts the user for account number and password,
    then checks if the login credentials are valid using the fazer_login function.

    Prints:
    str: A message indicating whether access is granted or denied.

    Raises:
    FileNotFoundError: If the file with account data is not found.
    JSONDecodeError: If there is an error in the formatting of the contas.json file.

    """
    try:
        dados = carregar_dados()
        contas = dados["contas"]

        numero_conta = input("Numero de conta: ")
        password = input("Password: ")

        if fazer_login(numero_conta, password, contas):
            print("\nAcess Granted\n")
        else:
            print("\nAcess Denied\n")
    except FileNotFoundError:
        print("Ficheiro com dados das contas nao encontrado")
    except JSONDecodeError:
        print("Erro na formatação do contas.json")
