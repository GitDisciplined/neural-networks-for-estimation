
import numpy as np
import matplotlib.pyplot as plt
import copy
import pandas as pd




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



x1=[]
y1=[]
x2=[]
y2=[]
tar_x=[]
tar_y=[]
v=.123466
T=1


dat=[]
ang=[]

dat2=[]

r_values=[2,3,4,5]
c_values=[360-90,360-110,360-130,360-150,360-180]



for r in  r_values:
    for course in c_values:


#r=5
        b_in=np.radians(10)
#course=np.radians(230)

        tem1=r**2/(1+(np.tan(b_in)**2))
        tx0=np.sqrt(tem1)+xo[0][0]
        tem2=r**2-((tx0-xo[0][0])**2)
        ty0=np.sqrt(tem2)+xo[0][1]
        tvx0=v*np.cos(course)
        tvy0=v*np.sin(course)




        t_in=[tx0,ty0,tvx0,tvy0]


        t_bot=[t_in]
        ang_temp=[[np.atan2(ty0-xo[0][1],tx0-xo[0][0])+np.random.normal(0,1.5),r,course]]

        sour_in=[r,course,xo[0][0],xo[0][1],xo[0][2],xo[0][3],(np.atan2(ty0-xo[0][1],tx0-xo[0][0])+np.random.normal(0,1.5)),tx0,ty0,tvx0,tvy0]

        sour=[sour_in]
        
        



        for j in range(len(xo)-1):

            e1=t_bot[j][0]+T*tvx0
            e2=t_bot[j][1]+T*tvy0
            e3=tvx0
            e4=tvy0
            #print(e1)

            an=np.atan2(e2-xo[j][1],e1-xo[j][0])
            an=an+np.random.normal(0,1.5)
            ang_temp.append([an,r,course])


            sour.append([r,course,xo[j][0],xo[j][1],xo[j][2],xo[j][3],an,e1,e2,e3,e4])

          
    
    #tx0=e1 
    #ty0=e2

            t_bot.append([e1,e2,e3,e4])
            
           
            


        dat.append(t_bot)
        dat2.append(sour)
        ang.append(ang_temp)

        


set1=copy.deepcopy(dat)

set1=np.concatenate(set1,axis=0)
set1=set1.tolist()




set2=copy.deepcopy(dat2)

set2=np.concatenate(set2,axis=0)
set2=set2.tolist()



df = pd.DataFrame(set2, columns=["r", "c", "xo","yo","vxo","vyo","thet_rel","xt","yt","vxt","vyt"])

df.to_csv("sample2.csv")







