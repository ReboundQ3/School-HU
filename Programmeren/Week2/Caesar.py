alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
def caesar(shift,text):
    length = len(alfabet)
    #print(length)
    for letter in text:
        newletter = int(alfabet.index(letter)) + shift
        if newletter >= length:
            newletter = newletter - length
        #print (newletter)
        print (alfabet[newletter],end='')

def caesarReturn(shift,text):
    length = len(alfabet)
    #print(length)
    for letter in text:
        newletter = int(alfabet.index(letter)) - shift
        if newletter >= length:
            newletter = newletter + length
        #print (newletter)
        print (alfabet[newletter],end='')


shift = 1
# text = 'hello this is a test'
# caesar(shift,text)

print()
print()
textReturn = 'ifmmpauijtajtabauftu'
caesarReturn(shift,textReturn)

