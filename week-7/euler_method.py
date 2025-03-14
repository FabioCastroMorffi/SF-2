m = 0.003
A = 150
p = 1.22
C = 0.5
def a_y(v):
    return -9.8 + ((C*p*A*v**2)/ 2*m)
vi = 0
vf = 0
t = 0.2
lst = []
for i in range(1, 10):
    a = a_y(vi)
    vf = vi + a*t
    vi = vf
    lst.append((vf,t*i))

print(lst)
print("h")