#Problem Statement: Upto N, I need to find all (a, b, c) triplets.
#Also, i want to have a count of them.
N=int(input("Enter the value of N:"))

count = 0

#LOOPING
#range(x, y) = start from x, go upto y-1
for a in range(1, N+1):
    for b in range(a, N+1):
        for c in range(b, N+1):
            if c*c == (a*a + b*b):
                print(a, b, c)
                count = count + 1
print("Count ",count)
