# PS: Count all the primes from M to N. print those primes as well.

M = int(input("Enter starting number: "))
N = int(input("Enter ending number: "))

count = 0

def is_prime(x):
    for a in range (2, x):
        if x%a == 0:
            #Not a prime
            return False
    #This is prime
    return True

for i in range(M, N+1):
    if is_prime(i):
        count = count + 1
        print(i)
print("Total prime numbers count is: ",count)