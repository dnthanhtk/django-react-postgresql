import torch
import numpy as np
a = np.ones(1)
b = torch.from_numpy(a)
c = torch.from_numpy(a+1)
np.add(a,2,out=a)
print(c)
print(a)
print(b)