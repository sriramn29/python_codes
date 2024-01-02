'''n = int(input("Enter a number: "))
fibo1 = 0
fibo2 = 1
print(fibo1)
print(fibo2)
for i in range(0,n-2):
        fibo = fibo1 + fibo2   
        fibo1 = fibo2
        fibo2 = fibo
        print(fibo)'''

#another method
        
def fib(n):
        # base condition 
        if n ==1 or n ==0:
                return 1
        # decomposition
        a= fib(n-1)
        b= fib(n-2)
        # recomposition
        return a+b
N = int(input())
print(fib(N))