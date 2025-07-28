# Faça um algoritmo que leia uma variável e some 5 caso seja par ou 
# some 8 caso seja ímpar, imprimir o resultado desta operação.


# a = int(input("digite um numero: "))

# if a % 2 == 0:
#     resultado = a + 5

# else:
#     resultado = a + 8
        
# print(f"Resultado da operação {resultado}")

# for c in range(2,201,2):
#     print("{} é par".format(c))

# for c in range(1,200,2):
#     print("{} é impar".format(c))

n = int(input())

if n == 1 :
    print("0")

elif n == 2:
    print("0 1", end='')

else:
    anterior = 0
    proximo = 1
    print("0 1", end=' ')

    for i in range(n - 2):
        soma = anterior + proximo
        anterior = proximo
        proximo = soma 

        if i == n - 3:
             print(proximo)
        else:
             print(proximo, end=' ')
