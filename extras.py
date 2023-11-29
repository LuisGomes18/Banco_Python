"""
Módulo para carregar dados de um arquivo JSON e manipular o sistema operacional.

Este módulo contém duas funções principais:

1. `carregar_dados`: Carrega os dados de um arquivo JSON.
    - Tenta abrir o arquivo "data/data.json" e carregar os dados.
    - Retorna um dicionário contendo os dados carregados do arquivo JSON.
    - Exceções:
        - JSONDecodeError: Se houver um erro na formatação do arquivo JSON.
        - FileNotFoundError: Se o arquivo não for encontrado.
        - Exception: Para outros erros inesperados durante o carregamento dos dados.

2. `sistema_operativo`: Limpa a tela do console com base no sistema operacional.
    - Detecta o sistema operacional e utiliza o comando apropriado para limpar a tela do console.
    - Exceção:
        - OSError: Se ocorrer um erro ao tentar limpar a tela do console.
"""
from json import load
from json import JSONDecodeError
import platform
import os


def carregar_dados():
    """
    Carrega os dados de um arquivo JSON.

    Tenta abrir o arquivo "data/data.json" e carregar os dados.

    Returns:
        dict: Um dicionário contendo os dados carregados do arquivo JSON.

    Raises:
        JSONDecodeError: Se houver um erro na formatação do arquivo JSON.
        FileNotFoundError: Se o arquivo não for encontrado.
        Exception: Para outros erros inesperados durante o carregamento dos dados.
    """
    try:
        with open('data/data.json', 'r', encoding='utf-8') as dd:
            dados = load(dd) # type: ignore
    except JSONDecodeError:
        print('Erro na formatação do .json')
    except FileNotFoundError:
        print('Ficheiro não existe')
    except Exception as erro:  # pylint: disable=broad-except
        print(f'ERRO: {erro}')
    else:
        return dados


def apagar_terminal():
    """
    Limpa a tela do console com base no sistema operacional.

    Detecta o sistema operacional e utiliza o comando apropriado para limpar a tela do console.

    Raises:
        OSError: Se ocorrer um erro ao tentar limpar a tela do console.
    """
    try:
        sistema_operacional = platform.system()

        if sistema_operacional == 'Windows':
            os.system('cls')
        elif sistema_operacional == 'Linux' or sistema_operacional == 'Darwin':
            os.system('clear')
        else:
            print(f'Não foi possível determinar o sistema operacional. Sistema detectado: {sistema_operacional}')
    except OSError as erro:
        print(f'Erro ao tentar limpar a tela do console: {erro}')
