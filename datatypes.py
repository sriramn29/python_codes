# 1.NUMBERS: int, float, bool
# PS: Calculate factorials. N! = 1*2*...*N
'''N = int(input("Enter the number: "))

factorial = 1
for i in range(1, N+1):
    factorial = factorial * i
print(factorial)'''

# PS: Take inputs (a, b, c) and tell me the roots of ax^2 + bx + c = 0.
'''import cmath
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
d = (b**2) - (4*a*c)
# find two solutions
sol1 = (-b + d**0.5)/(2*a)
sol2 = (-b - d**0.5)/(2*a)
print("The roots are: ", sol1, sol2)'''

# 2. STRINGS

'''a="sriram"
print(a)'''

# slicing: string[start:end:jump]
'''print(a[2])
print(a[:3])
print(a[::2])
print(a[::-1])'''

# PS: check if the input string is palindrome or not.
'''string = input("check palindrome for: ")
print(string == string[::-1])'''

# Operation with strings
'''fname = "Sri"
lname = "Ram"

fullname = fname + " " + lname # '+' with strings, mean concatenation
print(fullname)

print(fname*3) # '*' of strings mean repeat it that many times.'''

#object oriented way of calling functions. "Any string" is an object

'''print("sriram".upper())
print("29-12-2003".split("-"))'''

# 3. LISTS
'''sqaures_1 = [1, 4, 9, 16, 25]
sqaures_2 = [36, 49, 64, 81, 100]

# Intended: sqaures = [1,....,100]

squares = sqaures_1 + sqaures_2 # Adding two lists, concatenate them.

squares.append(121) # Append adds elements to the last
print(squares)

squares.pop() # pop removes last element
print(squares)

# squares.clear()
# print(squares)

#Slicing works on lists
print(squares[1::2])

print(squares[::-1])

print(squares, len(squares))'''



# 4. TUPLES

# when it is list
'''elements = [34, 7, 91, 9, 1, 20, 10]

print(elements)

elements[2] = 98  #You can edit the elements of the same array.

print(elements)  #Lists are mutable

#when it is tuples
elements2 = (34, 7, 91, 9, 1, 20, 10)
print(elements2)

#elements2[2] = 98  #You cannot edit the elements after tuple is made.
#print(elements2)  #Tuples are immutable'''

# 5. SETS
'''names = ["Sriram", "Sameer", "Sudharsan", "Siva", "Sarath","Sriram", "Siva"]

# PS: Tell me how many unique names are there in the list?

print(set(names), len(set(names)))

name = "Srisram"

# PS: Tell me how many unique characters are there.

print(set(name), len(set(name)))

set1 = {1, 2, 3, 2, 3}
set2 = {3, 4, 5, 3}

print(set1)
print(set2)

# Set Operations
print(set1 | set2)  # Union
print(set1 & set2)  # Intersection
print(set1 - set2)  # Left difference
print(set2 - set1)  # Right difference'''

# 6. Dictionaries

# Till now, in lists/arrays , you have done indexing like this.

'''array = [9.81, 3.14, 1.73, 1.61, 2.71]
# [gravity_const, pi, ....]

print(array[1])'''

# Can i do this? print(array[pi])

'''constants = {
    "pi" : 3.14,
    "golden_ratio" : 1.61,
    "gravity" : 9.81
    #key: value pair
}

print(constants["pi"])'''

exam_marks = {
    "Sriram": {
        "physics": 60,
        "chemistry": 70,
        "Maths":80
    },
    "Sameer": {
        "physics": 80,
        "chemistry": 70,
        "Maths":60
    }
}

print(exam_marks["Sriram"]["Maths"])

print(exam_marks.keys())
print(exam_marks.items())
print(exam_marks.values())