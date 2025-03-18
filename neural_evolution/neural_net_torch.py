"""
neural_net_torch.py

Example PyTorch-based feedforward network for illustration.

We represent each individual genotype as a flattened vector of parameters (weights/biases).
"""

import torch
import torch.nn as nn

class NeuralNetTorch(nn.Module):
    def __init__(self, input_size=5, hidden_size=3, output_size=2):
        super().__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
        # optionally add activation if you want (e.g. ReLU), but keep it simple for now

    def forward(self, x):
        # x shape: (batch_size, input_size)
        h = self.fc1(x)
        h = torch.tanh(h)
        o = self.fc2(h)
        return o

    def get_param_vector(self):
        """
        Flatten all parameters into a 1D vector (CPU).
        """
        with torch.no_grad():
            return torch.cat([p.view(-1) for p in self.parameters()]).cpu().numpy()

    def set_param_vector(self, param_vector):
        """
        Inverse of get_param_vector: load from a 1D array.
        """
        with torch.no_grad():
            idx = 0
            for p in self.parameters():
                numel = p.numel()
                shape = p.shape
                chunk = param_vector[idx:idx+numel]
                p.copy_(torch.from_numpy(chunk.reshape(shape)))
                idx += numel
