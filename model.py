import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn import BatchNorm1d,ReLU,Linear

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.model = torch.nn.Sequential(
            Linear(state_size,100),
            BatchNorm1d(100),
            ReLU(),
            Linear(100,50),
            BatchNorm1d(50),
            ReLU(),
            Linear(50,action_size)
            )

    def forward(self, state):
        """Build a network that maps state -> action values."""
        return self.model(state)
