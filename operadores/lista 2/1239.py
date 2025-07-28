# MEU CODIGO 
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

# CODIGO DO CHAT NA SUA VERSÃO
# def formatar():
#     global novoTexto
#     global it, negrito
#     for letra in frase:
#         if letra == '_':
#             if it == 0:
#                 novoTexto += "<i>"
#                 it = 1
#             else:
#                 novoTexto += "</i>"
#                 it = 0
#         elif letra == '*':
#             if negrito == 0:
#                 novoTexto += "<b>"
#                 negrito = 1
#             else:
#                 novoTexto += "</b>"
#                 negrito = 0
#         else:
#             novoTexto += letra

# frase = input()
# novoTexto = ""
# it = 0        # 0 = fechado, 1 = aberto
# negrito = 0   # 0 = fechado, 1 = aberto

# formatar()
# print(novoTexto)

# CODIGO DO CHAT UTILIZANDO MINHA LOGICA 
def aplicar_formatacao():
    global novoTexto
    partes = frase.split(" ")  # separa por palavras
    for palavra in partes:
        if "_" in palavra:
            if contIt % 2 == 0:
                palavra = palavra.replace("_", "<i>", 1)
            else:
                palavra = palavra.replace("_", "</i>", 1)
            global contIt
            contIt+= 1

        if "*" in palavra:
            if contNe % 2 == 0:
                palavra = palavra.replace("*", "<b>", 1)
            else:
                palavra = palavra.replace("*", "</b>", 1)
            global contNe
            contNe += 1

        novoTexto += palavra + " "

frase = input()
novoTexto = ""
contIt = 0
contNe = 0

aplicar_formatacao()
print(novoTexto.strip())
