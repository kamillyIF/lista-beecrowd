a, b, c = map(int, input().split())

num1 = a
num2 = b
num3 = c

valores = [a, b, c]
valores.sort()

for j in valores:
    
    print("{}".format(j))
    
print()

print(num1)
print(num2)
print(num3)