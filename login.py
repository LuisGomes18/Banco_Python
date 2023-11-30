from json import JSONDecodeError
from extras import carregar_dados


def fazer_login(numero_conta, password, contas):
    for conta in contas:
        if conta['numero'] == numero_conta and conta['password']:
            return True
    return False

def login_conta():
    try:
        dados = carregar_dados()
        contas = dados['contas']

        numero_conta = input('Numero de conta: ')
        password = input('Password: ')

        if fazer_login(numero_conta, password, contas):
            print('\nAcess Granted\n')
        else:
            print('\nAcess Denied\n')
    except FileNotFoundError:
        print('Ficheiro com dados das contas nao encontrado')
    except JSONDecodeError:
        print('Erro na formatação do contas.json')
