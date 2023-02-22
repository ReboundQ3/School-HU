# Enter your code here. Read input from STDIN. Print output to STDOUT
def findNumber (name):
    result = phonebook.get(name, 0)
    if result == 0:
        return 'Not found'
    else:
        return name + '=' + phonebook[name]
    

phonebookSize = int(input())
phonebook = {}
i = 0

while i < phonebookSize:
    entry = input().split(" ")
    phonebook[entry[0]] = entry[1]
    
    i += 1

i = 0
while i < phonebookSize:
    name = input()
    print(findNumber(name))
    
    i += 1
