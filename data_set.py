import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


xo=1
yo=2
xt=10
yt=25
vt=5

T=1
count=100
hori=[xt]
verti=[yt]
an=[(yt-yo)/(xt-xo)]
xr=[xt-xo]
yr=[yt-yo]

def param(x1,y1,x2,y2):

    #x=x2-x1
    #y=y2-y1
    #theta=np.arctan(y/x)

    x2_new=x2+(T*vt)
    y2_new=y2+(T*vt)

    theta=(y2_new-yo)/(x2_new-xo)

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


plt.figure(figsize=(8, 6))

plt.scatter(hori,verti,color='black')
plt.scatter(xo,yo,color='red')

#plt.plot(time,an)



plt.show()

    

    

   

    

    


