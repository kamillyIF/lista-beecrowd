def formatacao():
    global novoTexto
    global cont_it, cont_negrito

    for caractere in frase:
        if caractere == "_":
            if cont_it % 2 == 0:
                novoTexto += "<i>"
            else:
                novoTexto += "</i>"
            cont_it += 1
        elif caractere == "*":
            if cont_negrito % 2 == 0:
                novoTexto += "<b>"
            else:
                novoTexto += "</b>"
            cont_negrito += 1
        else:
            novoTexto += caractere 

frase = input()
novoTexto = ""
cont_it = 0
cont_negrito = 0

formatacao()
print(novoTexto, end="")
