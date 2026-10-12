import numpy as np
import matplotlib.pyplot as plt
import copy

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset





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

np.random.seed(42)
for i in range(len(xo)):

    x1.append(xo[i][0])
    y1.append(xo[i][1])
    x2.append(xt[i][0])
    y2.append(xt[i][1])
    xr.append(dx[i][0])
    yr.append(dx[i][1])
    an.append(np.atan2((y2[i]-y1[i]),(x2[i]-x1[i])))



d=copy.deepcopy(xo)

for j in range(len(d)):

    d[j].append(an[j].item())





x_full=torch.tensor(d)
y_full=torch.tensor(xt)

dataset = TensorDataset(x_full, y_full)

dataloader = DataLoader(dataset, batch_size=4, shuffle=True)






#split_index = int(len(x_full) * 0.80)
#x_train, x_test = x_full[:split_index], x_full[split_index:]
#y_train, y_test = y_full[:split_index], y_full[split_index:]




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
optimizer=op.SGD(model.parameters(),lr=.1)




for epoch in range(100):
  
    
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
   
    
    
    prediction=model(x_full)

    #print(prediction)


for temp in range(len(prediction)):

    

    tar_x.append(prediction.numpy()[temp][0].item())

    tar_y.append(prediction.numpy()[temp][1].item())



plt.plot(x1,y1,label='observer_path')

plt.plot(x2,y2,label='true_target_path')

plt.plot(tar_x,tar_y,label='target_path__ANN')

plt.xlabel("X (km)")
plt.ylabel("Y (km)")
plt.title("prediction of target path using ANN with stationary observer")


plt.legend()

plt.show()




    


