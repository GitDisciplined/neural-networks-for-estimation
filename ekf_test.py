import numpy as np
import scipy
import matplotlib.pyplot as plt


#initialization

X=
F=
P=
H=
Q=
R=
A=

#functions for prediction and updation of state and measurement

def predict(x,p,q):

    x_pred= X*A+np.ranodm.normal(np.zeros(4),Q)
    p_pred= A@p@A.T +q

    measure_pred= np.arctan(x_pred[1],x_pred[0])
    

    return x_pred,p_pred, measure_pred


def update(x_pred,p_pred,r,measure):

    z= np.arctan(x_pred[1],x_pred[0])+np.random(0,.01) #sensor data
    y=z-measure
    s= (h@p_pred)@h.T+r
    k= (p_pred @ h.T)@ np.linalg.inv(s)

    x_update=x_pred+k*y
    p_update= (np.eye(len(x_pred))-(k@h))*p_pred
    
    
    return x_update,p_update


state=[]
x_in=X

#estimation of states in discrete time steps

for t in range(100):

    
    x_pr,p_pr,m_p= predict(x_in,p_in)

    x_u,p_u= update(x_pr,p_pr,m_p)

    x_in,p_in=x_pr,p_pr

    

    state.append(x_u)

    

#plotting elements of state   

    
    

    

    
