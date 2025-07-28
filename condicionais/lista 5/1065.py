contadorP = 0
contadorI = 0
contadorPo = 0
contadorNe = 0
for c in range (5):
    a = int(input())
    if a % 2 == 0:
        contadorP += 1
    if a % 2 != 0:
        contadorI += 1
    if a > 0:
        contadorPo += 1
    if a < 0:
        contadorNe += 1
    
print(f"{contadorP} valor(es) par(es)")
print(f"{contadorI} valor(es) impar(es)")
print(f"{contadorPo} valor(es) positivo(s)")
print(f"{contadorNe} valor(es) negativo(s)")