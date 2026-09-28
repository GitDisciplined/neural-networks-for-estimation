import numpy as np
import scipy
import matplotlib.pyplot as plt
#from scipy.differentiate import jacobian



#data set


xo=1
yo=2
xt=10
yt=25
vt=5

T=1
count=100
hori=[xt]
verti=[yt]
an=[np.arctan2((yt-yo),(xt-xo))]
xr=[xt-xo]
yr=[yt-yo]

def param(x1,y1,x2,y2):

    #x=x2-x1
    #y=y2-y1
    #theta=np.arctan(y/x)

    x2_new=x2+(T*vt)
    y2_new=y2+(T*vt)

    theta=np.arctan2((y2_new-yo),(x2_new-xo))

    return x2_new,y2_new,theta


for i in range(count):
    

    x_tar,y_tar,angle=param(xo,yo,xt,yt)
    hori.append(x_tar)
    verti.append(y_tar)
    an.append(angle)
    xr.append(x_tar-xo)
    yr.append(y_tar-yo)

    xt,yt =x_tar,y_tar

#time=np.arange(0,count+1)


#plt.figure(figsize=(8, 6))

#plt.scatter(hori,verti,color='black')
#plt.scatter(xo,yo,color='red')

#plt.plot(time,an)



#plt.show()

    






#ekf implimentation



#initialization
#dt=1
#X=np.array([1,2,4,4])
X=np.array([xr[0],yr[0],vt,vt])
F=np.array([[1,0,T,0],[0,1,0,T],[0,0,1,0],[0,0,0,1]])
P=np.eye(4)*.001
#Q=np.eye(4)*.0001
Q=np.eye(4)*.009
R=.5
A=F

#functions for prediction and updation of state and measurnt


#def h(x):

#    msr=np.arctan2(x[1],x[0])

#   return msr


def jaco(x):
    
    de=x[0]**2+x[1]**2
    p1=-(x[1]/de)
    p2= x[0]/de

    return np.array([p1,p2,0,0])
    


def predict(x,p,q):

    x_pred= F@x.T+(np.random.multivariate_normal(np.zeros(4).T,Q))
    #print('xpred',x_pred)
    p_pred= A@p@A.T +q
    #print('ppred',p_pred)

    measure_pred=np.arctan2(x[1],x[0])+np.random.normal(0,R)
    #print('meaure_pred',measure_pred)
    

    return x_pred,p_pred, measure_pred


def update(x_pred,p_pred,r,measure,ang):
    H=jaco(x_pred)
    #print('jaco',H)
    r=R
    #print('r',r)
    z= ang+np.random.normal(0,.01) #sensor data
    #print(np.random.normal(0,1)
    y=z-measure
    #print('z',y)
    s= H@p_pred@H.T+r
    #print('s',s)
    k= (p_pred @ H.T)/s
    #print('k',k)

    x_update=x_pred+k*y
    p_update=(np.eye(len(x_pred))-(k@H))*p_pred
    
    
    return x_update,p_update



#time=[]

mse1=[]
mse2=[]



# outer loop for monte carlo analysis
for mc in range(1000):
    pos1=[]
    pos2=[]
    x_in=X
    p_in=P
    q_in=Q
    mse_x=[]
    mse_y=[]

    for t in range(count):

        ang=an[t]
        x_pr,p_pr,m_p= predict(x_in,p_in,q_in)

        x_u,p_u= update(x_pr,p_pr,R,m_p,ang)

        x_in,p_in=x_u,p_u

        pos1.append(x_u[0])
        pos2.append(x_u[1])

        mse_x.append((x_u[0]-xr[0])**2)
        mse_y.append((x_u[1]-xr[1])**2)

    mse1.append(sum(mse_x)/len(mse_x))
    mse2.append(sum(mse_y)/len(mse_y))

mse_pos_x=sum(mse1)/1000
mse_pos_y=sum(mse2)/1000

#avg_error=mse/1000
    
print(mse_pos_x,mse_pos_y)
    

    #print((np.sqrt((pos1[t]-xr[t])**2+(pos2[t]-xr[t])**2)))
    #print(m_p,ang)

    #time.append(t)




#plt.plot(pos1, pos2, marker='o', linestyle='-', color='black')
plt.plot(pos1,pos2)
plt.plot(xr,yr)
plt.xlabel("x componant of position")
plt.ylabel("y componant of position")
plt.title("estimation of relative position using EKF with stationary observer")
plt.show()









    

#plotting elements of state   

    
    

    

    
