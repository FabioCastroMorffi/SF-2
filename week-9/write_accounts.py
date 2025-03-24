output_file = open('accounts.txt','w')
def accounts(n):
    for i in range(n):
        line = input()
        output_file.write(line+'\n')
    output_file.close()
accounts(5)

'''
From accounts.txt, read line and create a dict of dicts. The outer Dict key is the account num
. The inner dict key is the last name and the val (of inner dict)
is the acount balance. Print dict

d = {key: {key2: ...}}
'''