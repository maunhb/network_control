import numpy as np 
import random
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt 
from pigou_game import Pigou_2_os

## Choose degree of polynomial edge
game = Pigou_2_os(degree=1)

num_d = 21
demand = np.linspace(0,1,num_d)
sc_vector = np.ones(num_d) 
c_vector = np.zeros((num_d,2))  
x_vector  = np.zeros(num_d) 

for d in range(len(demand)):
    d1 = demand[d]
    d2 = 1 - d1 
    x1_space = np.linspace(0,d1, int(round(1000*d1) + 1)) 
    x2_space = np.linspace(0,d2, int(round(1000*d2) +1)) 
    old_x1 = d1
    old_x2 = d2
    old_cost1 = 500
    old_cost2 = 500
    for num_round in range(200):
        min_cost_1 =1000
        min_cost_2 = 1000 
        ## Operating system 1 best reponds
        for i in range(len(x1_space)):
                sc = game.social_cost_1(x1_space[i],old_x2,d1)
                if sc < min_cost_1:
                    min_cost_1 = sc
                    best_x1 = x1_space[i]
        ## Operating system 2 best reponds
        for i in range(len(x2_space)):
                sc = game.social_cost_2(old_x1,x2_space[i],d2)
                if sc < min_cost_2:
                    min_cost_2 = sc
                    best_x2 = x2_space[i]
        old_x1 = best_x1 
        old_x2 = best_x2 
        if old_cost1 == min_cost_1 and old_cost2 == min_cost_2:
            print("demand 1", d1, "demand 2", d2, "total cost", game.social_cost(old_x1,old_x2))
            sc_vector[d] = game.social_cost(old_x1,old_x2) 
            c_vector[d][0] = game.social_cost_1(old_x1,old_x2,demand[d]) 
            c_vector[d][1] = game.social_cost_2(old_x1,old_x2,1-demand[d]) 
            x_vector[d] = old_x1
            break 
        else:
            old_cost1 = min_cost_1 
            old_cost2 = min_cost_2 



plt.figure()
plt.scatter(demand, sc_vector, color="black", marker="x", label="NE") 
optimal = 1/(np.power(game.degree+1, 1./game.degree))
case_1 = game.social_cost(demand, optimal*(1-demand))
plt.plot(demand, case_1, '--', color="red", label="Case 1")
number = 1/(np.power(game.degree*(2**(game.degree-1))+(2**game.degree),(1./game.degree)))
case_2 = game.social_cost(np.ones(num_d)*number, np.ones(num_d)*number)
plt.plot(demand, case_2, color="blue", label="Case 2") 
case_3 = game.social_cost(optimal*demand,1-demand)
plt.plot(demand, case_3, '-.', color="green", label="Case 3")
plt.xlabel("$d_r$")
plt.ylabel("Social cost")
plt.title("degree = {}".format(game.degree)) 
plt.legend()

opt = game.social_cost(optimal,0) 
plt.figure()
plt.plot(demand, sc_vector/opt)
plt.xlabel("$d_r$")
plt.ylabel("Price of Anarchy")
plt.title("degree = {}".format(game.degree)) 


plt.show()
