import math


total = 0

number = str(math.factorial(100))

i = 0

while i < len(number):
    num = int(number[i])
    total = total + num
    i = i+1
print(total)
