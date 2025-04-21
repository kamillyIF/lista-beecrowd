dias = int(input())

anos = dias // 365
restAnos = dias % 365

meses = restAnos // 30
dias = restAnos % 30

print(anos, "ano(s)")
print(meses, "mes(es)")
print(dias, "dia(s)")