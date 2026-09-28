import numpy as np
import scipy
import matplotlib.pyplot as plt
from scipy.differentiate import jacobian


#initialization
dt=1
X=np.array([1,2,4,4])
F=np.array([[1,0,dt,0],[1,0,0,dt],[0,0,1,0],[0,0,0,1]])
P=np.eye(4)*.01
Q=np.eye(4)*5
R=1
A=F

#functions for prediction and updation of state and measurement


#def h(x):

#    msr=np.arctan2(x[1],x[0])

#   return msr


def jaco(x):
    
    de=x[0]**2+x[1]**2
    p1=-(x[1]/de)
    p2= x[0]/de

    return np.array([p1,p2,0,0])
    


def predict(x,p,q):

    x_pred= X@A+(np.random.multivariate_normal(np.zeros(4).T,Q))
    #print('xpred',x_pred)
    p_pred= A@p@A.T +q
    #print('ppred',p_pred)

    measure_pred=np.arctan2(x[1],x[0])+np.random.normal(0,R)
    #print('meaure_pred',measure_pred)
    

    return x_pred,p_pred, measure_pred


def update(x_pred,p_pred,r,measure):
    H=jaco(x_pred)
    #print('jaco',H)
    r=R
    #print('r',r)
    z= np.arctan2(x_pred[1],x_pred[0])+np.random.normal(0,.01) #sensor data
    #print('z',z)
    y=z-measure
    #print('z',y)
    s= H@p_pred@H.T+r
    #print('s',s)
    k= (p_pred @ H.T)/s
    #print('k',k)

    x_update=x_pred+k*y
    p_update= (np.eye(len(x_pred))-(k@H))*p_pred
    
    
    return x_update,p_update


pos1=[]
pos2=[]
x_in=X
p_in=P
q_in=Q
time=[]

for t in range(100):


    x_pr,p_pr,m_p= predict(x_in,p_in,q_in)

    x_u,p_u= update(x_pr,p_pr,R,m_p)

    x_in,p_in=x_pr,p_pr

    pos1.append(x_u[0])
    pos2.append(x_u[1])

    #print(x_u)

    time.append(t)





plt.scatter(pos1,pos2)

plt.show()

    

    

#plotting elements of state   

    
    

    

    
