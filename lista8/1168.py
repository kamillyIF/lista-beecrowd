leds = {"0":6, "1":2, "2":5, "3":5, "4":4, "5":5, "6":6, "7":3, "8":7, "9":6}

n = int(input())
soma = 0

for i in range (n):
    n = input()
    total = 0
    for letra in n:
        soma += leds[letra]
    print(soma)
    print(leds.values())

# outra forma de fazer 

teste = int(input())

for i in range(teste):
    n = input()
    soma = 0

    for letra in n:
        if letra == "0":
            soma += 6
        elif letra == "1":
            soma += 2 
        elif letra == "2":
            soma += 5
        elif letra == "3":
            soma += 5
        elif letra == "4":
            soma += 4
        elif letra == "5":
            soma += 5
        elif letra == "6":
            soma += 6
        elif letra == "7":
            soma += 3
        elif letra == "8":
            soma += 7
        elif letra == "9":
            soma += 6
    print("{} leds".format(soma))

          

