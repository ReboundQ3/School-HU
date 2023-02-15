import random

print('(R)ock, (P)aper or (S)cisors')
choiceOne = input()


choices = ["R", "P", "S"]
choiceTwo = random.choice(choices)

print ()
print ('Your choice is ' + choiceOne)
print ('Computer choice is ' + choiceTwo)
print ()

if choiceOne == choiceTwo:
    print ('Tie!')
elif choiceOne == 'R' and choiceTwo == 'P':
    print ('Computer wins!')
elif choiceOne == 'R' and choiceTwo == 'S':
    print ('Player wins!')
elif choiceOne == 'P' and choiceTwo == 'R':
    print ('Player wins!')
elif choiceOne == 'P' and choiceTwo == 'S':
    print ('Computer wins!')
elif choiceOne == 'S' and choiceTwo == 'R':
    print ('Computer wins!')
elif choiceOne == 'S' and choiceTwo == 'P':
    print ('Player wins!')
