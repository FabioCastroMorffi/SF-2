n, m, d = input().split()
laundry = 0 
dirty_shirt = 0
events = input().split()
print(events)

for event in events:
    events[event] = int(events[event])

for i in range(int(d)):
    if dirty_shirt == n:
        laundry += 1
        dirty_shirt = 0
    for j in events:
        if j == i+1:
            n+=1
    dirty_shirt +=1
print(laundry)



