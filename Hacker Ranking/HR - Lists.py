if __name__ == '__main__':
    N = int(input())
    
i = 0
list = []


while i < N:
    command = input().split(" ")
    
    if command[0] == 'insert':
        arg1 = int(command[1])
        arg2 = int(command[2])
        list.insert(arg1, arg2)
    elif command[0] == 'print':
        print(list)
    elif command[0] == 'remove':
        arg1 = int(command[1])
        list.remove(arg1)
    elif command[0] == 'append':
        arg1 = int(command[1])
        list.append(arg1)
    elif command[0] == 'sort':
        list.sort()
    elif command[0] == 'pop':
        list.pop()
    else:
        list.reverse()

    i += 1
    