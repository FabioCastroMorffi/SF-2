import matplotlib.pyplot as plt
import pandas as pd

#df = pd.read_csv("clean_data_multiple_filter.csv")
mass = 0.0068 #(with 8 coffee filters)
area = 1.90
air_density = 1.2
drag_coeff = 0.0097
def newAcc(v):
    return -9.8 + ((drag_coeff*air_density*area*v**2)/ 2*mass)
initial_velocity, final_velocity = 0, 0
initial_position = 1
delta_t = 0.002
#lst final_velocity = []
lst_time = []
lst_position = []
#acc = -9.8
while initial_position>0:
    acc = newAcc(initial_velocity)
    #print(acc)
    final_velocity = initial_velocity + acc*0.2
    final_position = initial_position + initial_velocity*0.002 + 0.5*acc*0.002**2 
    #print(final_position)
    initial_velocity, initial_position = final_velocity, final_position
    delta_t+=0.002
    #lst final_velocity.append final_velocity)
    lst_time.append(delta_t)
    lst_position.append(final_position)


plt.plot(lst_time, lst_position)
#plt.plot(lst_time, lst final_velocity)
plt.show()