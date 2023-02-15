def collatz(input):
    input = int(input)
    if input % 2 == 0:
        output =  input // 2
    if input % 2 == 1:
        output = 3 * input + 1
    return output
    
number = input('Geef een nummer op: ')
while number != 1:
    number = collatz(number)
    print (number)

print('')
print('Done!')