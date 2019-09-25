

number = str((28433*(2**7830457))+1)
print(number)
length = int(len(number))
total = 0
for i in range(10):
    total = total + int(number[length -i])

print(total)
