# Entrada de dados
h_inicial, m_inicial, h_final, m_final = map(int, input().split())

# Convertendo tudo para minutos desde meia-noite
inicio_em_minutos = h_inicial * 60 + m_inicial
fim_em_minutos = h_final * 60 + m_final

# Se o fim for menor ou igual ao início, significa que o jogo passou da meia-noite
if fim_em_minutos <= inicio_em_minutos:
    fim_em_minutos += 24 * 60  # Adiciona 24 horas em minutos

# Calcula a duração total em minutos
duracao_total = fim_em_minutos - inicio_em_minutos

# Converte de volta para horas e minutos
duracao_horas = duracao_total // 60
duracao_minutos = duracao_total % 60

# Exibe o resultado
print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")

