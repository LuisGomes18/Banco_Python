"""
Módulo para manipulação de dados e operações no terminal.

Este módulo fornece funções para carregar e salvar dados em um arquivo JSON,
bem como para limpar a tela do terminal de acordo com o sistema operacional.

Funções:
    - carregar_dados: Carrega dados de um arquivo JSON.
    - guardar_dados: Salva dados em um arquivo JSON.
    - apagar_terminal: Limpa a tela do terminal de acordo com o sistema operacional.

Exceções:
    - JSONDecodeError: Levantada se houver um erro na formatação JSON ao carregar dados.
    - FileNotFoundError: Levantada se o arquivo JSON não for encontrado ao carregar dados.
    - OSError: Levantada se houver um erro ao tentar limpar a tela do console.

Exemplo de uso:

    from nome_do_modulo import carregar_dados, guardar_dados, apagar_terminal

    # Carregar dados do arquivo JSON
    dados = carregar_dados()

    # Realizar operações com os dados

    # Salvar dados no arquivo JSON
    guardar_dados(dados)

    # Limpar a tela do terminal
    apagar_terminal()
"""

from json import load
from json import dump
from json import JSONDecodeError
import platform
import os


def carregar_dados():
    """
    Carrega os dados do arquivo JSON "data/login.json".

    Tenta abrir o arquivo e carregar os dados usando a função `load` do módulo `json`.
    Se o arquivo não existir, imprime uma mensagem indicando que o arquivo não foi encontrado.
    Se houver um erro na formatação JSON, imprime uma mensagem de erro.
    Se ocorrer qualquer outra exceção, imprime a mensagem de erro correspondente.

    Retorna os dados carregados se a operação for bem-sucedida.

    :return: Dados carregados do arquivo JSON, ou None se houver erro.
    :rtype: dict or None
    """
    try:
        with open("data/login.json", "r", encoding="utf-8") as dd:
            dados = load(dd)  # type: ignore
    except JSONDecodeError:
        print("Erro na formatação do .json")
    except FileNotFoundError:
        print("Ficheiro não existe")
    except Exception as erro:  # pylint: disable=broad-except
        print(f"ERRO: {erro}")
    else:
        return dados


def guardar_dados(dados):
    """
    Guarda os dados no arquivo JSON "data/login.json".

    Tenta abrir o arquivo no modo de escrita e usa a função `dump` do módulo `json`
    para escrever os dados no arquivo com indentação de 4 espaços.
    
    Em caso de erro ao guardar os dados, imprime uma mensagem de erro.

    :param dados: Dados a serem salvos no arquivo JSON.
    :type dados: dict

    :return: None
    """
    try:
        with open("data/login.json", "w", encoding="utf-8") as dd:
            dump(dados, dd, indent=4)
    except Exception as erro:  # pylint: disable=broad-except
        print(f"ERRO ao guardar dados: {erro}")


def apagar_terminal():
    """
    Limpa o terminal/console de acordo com o sistema operacional.

    Detecta o sistema operacional e utiliza o comando apropriado para limpar
    a tela do terminal. Suporta sistemas Windows, Linux e MacOS.

    :raises OSError: Se houver um erro ao tentar limpar a tela do console.

    :return: None
    """
    try:
        sistema_operacional = platform.system()

        if sistema_operacional == "Windows":
            os.system("cls")
        elif sistema_operacional == "Linux" or sistema_operacional == "Darwin":
            os.system("clear")
        else:
            print(
                f"Não foi possível determinar o sistema operacional. \
Sistema detectado: {sistema_operacional}"
            )
    except OSError as erro:
        print(f"Erro ao tentar limpar a tela do console: {erro}")
