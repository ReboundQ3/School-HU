events = '9/13 2:30 PM\n9/14 11:15 AM\n9/14 1:00 PM\n9/15 9:00 AM'
eventList = events.split("\n")
length = 0
counter = 0
for event in eventList:
    length += len(event)
    if str(event[0:4]) == '9/14':
        counter += 1
        index1 = length
    length += len(event)


print (counter)
print (index1)


print(events[62:])