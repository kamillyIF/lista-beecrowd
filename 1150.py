X = int(input())

while True:
    Z = int(input())
    if Z > X:
        break

soma = 0
contador = 0
i = X

while soma <= Z:
    soma += i
    i += 1
    contador += 1

print(contador)
