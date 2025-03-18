"""
neural_net.py

A simple feed-forward neural network class.
(This could be extended to Hopfield or other biologically-inspired networks.)
"""

import numpy as np

class SimpleNeuralNet:
    def __init__(self, input_size: int, hidden_size: int, output_size: int):
        """
        Create a small feed-forward network with one hidden layer.
        Weights and biases are randomly initialized.
        """
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Xavier-like initialization
        self.weights_input_hidden = np.random.randn(input_size, hidden_size) * np.sqrt(2.0 / input_size)
        self.bias_hidden = np.zeros(hidden_size)
        
        self.weights_hidden_output = np.random.randn(hidden_size, output_size) * np.sqrt(2.0 / hidden_size)
        self.bias_output = np.zeros(output_size)

    def forward(self, x: np.ndarray) -> np.ndarray:
        """
        Forward pass.
        :param x: Input vector of shape (input_size,)
        :return: Output vector of shape (output_size,)
        """
        # Hidden layer
        h = np.dot(x, self.weights_input_hidden) + self.bias_hidden
        h_act = np.tanh(h)  # simple non-linear activation
        
        # Output layer
        o = np.dot(h_act, self.weights_hidden_output) + self.bias_output
        # e.g. we can do a final activation or not
        return o

    def copy(self):
        """
        Return a deep copy of the network (for GA reproduction).
        """
        new_net = SimpleNeuralNet(self.input_size, self.hidden_size, self.output_size)
        new_net.weights_input_hidden = np.copy(self.weights_input_hidden)
        new_net.bias_hidden = np.copy(self.bias_hidden)
        new_net.weights_hidden_output = np.copy(self.weights_hidden_output)
        new_net.bias_output = np.copy(self.bias_output)
        return new_net
