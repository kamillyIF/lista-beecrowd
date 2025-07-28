contar = 0
soma = 0
for b in range (6):
    n = float(input())
    if n > 0:
        contar += 1 
        soma += n
media = soma / contar 
print(f"{contar} valores positivos")
print("{:.1f}".format(media))