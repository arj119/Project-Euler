count=0
x=0
y=1
Len = 0
while Len != 1000:
    x,y = x+y, x
    count = count+1
    Len = int(len(str(x)))
print(count)
    
