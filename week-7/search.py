# import time 
# def search(collection, value):
#     '''
#     search for value in the collection
#     '''
#     for i in collection:
#         found = value in collection
#         print("searching")
#     return found
    


# lst = list(range(1,50000))

# s = set(range(1,50000))

# start = time.time()
# search(s, 50000)
# end = time.time()
# print(end-start)
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("clean_data_multiple_filter.csv")
m = 0.003
A = 150
p = 1.22
C = 0.5
def a_y(v):
    return -9.8 + ((C*p*A*v**2)/ 2*m)
vi = 0
vf = 0
pi = 1
t = 0.002
lst_vf = []
lst_t = []
lst_p = []
a = -9.8
while pi>0:
    a = a_y(vi)
    print(a)
    vf = vi + a*0.2
    pf = pi + vi*0.002 + 0.5*a*0.002**2 
    print(pf)
    vi = vf

    pi = pf
    t+=0.002
    lst_vf.append(vf)
    lst_t.append(t)
    lst_p.append(pf)


plt.plot(lst_t, lst_p)
#plt.plot(lst_t, lst_vf)
plt.show()
