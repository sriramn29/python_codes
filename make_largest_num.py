# PS: What is the max number you can create by attaching/ connecting elemets of this array

# 9 91 7 34 20 1 10 => 99173420110


elements = [34, 7, 91, 9, 1, 20, 10]

elements2 = []
for i in range(len(elements)):
    elements2.append(str(elements[i]))

print(elements2)

def double_num(x):
    return x*2

elements2.sort(key=double_num, reverse=True)

print((int("".join(elements))))
