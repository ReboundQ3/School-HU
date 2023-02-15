def toString (input):
    length = len(input) - 1
    i = 0
    while i < length:
        if i != 0:
            print (', ', end='')
        print (input[i], end='')
        i += 1
    
    print (' and', input[i])
    


spam = ['apples', 'bananas', 'tofu', 'cats']
toString(spam)