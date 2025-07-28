# def italico():
#     global novoTexto
#     if palavra.startswith("_"):
#         novocaractere = palavra.replace("_", "<i>", 1)
#         novoTexto += novocaractere
#     elif palavra.endswith("_"):
#         novocaractere = palavra.replace("_", "<i>", 1)
#         novoTexto += novocaractere
#     else:
#         novoTexto += novocaractere

# palavra = input()
# novoTexto = " "

# italico()
# print(novoTexto )

def processa():
    global novoTexto
    italic_on = 0
    bold_on = 0

    for caractere in palavra:
        if caractere == '_':
            if italic_on == 0:
                novoTexto += "<i>"
                italic_on = 1
            else:
                novoTexto += "</i>"
                italic_on = 0
        elif caractere == '*':
            if bold_on == 0:
                novoTexto += "<b>"
                bold_on = 1
            else:
                novoTexto += "</b>"
                bold_on = 0
        else:
            novoTexto += caractere

palavra = input()
novoTexto = ""

processa()
print(novoTexto)
