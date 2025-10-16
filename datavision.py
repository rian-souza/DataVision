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
            nome_arquivo = input("Digite o nome do arquivo CSV (ou digite 0 para voltar): ")
            if nome_arquivo == '0':
                limpar_terminal()
                return None
            dataframe_arquivo = pd.read_csv(nome_arquivo)
            print("\nArquivo lido com sucesso !")
            print("\nVoltando ao menu principal ...")
            return dataframe_arquivo
        except FileNotFoundError:
            print(f"Arquivo {nome_arquivo} não encontrado.")
        except Exception as e:
            print(f"Erro ao ler o arquivo {nome_arquivo}: {e}")

def menu_estatistica(dataframe):
    while True:
        print("\nO que você gostaria de visualizar?\n\n1 - Gráfico de linhas\n2 - Gráfico de barras\n3 - Histograma\n4 - Informações diversas\n0 - Voltar\n")
        temp = validar(0, 4)
        numeric_df = dataframe.select_dtypes(include='number')
        
        if temp == 1:
            ax = numeric_df.plot(title="Gráfico de Linhas", figsize=(10,6), marker='o')
            ax.set_xlabel("Índice")
            ax.set_ylabel("Valores")
            ax.grid(True)
            plt.tight_layout()
            plt.show()
        elif temp == 2:
            ax = numeric_df.plot(kind="bar", title="Gráfico de Barras", figsize=(10,6))
            ax.set_xlabel("Índice")
            ax.set_ylabel("Valores")
            ax.grid(axis='y')
            plt.tight_layout()
            plt.show()
        elif temp == 3:
            numeric_df.hist(figsize=(12, 8), bins=15)
            plt.suptitle("Histogramas das Colunas Numéricas")
            plt.tight_layout()
            plt.show()
        elif temp == 4:
            with pd.option_context('display.float_format', '{:.2f}'.format):
                print(dataframe.info())
                print(dataframe.describe())
            input("\nPressione Enter para voltar ao menu...")
        elif temp == 0:
            limpar_terminal()
            break

def menu_principal():
    dataframe = None
    while True:
        print("\nO que você gostaria de fazer?\n\n1 - Ler arquivo CSV.\n2 - Analisar arquivo lido.\n0 - Sair.\n")
        temp = validar(0, 2)
        if temp == 1:
            dataframe = menu_ler_arquivo()
        elif temp == 2:
            if dataframe is not None:
                menu_estatistica(dataframe)
            else:
                print("Nenhum arquivo carregado ainda.")
        elif temp == 0:
            print("\nObrigado por usar o DataVision !\n")
            break

limpar_terminal()
print("=" * 25)
print("Bem-vindo ao DataVision !")
print("=" * 25)

menu_principal()
