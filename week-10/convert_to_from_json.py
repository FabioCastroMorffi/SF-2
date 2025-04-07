import json

#convert from JSON to PYTHON
student_record = '{"name": "Lucy", "year": 1, "college": "Dawson" }' #some JSON
parsed_record = json.loads(student_record)

print(parsed_record)

#convert from PYTHON to JSON

student_dict = {'name': 'Lucy', 'year': 1, 'college': 'Dawson'}
student_record_json = json.dumps(student_dict)

#print(student_record_json)

print(json.dumps({'name': 'Lucy' , 'year': 1})) #dict -> json obj
print(json.dumps(['name','year']))# list -> array
print(json.dumps(('apple', ['hello'])))# tuple -> array
#float -> number
# int -> number 
# boolean -> lower case boolean
# None -> null







