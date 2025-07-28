contadorIn = 0 # in - dentro
contarOut = 0 # out - fora
n = int(input())

for i in range(0,n):
    num = int(input())

    if num >= 10 and num <= 20:
        contadorIn += 1
    else:
        contarOut += 1
    
print("{} in".format(contadorIn))
print("{} out".format(contarOut))