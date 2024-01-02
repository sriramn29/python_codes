# PS: 
# Input: a b c
# Output: side angle triangle

sides = ["Equi", "Iso", "Scalen"]
angle = ["Right", "obtuse", "Acute"]
a, b, c = list(map(int, input().split()))
if a == b == c:
    print(sides[0],angle[2],"triangle")
elif a == b or b == c or c == a:
    print(sides[1],"triangle")
else:
    print(sides[2],"triangle")
 