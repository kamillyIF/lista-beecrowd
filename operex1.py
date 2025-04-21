# Testar se os números são neutro, positivos ou negativos 
n = int(input("Digite um número: "))

if n > 0:
    print("é positivo")
else: 
    if n < 0:
        print("é negativo")

    if n == 0:
        print("é neutro")

