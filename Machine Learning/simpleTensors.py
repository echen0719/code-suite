# check it out: https://www.learnpytorch.io/00_pytorch_fundamentals/

import torch
import warnings
warnings.filterwarnings("ignore")

# print(torch.__version__)

# scalars and vectors as in precalc

scalar = torch.tensor(7) # out: tensor(7)
# print(scalar.ndim) # 0
# print(scalar.item()) # similar to .get() for Java Lists but only when ndim = 0
# print(scalar.shape) # out: torch.Size([])

vector = torch.tensor([7, 7]) # out: tensor([7, 7])
# print(vector.item) # returns object location
# print(vector.ndim) # out: 1
# print(vector.shape) # out: torch.Size([2]) because [7, 7]

matrix = torch.tensor([[1, 2], [3, 4]]) # yes, list within lists
# print(matrix.shape) # out: torch.Size([2, 2]) because [ [1, 2], [3, 4] ]
# print(vector.ndim) # out: 2

tensor = torch.tensor([ [[1, 2], [3, 4]], [[4, 5], [6, 7]], [[8, 9], [10, 11]] ])
# print(tensor.shape) # out: torch.Size([3, 2, 2]) because 3 elements with 2 each with 2 each

randTensor = torch.rand(size=(2, 3)) # 2 lists of 3 elements each -> [ [], [], [] ], [ [], [], [] ]
# print(randTensor) # out: tensor([[0.2173, 0.8464, 0.7906], [0.1793, 0.1094, 0.4972]])
# print(randTensor.dtype) # out: torch.float32

zeroedTensor = torch.zeros(size=(2, 2, 3)) # [ [[0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0]] ]
# print(zeroedTensor) # out: tensor([[[0., 0., 0.], [0., 0., 0.]], [[0., 0., 0.], [0., 0., 0.]]])

onedTensor = torch.ones(size=(3, 5)) # 3 lists of 5 ones each
# print(onedTensor) # out: tensor([[1., 1., 1., 1., 1.], [1., 1., 1., 1., 1.], [1., 1., 1., 1., 1.]])

# torch.zeros_like(input=$tensor) or torch.ones_like(input=$tensor)
# to create or set a tensor to all zeros or ones; most likely useful for later applications

rangedTensor = torch.arange(start=0, end=10, step=1)
# print(rangedTensor) # out: tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# None will default to default values
specificTensor = torch.tensor(rangedTensor, dtype=None, device=None, requires_grad=False)
# dtype for datatype, device for CPU/GPU/NPU, requires_grad records tensor operations

FP64Tensor = torch.tensor(torch.rand(size=(2, 3)), dtype=torch.double)
# print(FP64Tensor.dtype) # out: torch.float64, refer to line 28