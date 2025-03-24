output_file = open('accounts.txt','r')
def accounts(n):
    for i in range(n):
        line = input()
        output_file.write(line+'\n')
    output_file.close()
#accounts(5)

'''
From accounts.txt, read line and create a dict of dicts. The outer 
Dict key is the account num
. The inner dict key is the last name and the val (of inner dict)
is the acount balance. Print dict

d = {key: {key2: ...}}
'''
def dictAccount():
    d = {}
    for line in output_file:
        acc_num, name, money = line.split()
        d[acc_num] = d.get(acc_num, {name: int(money)})
    print(d)
dictAccount()

