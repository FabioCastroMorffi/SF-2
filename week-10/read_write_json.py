import json

#deserialization of JSON => conversion of JSON object to respective 
# Python object

input_file = open('students.json','r')
data = json.load(input_file)
#print(data, type(data))

for line in input_file:
    print(line)
    #print(type(line))

#serialization of JSON=> conversion PYTHON object to JSON object

output_file = open('butterflies.json', 'w')
d = {'painted': 1, 'lol':4}
json.dump(d, output_file)
output_file.close()