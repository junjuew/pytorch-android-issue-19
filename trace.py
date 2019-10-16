import torch
from torch.autograd import Variable
from torch.optim import Adam
from torch.utils.data import DataLoader
import torchvision
from torchvision import datasets
from torchvision import transforms

from transformer_net import TransformerNet

class Tracer():
    def __init__(self):
        self.model = 'input-trained.model'
        self.style_model = TransformerNet()
        self.style_model.load_state_dict(torch.load(self.model))
    
    def trace(self):
        nn_input = torch.rand(1, 3, 224, 224)
        traced_script_module = torch.jit.trace(self.style_model, nn_input)
        traced_script_module.save('serialized.pt')
        print('traced model saved to serialized.pt')

if __name__ == "__main__":
    tracer = Tracer()
    tracer.trace()
