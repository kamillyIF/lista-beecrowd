n = int(input())

for i in range (n):
    valor = int(input())
    
    if valor == 0:
        print("NULL")
        
    elif valor %2 == 0 and valor < 0:
        print("EVEN NEGATIVE") # par negativo
    elif valor %2 == 0 and valor > 0:
        print("EVEN POSITIVE") # par positivo
    elif valor %2 != 0 and valor > 0:
        print("ODD POSITIVE") # impares positivos
    elif valor %2 != 0 and valor < 0:
        print("ODD NEGATIVE") # impares negativos