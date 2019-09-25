
count = 0
def rotate(l, n):
    return l[n:] + l[:n]
def check(x):
    for m in range(2,x):
        if (x%m) == 0:
            break
        else:
            global count
            count  = count + 1
            print(x)

for i in range(100,1000000):
    for l in range(i-1):
        number = i
        check(number)
        number = int(''.join(rotate(list(str(i)),l)))
        
print(count)       

