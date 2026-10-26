
import numpy as np
import matplotlib.pyplot as plt
import copy
import pandas as pd

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset







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
c_values=[0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360]

#r_values=np.linspace(2,5,100)
#c_values=np.linspace(0,360,1000)



for r in  r_values:
    for course in c_values:



        b_in=np.radians(10)
        tem1=r**2/(1+(np.tan(b_in)**2))
        tx0=np.sqrt(tem1)+xo[0][0]
        tem2=r**2-((tx0-xo[0][0])**2)
        ty0=np.sqrt(tem2)+xo[0][1]
        tvx0=v*np.cos(course)
        tvy0=v*np.sin(course)




        t_in=[tx0,ty0,tvx0,tvy0]


        t_bot=[t_in]
        ang_temp=[[np.atan2(ty0-xo[0][1],tx0-xo[0][0])+np.random.normal(0,np.radians(1.5)),r,course]]

        sour_in=[r,course,xo[0][0],xo[0][1],xo[0][2],xo[0][3],(np.atan2(ty0-xo[0][1],tx0-xo[0][0])+np.random.normal(0,np.radians(1.5))),tx0,ty0,tvx0,tvy0,tx0-xo[0][0],ty0-xo[0][1],tvx0-xo[0][2],tvy0-xo[0][3]]

        sour=[sour_in]
        
        



        for j in range(len(xo)-1):

            e1=t_bot[j][0]+T*tvx0
            e2=t_bot[j][1]+T*tvy0
            e3=tvx0
            e4=tvy0
            an=np.atan2(e2-xo[j][1],e1-xo[j][0])
            an=an+np.random.normal(0,np.radians(1.5))
            ang_temp.append([an,r,course])
            sour.append([r,course,xo[j][0],xo[j][1],xo[j][2],xo[j][3],an,e1,e2,e3,e4,e1-xo[j][0],e2-xo[j][1],e3-xo[j][2],e4-xo[j][3]])

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



df = pd.DataFrame(set2, columns=["r", "c", "xo","yo","vxo","vyo","thet_rel","xt","yt","vxt","vyt","x_rel","y_rel","vx_rel","vy_rel"])

df.to_csv("dataset_all_qudrants.csv")





feature=['xo','yo','vxo','vyo','thet_rel']
tar=['x_rel','y_rel','vx_rel','vy_rel']


x_full=torch.tensor(df[feature].values, dtype=torch.float32)
y_full=torch.tensor(df[tar].values, dtype=torch.float32)



#evaluation data



def test_set(ran,angle):

    r0=ran
    b_in0=np.radians(10)
    course0=np.radians(angle)
    v0=.123466
    T0=1
    tem10=r0**2/(1+(np.tan(b_in0)**2))
    tx00=np.sqrt(tem10)+xo[0][0]
    tem20=r0**2-((tx00-xo[0][0])**2)
    ty00=np.sqrt(tem20)+xo[0][1]
    tvx00=v0*np.cos(course0)
    tvy00=v0*np.sin(course0)
    an1=np.atan2(ty00-xo[0][1],tx00-xo[0][0])+np.random.normal(0,np.radians(1.5))




    t_test0=[xo[0][0],xo[0][1],xo[0][2],xo[0][3],an1]


    t_test=[t_test0]

    t_real_in=[tx00,ty00,tvx00,tvy00]
    t_real=[t_real_in]





    for j in range(len(xo)-1):

        e10=t_real[j][0]+T0*tvx00
        e20=t_real[j][1]+T0*tvy00
        e30=tvx00
        e40=tvy00
        ang10=np.atan2(e20-xo[j][1],e10-xo[j][0])+np.random.normal(0,np.radians(1.5))
        #print(ang10)
        
        t_test.append([xo[j][0],xo[j][1],xo[j][2],xo[j][3],ang10])

        t_real.append([e10,e20,e30,e40])




    return(t_test,t_real)






temp_ev=test_set(4.5,322)

x_ev=torch.tensor(temp_ev[0],dtype=torch.float32)





#ANN



dataset = TensorDataset(x_full, y_full)

dataloader = DataLoader(dataset, batch_size=4096, shuffle=True)



class ANN(nn.Module):

    def __init__(self):

        super().__init__()

        self.l1=nn.Linear(5,128)
        self.l2=nn.Linear(128,64)
        self.l3=nn.Linear(64,4)
        
        self.relu=nn.ReLU()

    def forward(self,x):

        x=self.relu(self.l1(x))
        x=self.relu(self.l2(x))
        x=self.l3(x)

        return x




import torch.optim as op

model=ANN()
criteria=nn.MSELoss()
optimizer=op.Adam(
    model.parameters(), 
    lr=0.001, 
    betas=(0.9, 0.999), 
    eps=1e-08, 
    weight_decay=0, 
    amsgrad=False)




for epoch in range(300):
  
    
    for batch_x, batch_y in dataloader:

        model.train()

        out=model(batch_x)

        loss=criteria(out,batch_y)

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()




tar_x=[]
tar_y=[]



model.eval()

with torch.no_grad():
   
    
    
    prediction=model(x_ev)

    


for temp in range(len(prediction)):

    x1.append(xo[temp][0])
    y1.append(xo[temp][1])
    x2.append(temp_ev[1][temp][0])
    y2.append(temp_ev[1][temp][1])

    tar_x.append(prediction.numpy()[temp][0].item()+x1[temp])

    tar_y.append(prediction.numpy()[temp][1].item()+y1[temp])



plt.plot(x1,y1,label='observer_path')

plt.plot(x2,y2,label='true_target_path')

plt.plot(tar_x,tar_y,label='target_path__ANN')

plt.xlabel("X (km)")
plt.ylabel("Y (km)")
plt.title("prediction of target path using ANN with moving observer")


plt.legend()

plt.show()















