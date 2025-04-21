import math

n1, n2, n3, n4 = map(float, input().split())
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
print("Media: {:.1f}".format(media))

if media >= 7.0:
    print("Aluno aprovado.")
    
elif media < 5.0:
     print("Aluno reprovado.")

elif media >= 5.0 and media <= 6.9:
     print("Aluno em exame.")
     nota = float(input())
     print("Nota do exame: {}".format(nota))
     media2 = math.ceil(media + nota) / 2
     
     if media2 > 5.0:
     print("Aluno aprovado.")
     print("Media final: {:.1f}".format(media2))
     
     else:
         print("Aluno reprovado.")