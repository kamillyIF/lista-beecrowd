n = int(input())  # Número de nomes a processar

for _ in range(n):
    nome = input()  # Nome a ser criptografado
    novaPalavra = ""  # Inicializa a string onde vamos armazenar a criptografia
    
    for letra in nome:
        if letra.isalpha():  # Se for letra
            novoCaractere = chr(ord(letra) + 3)  # Desloca a letra 3 posições
            novaPalavra += novoCaractere
        else:
            novaPalavra += letra  # Se não for letra, mantém o caractere inalterado

    novaPalavra = novaPalavra[::-1]  # Reverte o texto criptografado
    print(novaPalavra)  # Exibe a palavra criptografada
