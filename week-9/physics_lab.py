import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("clean_data_multiple_filter.csv")

real_time = df["Time (s) Run #4"]  
real_position = df["Position (m) Run #4"]
initial_position = real_position.dropna().iloc[0] 

mass = 0.0068 #(with 8 coffee filters)
area = 0.019
air_density = 1.2
drag_coeff = 0.97
def newAcc(v):
    return -9.8 + ((drag_coeff*air_density*area*v**2)/ 2*mass)

initial_velocity, final_velocity = 0, 0
delta_t = -0.02

lst_final_velocity = []
lst_time = []
lst_position = []


while initial_position>0:
    acc = newAcc(initial_velocity)

    final_velocity = initial_velocity + acc*0.02
    final_position = initial_position + initial_velocity*0.02 + 0.5*acc*0.02**2 


    initial_velocity, initial_position = final_velocity, final_position
    delta_t+=0.02
    lst_final_velocity.append(final_velocity)
    lst_time.append(delta_t)
    lst_position.append(final_position)


plt.figure(figsize=(10, 6))
plt.plot(lst_time, lst_position, label="Simulated Drop", linestyle='solid', color='b')
plt.scatter(real_time, real_position, label="Real-Life Drop", linestyle='solid', color='r')

plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Simulated vs Real-Life Coffee Filter Drop (8 Filters)")
plt.legend()
plt.grid()
plt.show()