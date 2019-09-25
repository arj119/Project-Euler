lives = 8
def lemons():
    lemon = str(input('What is the password?: '))
    if lemon == 'elephant':
        print('password accepted... ')
        print('you have '+str(lives)+' lives')
    else:
        print('incorrect password')
        lemons()

def con():
    con = int(input('What is 8 +  9: '))
    if con == 17:
        print('correct')
    else:
        print('incorrect')
        lives = lives - 1
        print('you have '+lives+' lives')

lemons()
while lives!=0:
    con()

print('you have lost')

                    
