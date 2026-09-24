import torch
import torch.nn as nn


#inp=torch.tensor([1,2]).float()

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
x_train=torch.tensor([[0,0],[0,1],[1,0],[1,1]]).float()
y_train=torch.tensor([0,1,1,0]).float().unsqueeze(1)




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
    test_data=torch.tensor([[1,1],[0,1],[0,0],[1,0]]).float()
    prediction=model(test_data)

    print(prediction)

    
























        
    
