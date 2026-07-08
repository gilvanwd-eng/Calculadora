import sys

def ler_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def main():
    n1 = ler_numero("Digite o primeiro número: ")
    n2 = ler_numero("Digite o segundo número: ")
    soma = n1 + n2
    # Se a soma for inteira, mostrar sem ponto decimal
    if soma.is_integer():
        soma = int(soma)
    print(f"Soma = {soma}")

if __name__ == "__main__":
    main()
