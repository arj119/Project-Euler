


def factor(x):
    for i in range(1, 20):
        if x % i == 0:
            print(i)
    
num = int(input('enter number: '))

factor(num)
 
