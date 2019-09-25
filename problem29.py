array = []

for a in range(2,101):
    for b in range(2,101):
        if ((a**b) in array) == False:
            array.append(a**b)
  

print(len(array))
