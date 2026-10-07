#import numpy as np
#import matplotlib.pyplot as plt


#theta=np.linspace(0,360,100)


#x=[]
#y=[]


#for i in theta:


    #x.append(np.cos(np.radians(i)))
    #y.append(np.sin(np.radians(i)))



#plt.plot(x,y)

#plt.show()









import numpy as np
import scipy
import matplotlib.pyplot as plt
#from scipy.differentiate import jacobian



#data set

xo=0
yo=0
xt=0
yt=0
v=1
a=.2
theta=[0,30,90,60,120,150,180,210,240,270,300,330,360]
np.random.seed(42)
phi1=np.radians(np.random.choice(theta))
phi2=np.radians(90)


ti=np.linspace(0,100,100).tolist()
#count=100
hori=[]
verti=[]
#an=[np.arctan2((yt-yo),(xt-xo))]
xr=[]
yr=[]
an=[]


ax=a*np.cos(phi1)
ay=a*np.sin(phi1)
vx=v*np.cos(phi2)
vy=v*np.sin(phi2)

def param(t):

    #x=x2-x1
    #y=y2-y1
    #theta=np.arctan(y/x)
    #theta= np.arctan2(yt,xt)
  
 
    

    x2_new=xt+(t*vx)+ax*(t**2)/2
    y2_new=yt+(t*vy)+ay*(t**2)/2

    theta=np.atan2(y2_new,x2_new)

    return x2_new,y2_new,theta









R=np.radians(.1)



for i in ti:
    time=i
    #print(i)
    x_tar,y_tar,ang=param(time)
    ang=ang+np.random.normal(0,R)
    #print(x_tar,y_tar)
    hori.append(x_tar)
    verti.append(y_tar)
    an.append(ang)
    








T=1

X=np.array([hori[0],verti[0],vx,vy])
F=np.array([[1,0,T,0],[0,1,0,T],[0,0,1,0],[0,0,0,1]])
#np.array([[0,0,ax*(T**2)/2,0],[0,0,0,ay*(T**2)/2],[0,0,0,0],[0,0,0,0]])
#P=np.eye(4)*.1

P=.001*np.array([[(T**2)/2,0,0,0],[0,(T**2)/2,0,0],[0,0,1,0],[0,0,0,1]])
#Q=np.eye(4)*.0001
#Q=np.eye(4)*.01
Q=np.array([[1000000,0,0,0],[0,100,0,0],[0,0,.0001,0],[0,0,0,0.0001]])

A=F






#for i in range(count):
    

    #x_tar,y_tar,angle=param(xo,yo,xt,yt)
    #hori.append(x_tar)
    #verti.append(y_tar)
    #angle=angle+np.random.normal(0,R)
    #an.append(angle)
    #xr.append(x_tar-xo)
    #yr.append(y_tar-yo)

    #xt,yt =x_tar,y_tar

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

    x_pred= F@x.T
    #print('xpred',x_pred)
    p_pred= A@p@A.T +q
    #print('ppred',p_pred)

    measure_pred=np.arctan2(x_pred[1],x_pred[0])
    #print('meaure_pred',measure_pred)
    

    return x_pred,p_pred, measure_pred


def update(x_pred,p_pred,r,measure,z):
    H=jaco(x_pred)
    #print('jaco',H)
    r=R
    #print('r',r)
    #z= ang+np.random.normal(0,.01) #sensor data
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

#mse1=[]
#mse2=[]



# outer loop for monte carlo analysis
#for mc in range(1000):
pos1=[]
pos2=[]
x_in=X
p_in=P
q_in=Q
    #mse_x=[]
    #mse_y=[]

for p in range(len(ti)):

    ang=an[p]
    x_pr,p_pr,m_p= predict(x_in,p_in,q_in)

    z1= ang+np.random.normal(0,np.radians(.01))
    z=z1

    x_u,p_u= update(x_pr,p_pr,R,m_p,z)

    x_in,p_in=x_u,p_u

    pos1.append(x_u[0])
    pos2.append(x_u[1])

        #mse_x.append((x_u[0]-xr[0])**2)
        #mse_y.append((x_u[1]-xr[1])**2)

    #mse1.append(sum(mse_x)/len(mse_x))
    #mse2.append(sum(mse_y)/len(mse_y))

#mse_pos_x=sum(mse1)/1000
#mse_pos_y=sum(mse2)/1000

#avg_error=mse/1000
    
#print(mse_pos_x,mse_pos_y)
    

    #print((np.sqrt((pos1[t]-xr[t])**2+(pos2[t]-xr[t])**2)))
    #print(m_p,ang)

    #time.append(t)




#plt.plot(pos1, pos2, marker='o', linestyle='-', color='black')
plt.plot(pos1,pos2,label="target_path_ekf")
plt.plot(hori,verti,label="true_target_with_path")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("estimation of relative position using EKF with stationary observer")
plt.legend()
plt.show()









    

#plotting elements of state   

    
    

    

    

    
