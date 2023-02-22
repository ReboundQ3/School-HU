def mutate_string(string, position, character):
    result = ''
    i = 0
    for letter in string:
        if i == position:
            result += character
        else:
            result += string[i]
        i += 1
    return result

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)