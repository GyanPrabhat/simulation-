
# coding: utf-8

# In[94]:


#Start the simulation
#import the packages
import numpy as np
from random import randint
reward_array = np.array([])
exp_reward_array = np.array([])
for q in range(0,9000,1):
    for w in range(0, 5, 1):
        ################################
        #Define the inital number (Say it is the inital state of the system)
        num = np.array([-1,-1,-1,-1,-1])
        #print("Number before start of the game =" , num)
        x1 = num[0]
        x2 = num[1]
        x3 = num[2]
        x4 = num[3]
        x5 = num[4]
        ###########################################
        #Make the first draw
        y1=randint(0, 9)
        #print("Result of spin-1 =",y1)
        #For spin-1 decide where to put the digit
        #######################
        if y1== 0:
            x5 = y1
        if y1== 1:
            x5 = y1
        if y1== 2:
            x5 = y1
        if y1== 3:
            x4 = y1
        if y1== 4:
            x3 = y1
        if y1== 5:
            x3 = y1
        if y1== 6:
            x2 = y1
        if y1== 7:
            x1 = y1
        if y1== 8:
            x1 = y1
        if y1== 9:
            x1 = y1
        ######################################
        #number after first spin
        num_1 = np.array([x1,x2,x3,x4,x5])
        #print("Number after the first spin is:",num_1)
        a1 = num_1[0]
        a2 = num_1[1]
        a3 = num_1[2]
        a4 = num_1[3]
        a5 = num_1[4]
        ######################################
        if x1 >= 0 :
            reward_s1 = 10000*x1
        if x2 >= 0:
            reward_s1 = 1000*x2
        if x3 >= 0:
            reward_s1 = 100*x3
        if x4 >= 0:
            reward_s1 = 10*x4
        if x5 >= 0:
            reward_s1 = 1*x5
        #print("Reward after spin-1 is:",reward_s1)
        #####################################
        #Upadte the place values of num after spin-1
        #For spin-1
        if a1 >= 0 :
            dum_1 = np.array([a2,a3,a4,a5])
            r_a1 = np.array([1000,100,10,1])
            #print("reward multiplication array is:",r_a1)
        ##################
        if a2 >= 0 :
            dum_1 = np.array([a1,a3,a4,a5])
            r_a1 = np.array([10000,100,10,1])
            #print("reward multiplication array is:",r_a1)
        ####################
        if a3 >= 0 :
            dum_1 = np.array([a1,a2,a4,a5])
            r_a1 = np.array([10000,1000,10,1])
            #print("reward multiplication array is:",r_a1)
        #####################
        if a4 >= 0 :
            dum_1 = np.array([a1,a2,a3,a5])
            r_a1 = np.array([10000,1000,100,1])
            #print("reward multiplication array is:",r_a1)
        ######################
        if a5 >= 0 :
            dum_1 = np.array([a1,a2,a3,a4])
            r_a1 = np.array([10000,1000,100,10])
           # print("reward multiplication array is:",r_a1)
        ################
        #print("Dummy number after the first reward to adjust the place values is:",dum_1)
        m1 = dum_1[0]
        m2 = dum_1[1]
        m3 = dum_1[2]
        m4 = dum_1[3]
        #Make the second draw
        ###########################
        y2=randint(0, 9)
        #print("Result of spin-2 =",y2)
        ###########################
        #place the digit got in spin-2 in blank places
        if y2== 0:
            m4 = y2
        if y2== 1:
            m4 = y2
        if y2== 2:
            m4 = y2
        if y2== 3:
            m3 = y2
        if y2== 4:
            m3 = y2
        if y2== 5:
            m2 = y2
        if y2== 6:
            m2 = y2
        if y2== 7:
            m1 = y2
        if y2== 8:
            m1 = y2
        if y2== 9:
            m1 = y2
        #######################
        #Get the updated number after spin-2
        num_2 = np.array([m1,m2,m3,m4])
        #print("num_2 is =", num_2)
        b1 = num_2[0]
        b2 = num_2[1]
        b3 = num_2[2]
        b4 = num_2[3]
        #b5 = num_2[4]
        ######################################
        #print("Notice the reward array was:",r_a1)
        reward_s2 = r_a1 * num_2
        #print("Reward for the second draw is",reward_s2)
        #print("reward array to choose form",reward_s2)
        #####################################
        for i in reward_s2:
            if i >= 0 :
                rs2 = i
                #print("reward for the second draw is = ",rs2)
        ##################################################
        #Upadted reward sequence is
        alpha = np.extract(reward_s2 < 0, reward_s2)
        r_a2 = alpha * -1
        #print("Upadted reward sequence is:",r_a2)
        #Upadte the place values of num after spin-2
        #For spin-2
        #########################
        if b1 >= 0  :
            dum_2 = np.array([b2,b3,b4])
        ##################
        if b2 >= 0  :
            dum_2 = np.array([b1,b3,b4])
        ####################
        if b3 >= 0:
            dum_2 = np.array([b1,b2,b4])
            r_a3 = np.array([10000,1000,1])
        #####################
        if b4 >= 0  :
            dum_2 = np.array([b1,b2,b3])
            r_a3 = np.array([10000,1000,10])
        #####################
        #print(dum_2)
        n1 = dum_2[0]
        n2 = dum_2[1]
        n3 = dum_2[2]
        #make the third draw
        y3=randint(0, 9)
        #print("Result of spin-3 is:",y3)
        ###########################
        ###########################
        #place the digit got in spin-3 in blank places
        if y3== 0:
            n3 = y3
        if y3== 1:
            n3 = y3
        if y3== 2:
            n3 = y3
        if y3== 3:
            n3 = y3
        if y3== 4:
            n2 = y3
        if y3== 5:
            n2 = y3
        if y3== 6:
            n1 = y3
        if y3== 7:
            n1 = y3
        if y3== 8:
            n1 = y3
        if y3== 9:
            n1 = y3
        ###################################
        #Get the updated number after spin-3
        num_3 = np.array([n1,n2,n3])
        #print("num_3 is:",num_3)
        c1 = num_3[0]
        c2 = num_3[1]
        c3 = num_3[2]
        #c4 = num_3[3]
        #c5 = num_3[4]
        ####################################
        #print("Remember the Upadted reward sequence was:",r_a2)
        reward_s3 = r_a2 * num_3
        #print("Reward sequence to choose from is:", reward_s3)
        for j in reward_s3:
            if j >= 0 :
                rs3 = j
                #print("reward for the third draw is = ",rs3)
        ################################################
        ##################################################
        #Upadted reward sequence is
        beta = np.extract(reward_s3 < 0, reward_s3)
        r_a3 = beta * -1
        #print("Upadted reward sequence is:",r_a3)
        #########################
        if c1 >= 0  :
            dum_3 = np.array([b2,b3])
        ##################
        if c2 >= 0  :
            dum_3 = np.array([c1,c3])
        ####################
        if c3 >= 0:
            dum_3 = np.array([c1,c2])
        #####################
        #print(dum_3)
        p1 = dum_3[0]
        p2 = dum_3[1]
        y4=randint(0, 9)
        #print("Result of spin-4",y4)
        #for spin-4
        #y4=randint(0, 9)
        if y4== 0:
            p2 = y4
        if y4== 1:
            p2 = y4
        if y4== 2:
            p2 = y4
        if y4== 3:
            p2 = y4
        if y4== 4:
            p2 = y4
        if y4== 5:
            p1 = y4
        if y4== 6:
            p1 = y4
        if y4== 7:
            p1 = y4
        if y4== 8:
            p1 = y4
        if y4== 9:
            p1 = y4
        ###################################
        #Get the updated number after spin-3
        num_4 = np.array([p1,p2])
        #print("num_4 is:",num_4)
        d1 = num_4[0]
        d2 = num_4[1]
        #d3 = num_4[2]
        #c4 = num_3[3]
        #c5 = num_3[4]
        ####################################
        #print("Remember the Upadted reward sequence was:",r_a3)
        reward_s4 = r_a3 * num_4
        #print("Reward sequence to choose from is:", reward_s4)
        for k in reward_s4:
            if k >= 0 :
                rs4 = k
                #print("reward for the third draw is = ",rs4)
        ################################################
        ##################################################
        #Upadted reward sequence is
        gamma = np.extract(reward_s4 < 0, reward_s4)
        r_a4 = gamma * -1
        #print("Upadted reward sequence is:",r_a4)
        #########################
        if d1 >= 0  :
            dum_4 = np.array([d2])
        ##################
        if d2 >= 0  :
            dum_4 = np.array([d1])
        ####################
        #print(dum_4)
        q1 = dum_4[0]
        y5=randint(0, 9)
        #print("Result of spin-5 =",y5)
        q1 = y5
        num_5 = q1
        #print("num_5 is:",num_5)
        #print("Notice that the Upadted reward sequence was:",r_a4)
        reward_s5 = r_a4 * num_5
        #print("reward_s5 is",reward_s5)
        #type(reward_s5)
        #print(reward_s5.shape)
        rs5 = reward_s5[0]
        #print("Result of spins were",y1,y2,y3,y4,y5)
        Tot_r = reward_s1 + rs2 + rs3 + rs4 + reward_s5
        Tot_reward = Tot_r[0]
        print("Total expected reward at the end of the simulation is:")
        print(Tot_reward)
        reward_array = np.append(reward_array, Tot_reward)
    exp_reward = np.mean(reward_array)
    exp_reward_array = np.append(exp_reward_array,exp_reward)
#######################################################################
output = exp_reward_array
import pandas as pd 
df = pd.DataFrame(output)
df.to_csv("C:/Users/USER/Desktop/Disertation_works/ff_1.csv")

