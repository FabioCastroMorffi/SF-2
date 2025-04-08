'''
INput specs:
--> first line has n(large)
--> next n lines(one per city) . Each line gives the name of a city, a space, state's 2 letter abbv. Note that the same city
an appear multiple lines for different states
SAMPLE INPUT:
12
SCRANTON PA
MANISTEE MI 
NASHUA NH
PARKER SC
LAFAYETTE CO


Sample output:
9

Read 5 different sample inputs, write them to a file such that there is an empty line for each sample input. Then from this file we
read the input and determine the output.
'''

output_file = open('files.txt', 'w')
n = int(input())
for i in range(n):
    city, state = input().split()
    output_file.write(city[:2] + ' ' + state+ '\n')
    if i == n-1:
        output_file.write('\n')
output_file.close()

def special_tuple():
    input_file = open('files.txt', 'r')
    d = {}
    for line in input_file:
        tupl = (line[:2], line[3:].rstrip())
        special = (tupl[1], tupl[0])
        if special in d:
            d[special] += 1
        else:
            d[tupl] = d.get(tupl,0) + 1 
    for key in d:
        if d[key] != 1:
            count += d[key]
    print(count)
    return d
print(special_tuple())
    
