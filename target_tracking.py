import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn


#data_preprocessing


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



class tracking_data():

    def __init__(self):

        self.X

    





    





class ANN(nn.Module):

    def __init__(self,a,b):

        super().__init__()

        self.l1=nn.Linear(a,b)
        self.l2=nn.Linear(b,1)
        self.relu=nn.ReLU()

    def forward(self,x):

        x=self.relu(self.l1(x))
        x=self.l2(x)

        return x


#layers=ANN(2,4)

#out=layers.forward(inp)
x_train=torch.tensor().float()
y_train=torch.tensor().float().unsqueeze(1)




import torch.optim as op

model=ANN(2,8)
criteria=nn.MSELoss()
optimizer=op.SGD(model.parameters(),lr=.1)




for epoch in range(100):

    model.train()

    out=model(x_train)

    loss=criteria(out,y_train)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()



model.eval()

with torch.no_grad():
    test_data=torch.tensor().float()
    prediction=model(test_data)

    print(prediction)

    
























        
    
