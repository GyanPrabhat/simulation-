
# coding: utf-8

# In[4]:


import numpy as np
import random
from random import randint
from random import choice
import math
aor = np.array([])
#####################
x1=randint(0, 9)
x2=randint(0, 9)
x3=randint(0, 9)
x4=randint(0, 9)
x5=randint(0, 9)
digits = np.array([x1,x2,x3,x4,x5])
print("The sequence of randomly generated digits are:",x1,x2,x3,x4,x5)
print("First spin:",x1)
print("Second spin:",x2)
print("Third spin:",x3)
print("Fourth spin",x4)
print("Fifth spin:",x5)
# A Python program to print all 
# permutations using library function
from itertools import permutations
# Get all permutations of 0,1,2,3,4
perm = list(permutations([4,3,2,1,0]))
c1 = random.choice(perm)
p1 = c1[0]
p2 = c1[1]
p3 = c1[2]
p4 = c1[3]
p5 = c1[4]
print("Number the place values of the 5-digit number starting from left as 4,3,2,1,0")
print("The random selection of place values is:")
print("Digit of first spin goes to place:",p1)
print("Digit of second spin goes to place:",p2)
print("Digit of third spin goes to place:",p3)
print("Digit of fourth spin goes to place:",p4)
print("Digit of fifth spin goes to place:",p5)
r1 = int(math.pow(10,p1))
r2 = int(math.pow(10,p2))
r3 = int(math.pow(10,p3))
r4 = int(math.pow(10,p4))
r5 = int(math.pow(10,p5))
#print(r1,r2,r3,r4,r5)
r_arr = np.array([r1,r2,r3,r4,r5])
print("The reward array for this random choice will be:",r_arr)
re = r_arr * digits
reward = re[0] + re[1] + re[2] + re[3] +re[4]
aor = np.append(reward,aor)
exp_reward = np.mean(aor)
print(exp_reward)

