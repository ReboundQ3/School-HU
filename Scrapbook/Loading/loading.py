a = 0
b = 30
max = b
direction = 'up'
i = 0

while i != -1:
    i = 0
    while i < a:
        print (" ",end="")
        i += 1
    
    print("*****",end="")
    
    i = 0
    while i < b:
        print (" ",end="")
        i += 1
    
    if direction == 'up':
        a += 1
        b -= 1
    elif direction == 'down':
        a -= 1
        b += 1

    if a == max:
        direction = 'down'
    elif b == max:
        direction = 'up'
    print ("")