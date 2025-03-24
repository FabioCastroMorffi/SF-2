'''def storedic():
    n = ''
    d = {}
    n = input()
    keys_set = set()
    while n != 'stop':
        inp = n.split()
        if inp[1] in keys_set:
            a = d[inp[0]]
            a[inp[1]].append(inp[2])
        
        else:
            d[inp[0]] = {inp[1]: [inp[2]]}
        keys_set.add(inp[1])
        n = input()
    print(d)
    return d
storedic()    
'''

'''
Every evening villagers in a small village gather around a big
fire and sing songs.

A prominent memeber of the community is the bard. Every evening,
if the bard is present, he sings a brand new song that no villager
has heard before, and no other song is sung that night. In the event that the bard
is not present, other villagers sing without him and exchange all songs that they know. (
NOTE: villagers can only learn a new song from the bard)

Given the list of villagers present for E consecutive evenings, output
all villagers that know all songs sung during that period.

Input SPECS:
--> first line is an integer N, number of villagers
--> second line is an integer E, number of evenings
--> next E lines contain the list of villagers present on each of the
    E evenings. Each line begins with a positive integer K, the
    number of villagers present that evening, followed by K 
    positive integers separated by spaces representing the villagers.

    No villager will appear twice in one night and the bard will
    appear at least once across all nights.

    Villager number 1 is the bard.

Sample Input-1:
4
3
2 1 2
3 2 3 4
3 4 2 1

Sample Output-1:
1
2
4

Sample Input-2:
8
5
4 1 3 5 4
2 5 6
3 6 7 8
2 6 2
4 2 6 8 1

Sample Output-2:
1
2
6
8

Sample Input-3:
5
3
2 1 3
2 2 1
4 2 1 4 5

Output:
1
'''
songs = 0
nmb_villagers = int(input())
nmb_evenings = int(input())
lst = [set() for _ in range(nmb_villagers-1)]
for i in range(nmb_evenings):
    row_info = input().split()
    row_info.pop(0) #removing num villagers
    if '1' in row_info: #if 1 in there everybody(each set) learns a new song(add the number of the song, eve, to their sets)
        songs += 1
        for vill in row_info:
            if vill != '1':
                lst[int(vill)-2].add(songs)
                
    else: # we iteratively union sets so that everyone shares their songs, updating final set and then replacing each numbers set with final set
        
        f_set = set()
        for vill in row_info:
            f_set.update(lst[int(vill)-2])
            #print(f_set)
        for vill in row_info:
            lst[int(vill)-2].update(f_set)
            #print(lst[int(vill)-2])


s = set()
for i in range(songs):
    s.add(i+1) #winning set
#print(f"s = {s}")
#checking for winning sets
for i in range(len(lst)):
    #print(lst[i])
    if lst[i] == s:
        print(i+2)
print(1)
        

    


     
    






