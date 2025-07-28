contador = int(input())

for i in range(contador):
    textoMisturado = input()
    textoCorreto = ""
    metadeE = textoMisturado[:len(textoMisturado)// 2] # : no inicio marca o começo 
    metadeD = textoMisturado[len(textoMisturado)// 2:] # : no final marca o fim

    textoCorreto += metadeE[::-1] # de traz para frene o -1
    textoCorreto += metadeD[::-1]

    print(textoCorreto)