
# coding: utf-8

# In[34]:


import numpy as np
import random
from random import randint
from random import choice
import math
aor = np.array([])
exp_reward_array = np.array([])
exp_exp_reward_array = np.array([])
#####################
for j in range (1,100,1):
    for i in range(1,5000,1):
        x1=randint(0, 9)
        x2=randint(0, 9)
        x3=randint(0, 9)
        x4=randint(0, 9)
        x5=randint(0, 9)
        digits = np.array([x1,x2,x3,x4,x5])
        from itertools import permutations
        perm = list(permutations([4,3,2,1,0]))
        c1 = random.choice(perm)
        p1 = c1[0]
        p2 = c1[1]
        p3 = c1[2]
        p4 = c1[3]
        p5 = c1[4]
        r1 = int(math.pow(10,p1))
        r2 = int(math.pow(10,p2))
        r3 = int(math.pow(10,p3))
        r4 = int(math.pow(10,p4))
        r5 = int(math.pow(10,p5))
        r_arr = np.array([r1,r2,r3,r4,r5])
        re = r_arr * digits
        reward = re[0] + re[1] + re[2] + re[3] +re[4]
    aor = np.append(reward,aor)
    exp_reward = np.mean(aor)
    exp_reward_array = np.append(exp_reward_array,exp_reward)
    exp_exp_reward = np.mean(exp_reward_array)
    exp_exp_reward_array = np.append(exp_exp_reward_array,exp_exp_reward)
expected_reward = np.mean(exp_exp_reward_array)
print("The long-run expected reward")
print("when random-digit choice policy is applied:")
print(expected_reward)

