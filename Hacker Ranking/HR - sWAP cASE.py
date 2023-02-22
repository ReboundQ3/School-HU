def swap_case(s):
    b = ''
    for letter in s:
        if letter.isupper():
            b += letter.lower()
        else:
            b += letter.upper()
            
    return b

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)