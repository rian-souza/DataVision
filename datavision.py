import os

def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def menu_principal():
    while True:
        print("1 - Ler arquivo CSV.\n2 - Arquivos lidos\n0 - Sair.")
        temp = int(input("Insira a opção desejada: "))
        if temp == 1:
            pass
        elif temp == 0:
            break

limpar_terminal()
print("=" * 25)
print("Bem-vindo ao DataVision !")
print("=" * 25)

menu_principal()