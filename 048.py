soma = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma += c # o += e o mesmo que soma = soma + c
print(soma)