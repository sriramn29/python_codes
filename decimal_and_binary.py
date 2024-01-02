'''binary_list = []
a = int(input())
rem = 0
while a!=0:
    rem = a%2
    binary_list.append(rem)
    a=a//2
binary_list = binary_list[::-1]
for num in binary_list:
    print(num,end='')'''
# another method
def dec_to_bin(n):
    # Base condition
    if n > 1:
        dec_to_bin(n//2)
    print(n%2, end="")
N = int(input())
dec_to_bin(N)


    
