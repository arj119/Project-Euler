import math

total = 0
i = 0
while i != -1:
    num = str(i)
    length = int(len(num))
    total = 0

    for l in range(0,length):
        
        number = int(num[l])
        total = total + math.factorial(number)
    if total == i: print(i)
    i = i+1
