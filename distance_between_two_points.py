# PS: Distance between two points

# input:
# x1 y1
# x2 y2

# output:
# distance between two points

x1, y1, r = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))

# formula for distance between two points
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(distance)

if(distance == r):
    print("oncircle")
elif(distance > r):
    print("outside the circle")
else:
    print("inside the circle")
