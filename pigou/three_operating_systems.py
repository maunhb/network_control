import numpy as np 
import random
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt 
import matplotlib
from pigou_game import Pigou_3_os

## Choose degree of polynomial edge
game = Pigou_3_os(degree=1)

num_d = 11
demand = np.linspace(0,1,num_d)
sc_vector = np.zeros((num_d,num_d))
c1_vector = np.zeros((num_d,num_d))
c2_vector = np.zeros((num_d,num_d))
c3_vector = np.zeros((num_d,num_d)) 

for d in range(len(demand)):
    for dd in range(len(demand)):
        d1 = demand[d]
        d2 = demand[dd]
        if d1 + d2 > 1:
            break 
        d3 = 1 - d1 -d2
        x1_space = np.linspace(0,d1, int(round(1000*d1) + 1)) 
        x2_space = np.linspace(0,d2, int(round(1000*d2) +1)) 
        x3_space = np.linspace(0,d3, int(round(1000*d3) +1)) 
        old_x1 = d1
        old_x2 = d2
        old_x3 = d3 
        old_cost1 = 500
        old_cost2 = 500
        old_cost3 = 500
        for num_round in range(200):
            min_cost_1 =1000
            min_cost_2 = 1000 
            min_cost_3 = 1000 
            ## Operating system 1 best reponds
            for i in range(len(x1_space)):
                    sc = game.social_cost_1(x1_space[i],old_x2,old_x3,d1)
                    if sc < min_cost_1:
                        min_cost_1 = sc
                        best_x1 = x1_space[i]
            ## Operating system 2 best reponds
            for i in range(len(x2_space)):
                    sc = game.social_cost_2(old_x1,x2_space[i],old_x3,d2)
                    if sc < min_cost_2:
                        min_cost_2 = sc
                        best_x2 = x2_space[i]
            ## Operating system 3 best reponds
            for i in range(len(x3_space)):
                    sc = game.social_cost_3(old_x1,old_x2,x3_space[i],d3)
                    if sc < min_cost_3:
                        min_cost_3 = sc
                        best_x3 = x3_space[i]
            old_x1 = best_x1 
            old_x2 = best_x2 
            old_x3 = best_x3 
            if old_cost1 == min_cost_1 and old_cost2 == min_cost_2 and old_cost3 == min_cost_3:
                print("p1", d1, "p2", d2, "total cost", game.social_cost(old_x1,old_x2,old_x3)) 
                sc_vector[d][dd] = game.social_cost(old_x1,old_x2,old_x3) 
                c1_vector[d][dd] = game.social_cost_1(old_x1,old_x2,old_x3,d1) 
                c2_vector[d][dd] = game.social_cost_2(old_x1,old_x2,old_x3,d2) 
                c3_vector[d][dd] = game.social_cost_3(old_x1,old_x2,old_x3,d3) 
                break 
            elif num_round > 101 and old_cost1-min_cost_1<0.05 and old_cost1-min_cost_1>-0.05 and old_cost2-min_cost_2<0.05 and old_cost2-min_cost_2>-0.05  and old_cost3-min_cost_3<0.05 and old_cost3-min_cost_3>-0.05:
                sc_vector[d][dd] = (game.social_cost(old_x1,old_x2,old_x3) + min_cost_1+ min_cost_2 + min_cost_3)/2 
                c1_vector[d][dd] = (game.social_cost_1(old_x1,old_x2,old_x3,d1) + min_cost_1)/2
                c2_vector[d][dd] = (game.social_cost_2(old_x1,old_x2,old_x3,d2) + min_cost_2)/2 
                c3_vector[d][dd] = (game.social_cost_3(old_x1,old_x2,old_x3,d3)  + min_cost_3)/2
                print("p1", d1, "p2", d2, "total cost", sc_vector[d][dd], num_round) 
                break 
            else:
                old_cost1 = min_cost_1 
                old_cost2 = min_cost_2 
                old_cost3 = min_cost_3 


fig, ax = plt.subplots(ncols=1)
divnorm = matplotlib.colors.TwoSlopeNorm(vmin=0.0, vcenter=0.7, vmax=0.815)
im = ax.imshow(sc_vector,norm=divnorm, cmap="Reds") 
ax.set_title("Social Cost")
ax.set_xlabel("$d_r$") 
ax.set_ylabel("$d_s$")
xy = np.linspace(0,num_d-1,round(num_d/2))
xy_label = np.linspace(0,1,round(num_d/2))
ax.set_xticks(xy) 
ax.set_xticklabels(xy_label)
ax.set_yticks([0,2,4,6,8,10]) 
ax.set_yticklabels([0,0.2,0.4,0.6,0.8,1.0])
cbar = fig.colorbar(im)
cbar.minorticks_on()
fig.savefig("3os_pigou_sc.png")
fig, (ax1, ax2, ax3) = plt.subplots(figsize=(13, 3), ncols=3, constrained_layout=True)
im = ax1.imshow(c1_vector, cmap="Blues") 
ax1.set_title("$C_r$") 
ax1.set_xlabel("$d_r$") 
ax1.set_xticks([0,2,4,6,8,10]) 
ax1.set_xticklabels([0,0.2,0.4,0.6,0.8,1.0])
ax1.set_yticks([0,2,4,6,8,10]) 
ax1.set_yticklabels([0,0.2,0.4,0.6,0.8,1.0])
ax1.set_ylabel("$d_s$") 

im = ax2.imshow(c2_vector, cmap="Blues") 
ax2.set_title("$C_s$") 
ax2.set_xlabel("$d_r$") 
ax2.set_ylabel("$d_s$") 
ax2.set_xticks([0,2,4,6,8,10]) 
ax2.set_xticklabels([0,0.2,0.4,0.6,0.8,1.0])
ax2.set_yticks([0,2,4,6,8,10]) 
ax2.set_yticklabels([0,0.2,0.4,0.6,0.8,1.0])

im = ax3.imshow(c3_vector, cmap="Blues") 
ax3.set_title("$C_t$")
ax3.set_xlabel("$d_r$") 
ax3.set_ylabel("$d_s$") 
ax3.set_xticks([0,2,4,6,8,10]) 
ax3.set_xticklabels([0,0.2,0.4,0.6,0.8,1.0])
ax3.set_yticks([0,2,4,6,8,10]) 
ax3.set_yticklabels([0,0.2,0.4,0.6,0.8,1.0])
cbar = fig.colorbar(im, ax=ax3)
cbar.minorticks_on()


plt.show()
