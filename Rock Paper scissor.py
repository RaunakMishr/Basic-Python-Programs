print("________Welcome To The Game________")
print("About :- ")
print('''The object of the rock-paper-scissor python project is to build a game for a single player that plays with a computer, 
anywhere, and anytime. This project is base on the rules that: rock blunts scissors so rock wins.
scissors cut the paper so scissors win.''')
import random
cc = random.choice(['rock','scissor','stone'])
uc = input('Enter your choice: ').lower()
print("computer's Choice: ",cc)
if uc == 'rock' and cc=='scicssor' or uc == 'paper' and cc == 'rock' or uc =='scissor' and cc=='paper':
    print('***YOU WON !!***')
else:
    print('Computer Won')