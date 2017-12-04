
# coding: utf-8

# In[1]:

import numpy as np
import sympy
from sympy import *


# In[7]:

#The problem for this exercise is given in the link below:

#http://www.mathstat.dal.ca/~handrew/teaching/math2030/assignments/a5.pdf

#This problem askes us to determine the values for the flow(current) of water f1-f5. I would treat this like an 
#electrical circuit and come up with equations to turn this into a matrix operation.

#f1+f2 = 100
#f4+f5 = 150
#f2+f3-f4 = 150
#-f1+f3+f5 = 200

# I then plug the equation's coefficients into the matrix below. The columns represent f1-f5.

B = sympy.Matrix([[1,1,0,0,0,100],
                  [0,0,0,1,1,150],
                  [0,1,1,-1,0,150],
                  [-1,0,1,0,1,200]
                  ])


# In[8]:

#sympy has a function to turn the matrix into reduced row echelon form
B.rref()



# In[ ]:

#This matrix has infinitely many solutions, and the vector form of the solutions can be represented as such:

#f1 = s + t − 200
#f2 = −s − t + 300
#f3 = s
#f4 = −t + 150
#f5 = t

