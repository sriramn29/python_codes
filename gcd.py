'''a=int(input("a: "))
b=int(input("b: "))
while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
print(a)'''

# another method
'''a, b = list(map(int, input().split()))
def gcd(a, b):
    #base condition
    if a%b == 0:
        return b
    #decomposition
    ans = gcd(b, a%b)
    # recompose
    return ans
print(gcd(a, b))'''

# another method
a, b = list(map(int, input().split()))
def gcd(a, b):
    if(a==b):
        return a
    elif(a>b):
        return gcd(a-b,b)
    elif(b>a):
        return gcd(a,b-a)
print(gcd(a, b))