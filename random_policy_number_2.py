
# coding: utf-8

# In[10]:


import numpy as np
from random import randint
reward_array = np.array([])
exp_reward_array = np.array([])
exp_exp_reward_array = np.array([])

for z in range(0,10,1):
    for y in range(0,5000,1):
        for x in range(0, 5, 1):
            x1=randint(0, 9)
            x2=randint(0, 9)
            x3=randint(0, 9)
            x4=randint(0, 9)
            x5=randint(0, 9)
            reward = (1*x5)+(10*x4)+(100*x3)+(1000*x2)+(10000*x1)
            #print(reward)
            reward_array = np.append(reward_array, reward)
            #print(reward_array)
        exp_reward = np.mean(reward_array)
        #print(exp_reward)
        exp_reward_array = np.append(exp_reward_array,exp_reward)
    exp_exp_reward = np.mean(exp_reward_array)
    exp_exp_reward_array = np.append(exp_exp_reward_array,exp_exp_reward)
expected_reward = np.mean(exp_exp_reward_array)
print("Total expected reward at the end of the simulation")
print("when policy-2 is applied is:")
print(expected_reward)

