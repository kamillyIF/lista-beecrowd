x = int(input())

while x != 0:
  for i in range(1, x +1): # coloca o + 1 para fica ate o x
    if i == x:
      print(i)
    else:
      print(i, end=' ') # o end= é para o resultado fica na mesma linha

  x = int(input()) # vai pegar o x ate enquando ele for diferente de 0