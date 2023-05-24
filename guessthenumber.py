import random

while True:
    
    fix = random.randint(1,10)

    i = 1
    while i<=3:
        guess = int(input('enter your number: ' ))
        if fix == guess:
            print('you won the game')
            break
        else:
            print('wrong guess')
        i = i+1

    else:
        print('you lost the game')


    ch = input('Do you wnat to play again?(yes/no)')
    if ch == 'no':
        break
print('Game over')

    

    
        
        
