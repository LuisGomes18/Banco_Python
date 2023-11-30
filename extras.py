from json import load
from json import dump
from json import JSONDecodeError
import platform
import os


def carregar_dados():
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
    try:
        with open("data/login.json", "w", encoding="utf-8") as dd:
            dump(dados, dd)
    except Exception as erro:  # pylint: disable=broad-except
        print(f"ERRO ao guardar dados: {erro}")


def apagar_terminal():
    try:
        sistema_operacional = platform.system()

        if sistema_operacional == "Windows":
            os.system("cls")
        elif sistema_operacional == "Linux" or sistema_operacional == "Darwin":
            os.system("clear")
        else:
            print(
                f"Não foi possível determinar o sistema operacional. Sistema detectado: {sistema_operacional}"
            )
    except OSError as erro:
        print(f"Erro ao tentar limpar a tela do console: {erro}")
