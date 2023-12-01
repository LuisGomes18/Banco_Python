# pyright: reportOptionalSubscript=false
"""login module

This module implements a basic login system.

Functions:
- fazer_login(numero_conta, password, contas): Checks if login credentials are valid.
- login_conta(): Facilitates the user login process.

"""
from json import JSONDecodeError
from random import randint
from extras import carregar_dados
from extras import guardar_dados


def fazer_login(numero_conta, password, contas): # pylint: disable=W0613
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
    JSONDecodeError: If there is an error in the formatting of the login.json file.

    """
    try:
        dados = carregar_dados()
        contas = dados["contas"]

        numero_conta = input("Numero de conta: ")
        password = input("Password: ")

        if fazer_login(numero_conta, password, contas):
            print("\nAcess Granted\n")
            dados["usuario_atual"] = numero_conta
            guardar_dados(dados)  # Corrigir para guardar os dados, não apenas as contas
        else:
            print("\nAcess Denied\n")
    except FileNotFoundError:
        print("Ficheiro com dados das contas nao encontrado")
    except JSONDecodeError:
        print("Erro na formatação do contas.json")



def criar_conta():
    """
    Função para criar uma nova conta, gerando um número único 
    para a conta e solicitando ao usuário uma senha válida.

    Returns:
    None
    """
    dados = carregar_dados()
    contas = dados["contas"]

    lista_contas = [conta["numero"] for conta in contas]

    numero_conta = str(randint(111, 999))
    while numero_conta in lista_contas:
        numero_conta = str(randint(111, 999))

    print(f"Sua conta é: {numero_conta}")

    password = input("Insira a sua senha: ")
    while len(password) < 4 or len(password) > 16:
        print("Senha inválida. A senha deve ter entre 4 e 16 caracteres.")
        password = input("Insira a sua senha: ")

    nova_conta = {"numero": numero_conta, "senha": password}
    contas.append(nova_conta)
    dados["contas"] = contas

    guardar_dados(dados)
