number = 0

for i in range(1000000, 0, -1):
    count = 0
    starting = i
    while i != 1:
        if (i % 2) == 0:
            i = i/2
            count =  count + 1
        else:
            i = (3*i) + 1
            count = count + 1
    if count > number:
        number = count
        print(starting)
print('finished')


        
        
