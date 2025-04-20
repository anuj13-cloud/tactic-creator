import json 
import torch
from torch.utils.data import Dataset 

with open('../data/match_data.json') as f:
    data = json.load(f)


inputs = []
labels = []
for item in data:
    inputs.append(item['input'])
    labels.append(item['label'])

x = torch.tensor(inputs, dtype = torch.float32)
y  = torch.tensor(labels, dtype = torch.long)

print(x.shape,y.shape)

class MatchDataset(Dataset):
    def __init__(self,x,y):
        self.x= x
        self.y =y 
    
    def __len__(self):
        return len(self.x)

    def __getitem__(self,idx):
        return self.x[idx], self.y[idx]
    
    def get_class_distribution(self):
        classes = torch.bincount(self.y)
        return classes 

dataset = MatchDataset(x,y)

print(len(dataset))
print(dataset[0])
print(dataset.get_class_distribution())