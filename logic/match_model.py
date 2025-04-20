import torch
import torch.nn as nn

class MatchOutcomeModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(14,32),
            nn.ReLU(),
            nn.Linear(32,16),
            nn.ReLU(),
            nn.Linear(16,3)
        )
    
    def forward(self,x):
        return self.model(x)