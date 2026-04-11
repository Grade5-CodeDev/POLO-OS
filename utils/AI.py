!pip install numpy
import numpy as np

def relu(x):
  return np.maximum(0, x)

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

#AI class
class AI:
  def __init__(self, lr=0.01):
    self.lr = lr
    self.w = np.random.randn(0,1)
    self.b = np.randim.randn(0.00, 0.12)
  
  def forward