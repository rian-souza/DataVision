import os

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

def menu_principal():
    while True:
        print("1 - Ler arquivo CSV.\n2 - Arquivos lidos\n0 - Sair.")
        temp = validar(0, 2)
        if temp == 1:
            pass
        elif temp == 0:
            break

limpar_terminal()
print("=" * 25)
print("Bem-vindo ao DataVision !")
print("=" * 25)

menu_principal()
