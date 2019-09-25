
def binarySearch(alist, x):
    iterations = 0
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        iterations = iterations + 1
        midpoint = (first + last)//2
        if alist[midpoint] == x:
            found = True
        elif x < midpoint:
            last = midpoint - 1
        elif x > midpoint:
            first = midpoint + 1

    return found and iterations

MADlist = list(range(1000000))
print(binarySearch(MADlist, 14315))

    
             
    
