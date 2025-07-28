# valor = int(input())
# n1,n2 = map(int, input().split())
# soma = 0 
# if n1 > n2:
#     for i in range(n2 + 1, n1): 
#         if i % 2 != 0:
#             soma += i  
# else:
#     for i in range(n1 + 1, n2): 
#         if i % 2 != 0:
#             soma += i  

# print(soma)

valor = int(input())  

for a in range(valor):
    n1, n2 = map(int, input().split())
    soma = 0 
    if n1 > n2:
        for i in range(n2 + 1, n1): 
            if i % 2 != 0:
                soma += i  
    else:
        for i in range(n1 + 1, n2): 
            if i % 2 != 0:
                soma += i  

    print(soma)

