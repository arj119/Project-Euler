total = 0
for x in range(10000):
    y = 0
    z = 0
    for i in range(1, x-1):
        if (x % i) == 0:
            y = y + i
    for l in range(1, y-1):
        if (y % l) == 0:
            z = z + l
    if z == x:
        print(x, 'and', y)
        total = total + x + y

print(total)
  
    
            

