from random import choice
rules = {'rock':'paper','scissors':'rock','paper':'scissors'}
previous = ['rock','paper','scissors']

while True:
    human = input('\n choose your weapon:')
    computer = rules[choice(previous)]
    
    if human in ('quit','exit'): break
    elif human in rules:
        previous.append(human)
        print('the computer played',computer,end=';')
        
        if rules[computer] == human:
            print('yaa you win!')
        elif rules[human] == computer:
            print('the computer beat you...:(')
        else: print("its a tie")
    else: print("that's not a vali choice")