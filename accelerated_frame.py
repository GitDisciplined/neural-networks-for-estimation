import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


xo=0
yo=0
xt=0
yt=0
v=1
a=2
phi1=np.radians(90)
phi2=np.radians(30)


ti=np.linspace(0,50,100).tolist()
#count=100
hori=[]
verti=[]
#an=[np.arctan2((yt-yo),(xt-xo))]
xr=[]
yr=[]

def param(t):

    #x=x2-x1
    #y=y2-y1
    #theta=np.arctan(y/x)
    #theta= np.arctan2(yt,xt)
    ax=a*np.cos(phi1)
    ay=a*np.sin(phi1)
    vx=v*np.cos(phi2)
    vy=v*np.sin(phi2)
 
    

    x2_new=xt+(t*vx)+ax*(t**2)/2
    y2_new=yt+(t*vy)+ay*(t**2)/2

    theta=np.arctan2(y2_new,x2_new)

    return x2_new,y2_new


for i in ti:
    time=i
    print(i)
    x_tar,y_tar=param(time)
    print(x_tar,y_tar)
    hori.append(x_tar)
    verti.append(y_tar)
    
    
    #an.append(angle)
    #xr.append(x_tar-xo)
    #yr.append(y_tar-yo)

    #xt,yt =x_tar,y_tar

#time=np.arange(0,count+1)


plt.figure(figsize=(8, 6))

plt.plot(hori,verti,color='black')
#plt.plot(xo,yo,color='red')

#plt.plot(time,an)



plt.show()

    

    

   

    

    


