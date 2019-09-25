total = 0
choice1 = 0
choice2 = 0
i = 0

       

while i < 1000001:
    dec = str(i)
    Bin = str(bin(i))
    if dec == dec[::-1] and Bin == Bin[::-1]:
        total = total + i
    
    
    
    i= i+1
print(total)
