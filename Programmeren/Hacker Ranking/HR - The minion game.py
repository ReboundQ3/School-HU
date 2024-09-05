def minion_game(string):
    # your code goes here
    stuartScore = 0
    kevinScore = 0
    vowels = ['A','E','O','U','I']
    length = len(string)
    
    # Stuart loop
    i = 0
    for letter in string:
        if letter not in vowels:
            stuartScore += length - i
        i += 1
    
    # Kevin loop
    i = 0
    for letter in string:
        if letter in vowels:
            kevinScore += length - i
        i += 1
    
    # Compare scores and return
    if stuartScore < kevinScore:
        print ('Kevin ' + str(kevinScore))
    elif stuartScore > kevinScore:
        print ('Stuart ' + str(stuartScore))
    else:
        print ('Draw')
    
    
    
if __name__ == '__main__':
    s = input()
    minion_game(s)