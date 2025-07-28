while True:
    try:
        n, l, c = map(int, input().split())
        texto = input()

        linhas = 0
        paginas = 1

        while len(texto) > 0:
            recorte = texto[:c]
            texto = texto[c:]

            while len(texto) > 0 and recorte[-1] != " " and texto[0] != " ":
                texto = recorte[-1] + texto
                recorte = recorte[:-1]

            texto = texto.strip()

            linhas += 1
            if linhas > l:
                paginas += 1  
                linhas = 1

        print(paginas)

    except EOFError:
        break
