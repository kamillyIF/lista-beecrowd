# prova
import sys

for frase in sys.stdin:
    maiusculo= False 
    novoTexto = ""

    for pos, letra in enumerate(frase):
        if (pos == 0 and letra.isalpha()) or letra.isalpha() and maiusculo == False:
            novoTexto += letra.upper()
            maiusculo = not maiusculo

        elif letra.isalpha() and maiusculo == True:
            novoTexto += letra.lower()
            maiusculo = not maiusculo

        else:
            novoTexto += letra  

    print(novoTexto, end= "")






