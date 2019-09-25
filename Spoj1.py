number = 0

def UserIn():
    number = input()
    return number

UserIn()

if number == 42:
    exit
else:
    print(number)
    UserIn()
