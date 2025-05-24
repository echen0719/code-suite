# check it out: https://www.learnpytorch.io/00_pytorch_fundamentals/

import torch
import warnings
warnings.filterwarnings("ignore")

tensor = torch.tensor([1, 2, 3])
## print(tensor + 10) # out: tensor([11, 12, 13])
## print(tensor - 10) # out: tensor([-9, -8, -7])
## print(tensor * 10) # out: tensor([10, 20, 30])
## print(tensor / 10) # out: tensor([0.1000, 0.2000, 0.3000])

## print(tensor) # tensor([1, 2, 3])
# tensor remains the same because operations don't change tensor itself 

# MATRIX MULTIPLICATION
# I still need to learn this mathematically

# (a, b) @ (c, d)

# if b == c: it works
# size determined by a and d

# (2, 3) @ (3, 2)
# [                 [
#   [1, 2, 3]         [1, 2]
#   [4, 5, 6]         [3, 4]
#             ]       [5, 6]
#                            ]

# works because the first has 3 columns and second has 3 rows
# a = 2, d = 2 so size is 2 rows and 2 columns

# (3, 2) @ (2, 3)

# works because the first has 2 columns and second has 2 rows
# a = 3, d = 3 so size is 3 rows and 3 columns

# inner dimension = furthest to the right when .shape is printed

mat1 = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
## print(mat1.T) # out: tensor([ [1., 4.], [2., 5.], [3., 6.] ])

mat2 = torch.tensor([[1, 2], [3, 4], [5, 6]], dtype=torch.float32)
## print(mat2.T) # out: tensor([ [1., 3., 5.], [2., 4., 6.] ])

# yep, swaps the rows and columns so [1., 2., 3.] becomes [1., 4.]

## print(torch.matmul(mat1, mat2)) # out: tensor([[22, 28], [49, 64]])
# torch.mm() is alias

# smooth animations and useful: http://matrixmultiplication.xyz/

# LINEAR LAYERS

torch.manual_seed(69420) # ya know
linear = torch.nn.Linear(in_features=2, out_features=5)
# in_features needs to match inner dimension
linearTensor = linear(mat2)
## print(linearTensor)

# out: tensor([[ 1.8427,  0.6447,  0.8020, -0.8318,  0.5191],
#              [ 4.1900,  0.7330,  1.0927, -1.3720, -0.1103],
#              [ 6.5373,  0.8213,  1.3833, -1.9121, -0.7396]], grad_fn=<AddmmBackward0>)

## print(linearTensor.min()) # out: tensor(-1.9121, grad_fn=<MinBackward1>)
## print(linearTensor.max()) # out: tensor(6.5373, grad_fn=<MinBackward1>)

## print(linearTensor.type(torch.float32).mean()) # out: tensor(0.9067, grad_fn=<MeanBackward0>)
# need to specify dtype, not int, or else won't get correct values

## print(linearTensor.sum()) # out: tensor(13.6003, grad_fn=<SumBackward0>)

# uses row-major traversal with zero based indexing
## print(linearTensor.argmax()) # out: tensor(10)
## print(linearTensor.argmin()) # out: tensor(13)

rangedTensor = torch.arange(start=1, end=10.1, step=0.1) # 1.0000 -> 10.0000 by += 0.1000
## print(rangedTensor.dtype) # torch.float32
rangedTensor = rangedTensor.type(torch.int8)
## print(rangedTensor.dtype) # torch.int8
## print(rangedTensor.device) # cpu

primus = torch.tensor([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
secundus = torch.arange(start=1, end=10, step=1)

## print(primus) # out: tensor([[3,  2,  1], [6,  5, 4], [9,  8,  7]])
primus[1][2] = 10 # numpy style changes still apply
## print(primus) # out: tensor([3,  2,  1], [6,  5, 10], [9,  8,  7]])

## print(secundus.shape) # out: torch.Size([9])
secundus = secundus.reshape(primus.shape)

# secundus is now the same shape as primus
## print(secundus) # out: tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# torch.Size([3, 3]) for both primus and secundus
## print(primus.shape == secundus.shape) # out: True

# adds a tensor of size [3, 3] on top the original
stackedPrimus = torch.stack([primus, primus], dim=0) # shape is [2, 3, 3]
## print(stackedPrimus) # out: tensor([  [ [3,  2,  1], [6,  5, 10], [9,  8,  7] ], [ [3,  2,  1], [6,  5, 10], [9,  8,  7] ]  ])

# adds a copy of dim 1 (i.e. [3, 2, 1] or [6, 5, 4]) to the original for all elements in dim 1
stackedPrimus = torch.stack([primus, primus], dim=1) # shape is [3, 2, 3]
## print(stackedPrimus) # out: tensor([  [ [3,  2,  1], [3,  2,  1] ], [ [6,  5, 10], [6,  5, 10] ], [ [9,  8,  7], [9,  8,  7] ]  ])

# adds a copy of dim 2 (i.e. 3 or 2 or 1) to the original for all elements in dim 2
stackedPrimus = torch.stack([primus, primus], dim=2) # shape [3, 3, 2]
## print(stackedPrimus) # out: tensor([  [ [3,  3], [2,  2], [1,  1] ], [ [6,  6], [5,  5], [10, 10] ], [[9,  9], [8,  8], [7,  7] ]  ])

# stacking amount and dimension depends on inputed parameters
# so stack([primus, primus, primus]) would add 2 instead of 1 with [primus, primus]

## print(torch.squeeze(primus)) # removes dimensions of size 1, no change if none exist

tertius = torch.tensor([[[1]]])

## print(tertius.shape) # out: torch.Size([1, 1, 1])
tertius = torch.squeeze(tertius)
## print(tertius) # out: tensor(1)
## print(torch.unsqueeze(tertius, dim=0)) # out: tensor([1])

quartus = torch.randint(high=10, size=(1, 2, 3))
## print(quartus) # out: tensor([  [ [8, 9, 6], [3, 9, 1] ]  ])
# 1, 2, 3 --> 3, 2, 1
## print(quartus.permute(2, 1, 0)) # out: tensor([  [ [8], [3] ], [ [9], [9] ], [ [6], [1] ]  ])

# values inside reshape() need to multiply to size of tensor
reshaped = torch.arange(1, 9).reshape(2, 2, 2)
## print(reshaped) # out: tensor([  [ [1, 2], [3, 4] ], [ [5, 6], [7, 8] ]  ])
## print("{}, {}, {}".format(reshaped[0][1][0], reshaped[1][0][1], reshaped[0][0][1])) # out: 3, 6, 2

# numpy styled
print(reshaped[:, :, 0]) # out: tensor([[1, 3], [5, 7]])