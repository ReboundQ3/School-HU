cube = lambda x: x * x * x

def fibonacci(n):
    i = 1
    number = [0, 1]
    if n == 0:
        number = []
    elif n == 1:
        number = [0]
    elif n >= 3:
        while len(number) != n:
            number.append(i)
            i = number[-1] + number [-2]
    return number

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))