import math as m

count = 0
num = 0
den = 0
x = 0

for i in range(2,5):
    for l in range(1,i-1):
        x=0
        num = m.factorial(i)
        den = (m.factorial(l))*(m.factorial(i-l))
        x = num/den
        print(x)
        if x > 1000000:
            count = count + 1

print(count)
