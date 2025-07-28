teste = int(input())

for i in range(teste):
    texto1, texto2 = input().split()
    resultado = []
    tamanho = max(len(texto1), len(texto2))

    for a in range(tamanho):
        if a < len(texto1):
            resultado.append(texto1[a])
        if a < len(texto2):
            resultado.append(texto2[a])

    print("".join(resultado)) # join junta as string 