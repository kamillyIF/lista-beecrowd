def pa(a1,r,n):
    if n == 1:
        return a1
    else:
        return a1 + pa(a1+r,r,n-1)
    
a1 = int(input())
r = int(input())
n= int(input())
result= pa(a1,r,n)
print(result)
