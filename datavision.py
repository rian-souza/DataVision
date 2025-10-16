import os
import pandas as pd
import matplotlib.pyplot as plt

def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def validar(a, b):
    while True:
        try:
            temp = int(input("Insira a opção desejada: "))
            if a <= temp <= b:
                return temp
            else:
                print(f"Insira uma opção entre {a} e {b}") 
        except ValueError:
            print("Digite somente números.")

def menu_ler_arquivo():
    while True:
        try:
            nome_arquivo = input("Digite o nome do arquivo CSV: ")
            dataframe_arquivo = pd.read_csv(nome_arquivo)
            print(dataframe_arquivo.head())
            return dataframe_arquivo
        except FileNotFoundError:
            print(f"Arquivo {nome_arquivo} não encontrado.")
        except Exception as e:
            print(f"Erro ao ler o arquivo {nome_arquivo}: {e}")

def menu_estatistica(dataframe):
    while True:
        print("1 - Gráfico de linhas\n2 - Gráfico de barras\n3 - Histograma\n4 - Informações diversas\n0 - Voltar")
        temp = validar(0, 4)
        if temp == 1:
            dataframe.plot()
            plt.show()
        elif temp == 2:
            dataframe.plot(kind="bar")
            plt.show()
        elif temp == 3:
            dataframe.hist(figsize=(10, 8))
            plt.show()
        elif temp == 4:
            print(dataframe.info())
            print(dataframe.describe())
        elif temp == 0:
            break

def menu_principal():
    dataframe = None
    while True:
        print("1 - Ler arquivo CSV.\n2 - Arquivos lidos\n0 - Sair.")
        temp = validar(0, 2)
        if temp == 1:
            dataframe = menu_ler_arquivo()
        elif temp == 2:
            if dataframe is not None:
                menu_estatistica(dataframe)
            else:
                print("Nenhum arquivo carregado ainda.")
        elif temp == 0:
            break

limpar_terminal()
print("=" * 25)
print("Bem-vindo ao DataVision !")
print("=" * 25)

menu_principal()
