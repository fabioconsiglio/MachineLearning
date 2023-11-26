import torch
w = torch.tensor(1.0, requires_grad = True)
b = torch.tensor(0.5, requires_grad = True)
x = torch.tensor([1.4])
y = torch.tensor([2.1])
z = torch.add(torch.mul(w,x),b)
loss = (y-z).pow(2).sum()
loss.backward()
print(w.grad)
print(b.grad)
