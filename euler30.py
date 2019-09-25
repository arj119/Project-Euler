

count = 0

for i in range(1,1000000):
    for l in range(1,1000000):
        number = str(i**l)
        length = int(len(number))
        if length == l:
            
            count = count+1
print(count)














    
        
