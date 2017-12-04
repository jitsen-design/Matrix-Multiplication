
# coding: utf-8

# In[6]:

import numpy as np


# In[19]:

#This exercise is drawn directly from a tutorial in the link given below. 

#http://courses.ncssm.edu/math/TCMConf/TCM2004/TCMTalks/MatrixApps.pdf

#The problem is explained thus:

#"In the 60's the American car market was dominated by US made car. The Japanese auto makers, Toyota, Nissan, and 
#Honda were just beginning to make inroads to the American market while the European makers and other countries 
#had a small steady share. Still, most people who owned American, replaced their car with another US made car, 
#while the majority of Japanese car owners replaced their car with another Japanese make. The matrix to the left 
#below represents a possible survey of 500 car owners and their preferences. For example, of 300 US car owners, 
#240 or 80% planned to replace their car with another US made car, while 45 owners (or 15%) planned to switch to 
#a Japanese car.

#US   Jap Eur Other Total US Jap Eur Other Total
#US   240  45  12  3 300 0.8 0.15 0.04 0.01 1.00
#Jap   20  65  10  5 100 0.2 0.65 0.1  0.05 1.00
#Eur    8   8  60  4  80 0.1 0.1  0.75 0.05 1.00
#Other  4   4   2 10  20 0.2 0.2  0.1  0.5  1.00

#Suppose that the proportion of cars sold in the US in the mid 60's followed the proportions in the survey. An 
#initial matrix for these proportions would be:

#        US  Jap Eur Other
#Prop [ .60 .20 .16 .04 ]

#Suppose a transition can be said to occur every 5 years. Over the course of 20 years (4 transitions), what will 
#happen to the proportion of cars if we use the transition matrix that we computed above?"

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#First, I tranpose the probability matrix for ease of multiplication

A = np.array([[0.80,0.20,0.10,0.20],
              [0.15,0.65,0.10,0.20],
              [0.04,0.10,0.75,0.10],
              [0.01,0.05,0.05,0.50]])

#I then create a vector of initial probabilities for the likelihood of purchasing a car in the mid '60s

x = [.6,
     .2,
     .16,
     .04,]

#I will also need an output vector for the second round of probabilities. I create an output vector of zeros

y = [0,
     0,
     0,
     0]


# In[20]:

#The second time someone decides to buy a vehicle, the probabilities are calculated using a basic Matrix-vector 
#multiplication. I have written out the code to illustrate how the matrix-vector operations are carried out.

def matrix_mult(A, x, y):
    (m_A,n_A) = np.shape(A)
    for i in range(0,m_A):
        for j in range(0,n_A):
            y[i] = A[i,j]*x[j] + y[i]
    return(y)

matrix_mult(A, x, y)

#The output vector carries the following probabilities of purchasing a car by region the second time round:

print("Probability of Purchasing a US made vehicle:",y[0])
print("Probability of Purchasing a Japanese vehicle:",y[1])
print("Probability of Purchasing a European vehicle:",y[2])
print("Probability of Purchasing a vehicle made in another region:",y[3])

#I would also like to check if the calculation is correct, by ensuring that the output probabilities sum to 1.

print("Sum of Probabilities:",sum(y))  


# In[21]:

#However, we will have to put in values for y manually, each time we want to compute the next round of purchases. 
#therefore, we can use the existing functions in NumPy to compute the probability distribution after the fourth 
#round of purchases.

x1 = np.dot(A,x) 

for i in range(0,4):
    x1 = np.dot(A,x1)

print("Probability of Purchasing a US made vehicle:",x1[0])
print("Probability of Purchasing a Japanese vehicle:",x1[1])
print("Probability of Purchasing a European vehicle:",x1[2])
print("Probability of Purchasing a vehicle made in another region:",x1[3])


#Once again, I check to see if the calculation is correct, by ensuring that the output probabilities sum to 1.

print("Sum of Probabilities:",sum(x1))  


# In[ ]:



