import numpy as np
import matplotlib.pyplot as plt



np.random.seed(42)


xo= [ [0,         0  ,  0.0992 ,  -0.1182],
    [0.0992,   -0.1182,    0.0992  , -0.1182],
    [0.1984 ,  -0.2364 ,   0.0992 ,  -0.1182],
    [0.2976 ,  -0.3547 ,   0.0992,   -0.1182],
    [0.3968,   -0.4729 ,   0.0992,   -0.1182],
    [0.4960,   -0.5911 ,   0.0992,   -0.1182],
    [0.5952,   -0.7093,    0.0992,   -0.1182],
    [0.6944,   -0.8276 ,   0.0992,   -0.1182],
    [0.7936,   -0.9458,    0.0992,   -0.1182],
    [0.8928 ,  -1.0640,    0.0992 ,  -0.1182],
    [0.9920,   -1.1822,    0.0992,   -0.1182],
    [1.0912,   -1.3005,    0.0992,   -0.1182],
    [1.1904,   -1.4187,    0.0992,   -0.1182],
    [1.3168,   -1.5072,    0.1264,   -0.0885],
    [1.4703,   -1.5233,    0.1535,   -0.0161],
    [1.6102,   -1.4581,    0.1399,    0.0652],
    [1.6965,   -1.3302,    0.0863 ,   0.1279],
    [1.7493,   -1.1851,   0.0528,    0.1450],
    [1.8021,   -1.0401,    0.0528,    0.1450],
    [1.8548,  -0.8951,    0.0528,    0.1450],
    [1.9076,   -0.7501,    0.0528,    0.1450],
    [1.9604,   -0.6051,    0.0528,    0.1450],
    [2.0132,   -0.4600,    0.0528,    0.1450],
    [2.0660,   -0.3150,    0.0528,    0.1450],
    [2.1188,   -0.1700,    0.0528,    0.1450],
    [2.1715,   -0.0250,    0.0528,    0.1450],
    [2.2243,    0.1201,    0.0528,    0.1450],
    [2.2771,    0.2651,    0.0528,    0.1450],
    [2.3299,    0.4101,    0.0528,    0.1450],
    [2.3827,    0.5551,    0.0528,    0.1450],
    [2.4355,    0.7002,    0.0528,    0.1450]]




xt= [[4.9286,    0.8420,   -0.0794,   -0.0946],
    [4.8486,    0.7469,   -0.0800,   -0.0952],
    [4.7695,    0.6510,   -0.0783,   -0.0954],
    [4.6902,    0.5567,   -0.0805,   -0.0939],
    [4.6100,    0.4637,   -0.0811,   -0.0920],
    [4.5288,   0.3724,   -0.0825,   -0.0902],
    [4.4475,    0.2825,   -0.0822,   -0.0896],
    [4.3657,    0.1923,   -0.0828,   -0.0911],
    [4.2830,    0.1011,   -0.0830,   -0.0899],
    [4.2011,    0.0122,   -0.0823,   -0.0874],
    [4.1192,   -0.0729,   -0.0812,   -0.0837],
    [4.0383,   -0.1554,   -0.0810,   -0.0808],
    [3.9562,   -0.2368,   -0.0836,   -0.0832],
    [3.8726,   -0.3214,   -0.0819,   -0.0863],
    [3.7910,   -0.4084,   -0.0810,   -0.0883],
    [3.7101,   -0.4946,   -0.0800,   -0.0860],
    [3.6324,   -0.5806,   -0.0757,   -0.0862],
    [3.5568,   -0.6680,   -0.0762,   -0.0883],
    [3.4803,   -0.7573,   -0.0772,   -0.0887],
    [3.4032,   -0.8473,   -0.0747,   -0.0907],
    [3.3293,   -0.9385,   -0.0749,   -0.0915],
    [3.2558,   -1.0291,   -0.0721,   -0.0905],
    [3.1814,   -1.1183,   -0.0749,  -0.0890],
    [3.1055,   -1.2087,  -0.0756,   -0.0904],
    [3.0296,   -1.3016,   -0.0758,   -0.0942],
    [2.9539,   -1.3963,   -0.0754 ,  -0.0946],
    [2.8787,   -1.4906,   -0.0749,   -0.0941],
    [2.8039,   -1.5852,   -0.0756,   -0.0946],
    [2.7279,  -1.6791,   -0.0767,  -0.0923],
    [2.6520,   -1.7713,   -0.0741,   -0.0922],
    [2.5770,   -1.8643 ,  -0.0746,   -0.0927]]



dx=(np.array(xt)-np.array(xo)).tolist()




#t=np.linspace(0,30,31)

x1=[]
y1=[]
x2=[]
y2=[]
xr=[]
yr=[]
an=[]


for i in range(len(xo)):

    x1.append(xo[i][0])
    y1.append(xo[i][1])
    x2.append(xt[i][0])
    y2.append(xt[i][1])
    xr.append(dx[i][0])
    yr.append(dx[i][1])
    an.append(np.atan2((y2[i]-y1[i]),(x2[i]-x1[i])))




T=1

X=np.array(dx[0])
F=np.array([[1,0,T,0],[0,1,0,T],[0,0,1,0],[0,0,0,1]])
#np.array([[0,0,ax*(T**2)/2,0],[0,0,0,ay*(T**2)/2],[0,0,0,0],[0,0,0,0]])
#P=np.eye(4)*.1

#P=.001*np.array([[(T**2)/2,0,0,0],[0,(T**2)/2,0,0],[0,0,1,0],[0,0,0,1]])


#Q=np.eye(4)*.0001
#Q=np.eye(4)*.01
#Q=np.array([[1000000,0,0,0],[0,100,0,0],[0,0,.0001,0],[0,0,0,0.0001]])
R=np.radians(.1)*10
A=F
Q=np.array([[0.0981,0,0.1472,0],[ 0,0.0981,0,0.1472],[0.1472,0,0.2944,0],[ 0    ,0.1472,0,0.2944]])* 1.0e-05
P=np.array([[0.0019,-0.0007,0.0002,-0.0000],[-0.0007,0.0103,0.0005,0.0009],[0.0002,0.0005,0.0001,0.0000],[ -0.0000,0.0009,0.0000,0.0001]])






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
    


def predict(x,p,q,c):
    

    x_pred= F@x.T-c
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

for p in range(len(xt)-1):

    c1=xo[p+1][0]-xo[p][0]-xo[p][2]*T
    c2=xo[p+1][1]-xo[p][1]-xo[p][3]*T
    c3=xo[p+1][2]-xo[p][2]
    c4=xo[p+1][3]-xo[p][3]
    mat=np.array([c1,c2,c3,c4])
    print(mat)
    

    ang=an[p]
    x_pr,p_pr,m_p= predict(x_in,p_in,q_in,mat)

    z1= ang+np.random.normal(0,np.radians(R))
    z=z1

    x_u,p_u= update(x_pr,p_pr,R,m_p,z)

    x_in,p_in=x_u,p_u

    pos1.append(x_u[0]+xo[p][0])
    pos2.append(x_u[1]+xo[p][1])

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





plt.plot(x1,y1,label='observer_path')
plt.plot(x2,y2,label='true_target_path')
plt.plot(pos1,pos2,label='estimated_target_path')


plt.xlabel("X position (Km)")
plt.ylabel("Y position (Km)")
plt.title("estimation of target postion using EKF with moving observer")
plt.legend()
plt.show()




    
    

    
