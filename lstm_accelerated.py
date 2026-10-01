import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader


#lstm = nn.LSTM(input_size=1, hidden_size=4, num_layers=1, batch_first=True)


#x = torch.randn(1, 5, 1)
#out, (hn, cn) = lstm(x)


#x=np.arange(0,20,.1)

#y=np.sin(x)
    
#x_train=torch.tensor(x.tolist()[:100]).unsqueeze(1).unsqueeze(1)
#x_train=torch.split(x_train,10)
#y_train=torch.tensor(y.tolist()[:100]).unsqueeze(1)
#y_train=torch.split(y_train,10)


#dataset=TensorDataset(x_train,y_train)

#dataloader= DataLoader(dataset, batch_size=1, shuffle=False)

#x_test=torch.tensor(x.tolist()[100:]).unsqueeze(1).unsqueeze(1)
#y_test=torch.tensor(y.tolist()[100:]).unsqueeze(1)



#dataset

xo=0
yo=0
xt=0
yt=0
v=1
a=2
phi1=np.radians(90)
phi2=np.radians(30)


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

    return x2_new/10,y2_new/1000,theta









R=np.radians(.01)



for i in ti:
    time=i
    #print(i)
    x_tar,y_tar,ang=param(time)
    ang=ang+np.random.normal(0,R)
    #print(x_tar,y_tar)
    hori.append(x_tar)
    verti.append(y_tar)
    an.append(ang)
    




#neural network
a=[]
for k in range(len(an)):
    a.append([hori[k],verti[k],an[k]])
    
    



#a=np.arange(0,60,.1)
#b=np.sin(a)

step=3
features=3
x=[]
y=[]



for j in range(len(a)-step):

    x.append(a[j:j+step])

    
    y.append(a[j+step][:2])


x=np.array(x)
y=np.array(y)



x=np.reshape(x,(x.shape[0],x.shape[1],features))


x=torch.tensor(x,dtype=torch.float32)
y=torch.tensor(y,dtype=torch.float32).unsqueeze(1)



split_index = int(len(x) * 0.80)
x_train, x_test = x[:split_index], x[split_index:]
y_train, y_test = y[:split_index], y[split_index:]






class recurrent(nn.Module):

    def __init__(self):

        super().__init__()

        self.lstm=nn.LSTM(3,6,1)
        self.fc1=nn.Linear(6,8)
        self.fc2=nn.Linear(8,2)
        self.relu=nn.ReLU()
        


    def forward(self,x):

        p,q=self.lstm(x)
        #print(q)
        
        o=self.fc1(p[-1])
        #print(o)
        o=self.relu(o)
        #print(o)
        o=self.fc2(o)
        #print(o)

        return o


import torch.optim as op

model=recurrent()
criteria=nn.MSELoss()
#optimizer=op.SGD(model.parameters(),lr=.1)
optimizer = op.Adam(model.parameters(), lr=0.01, weight_decay=1e-4)



for epoch in range(100):
    
    model.train()

    for temp in range(len(x_train)):

        out=model(x_train[temp])
        #print(x_train[temp],out)
        out=out.unsqueeze(0)

        #print(out,y_train[temp])

        loss=criteria(out,y_train[temp])
        #print(loss)

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()


model.eval()


x_new=[]
x_pred=[]
y_pred=[]
y_actual=[]
x_actual=[]

with torch.no_grad():

    
    
    for k in range(len(x_test)):
        
        prediction=model(x_test[k])

        #print( prediction)

        x_new.append(k)
        x_pred.append(prediction[0].tolist()*10)
        y_pred.append(prediction[1].tolist()*1000)
        
        x_actual.append(y_test[k][0][0].tolist()*10)
        y_actual.append(y_test[k][0][1].tolist()*1000)
       
    

plt.plot(x_pred,y_pred,label="predicted trajectory")
plt.plot(x_actual,y_actual,label="actual trajectory")

plt.legend()
plt.show()





        
        
        

        
    

