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


a=np.arange(0,20,.1)
b=np.sin(a)

step=4
features=1
x=[]
y=[]



for i in range(len(a)-step):

    x.append(a[i:i+step])

    
    y.append(b[i+step])


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

        self.lstm=nn.LSTM(1,10,1)
        self.fc1=nn.Linear(10,8)
        self.fc2=nn.Linear(8,1)
        self.relu=nn.ReLU()


    def forward(self,x):

        p,(q,r)=self.lstm(x)

        out=self.fc1(q)
        out=self.relu(out)
        out=self.fc2(out)

        return y


import torch.optim as op

model=recurrent()
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


x_new=[]
y_new=[]

with torch.no_grad():

    
    
    for k in  x_test:
        #print(k)
        prediction=model(k)

        print(k,prediction)
       
    

#plt.plot(x_new,y_new)
#plt.show()





        
        
        

        
    

