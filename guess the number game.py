import random
#level
print("________Welcome To The Game________")
print('About :-')
print('''The foundation of the number guessing game in Python is the player's assumption
that they can guess a number within the given range.
The player wins the game if they correctly guess the target number; else, they lose.''')
print('---LEVELS ---')
print("B: Beginner")
print("M: Moderate")
print("H: High")
l= input('Enter  level: ')
if l=='b' or l=='B':
    print('---Your Level is Beginner---')
elif l=='m' or l=='M':
    print('---Your Level is Moderate---')
else:
    print('---Your Level is Advance---')
if l=='b' or l=='B':
    n_o_t = 10
    n = random.randint(1,100)
    while(n_o_t >0):
        t= int(input("Guess The Number between 1 and 100 :  "))
        if t==n:
            print('***YOU WON!!***')
            break
        elif t<n:
                print('TOO LOW :(' )
                print('Chances Left: ',n_o_t-1)
        else :
            print('TOO HIGH :(')
            print('Chances Left: ',n_o_t-1)
        n_o_t -=1
    if n_o_t == 0:
        print('--NO ATTEMPTS LEFT--')
    d = input('Did Yoy Enjoyed ? ')
    if d[0]=='y' or d[0] == 'Y':
        print('THANKS ')
    else:
        print('We will try to make it more efficient.')
if l=='m' or l=='M':
    n_o_t = 6
    n = random.randint(1,50)
    while(n_o_t !=0):
        t= int(input("Guess The Number between 1 and 50 :  "))
        if t==n:
            print('***YOU WON!!***')
            break
        elif t< n:
            print('TOO LOW :(')
            print('Chances Left: ',n_o_t-1)
        else :
            print('TOO HIGH :(')
            print('Chances Left: ',n_o_t-1)
        n_o_t -=1
    if n_o_t == 0:
        print('--NO ATTEMPTS LEFT--')
    d = input('Did Yoy Enjoyed ? ')
    if d[0]=='y' or d[0] == 'Y':
        print('THANKS ')
    else:
        print('We will try to make it more efficient.')

if l=='h' or l=='H':
    n_o_t = 3
    n = random.randint(1,25)
    while(n_o_t !=0):
        t= int(input("Guess The Number between 1 and 25 :  "))
        if t==n:
            print('***YOU WON!!***')
            break
        elif t< n:
            print('TOO LOW :( ')
            print('Chances Left: ',n_o_t-1)
        else :
            print('TOO HIGH :( ')
            print('Chances Left: ',n_o_t-1)
        n_o_t -=1
    if n_o_t == 0:
        print('--NO ATTEMPTS LEFT--')
    d = input('Did Yoy Enjoyed ? ')
    if d[0]=='y' or d[0] == 'Y':
        print('THANKS ')
    else:
        print('We will try to make it more efficient.')
