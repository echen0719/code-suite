# check it out: https://www.learnpytorch.io/00_pytorch_fundamentals/

import torch
import warnings
warnings.filterwarnings("ignore")

tensor = torch.tensor([1, 2, 3])
# print(tensor + 10) # out: tensor([11, 12, 13])
# print(tensor - 10) # out: tensor([-9, -8, -7])
# print(tensor * 10) # out: tensor([10, 20, 30])
# print(tensor / 10) # out: tensor([0.1000, 0.2000, 0.3000])

# print(tensor) # tensor([1, 2, 3])
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
# print(mat1.T) # out: tensor([ [1., 4.], [2., 5.], [3., 6.] ])

mat2 = torch.tensor([[1, 2], [3, 4], [5, 6]], dtype=torch.float32)
# print(mat2.T) # out: tensor([ [1., 3., 5.], [2., 4., 6.] ])

# yep, swaps the rows and columns so [1., 2., 3.] becomes [1., 4.]

# print(torch.matmul(mat1, mat2)) # out: tensor([[22, 28], [49, 64]])
# torch.mm() is alias

# smooth animations and useful: http://matrixmultiplication.xyz/

# LINEAR LAYERS

torch.manual_seed(69420) # ya know
linear = torch.nn.Linear(in_features=2, out_features=5)
# in_features needs to match inner dimension
linearTensor = linear(mat2)
# print(linearTensor)

# out: tensor([[ 1.8427,  0.6447,  0.8020, -0.8318,  0.5191],
#              [ 4.1900,  0.7330,  1.0927, -1.3720, -0.1103],
#              [ 6.5373,  0.8213,  1.3833, -1.9121, -0.7396]], grad_fn=<AddmmBackward0>)

# print(linearTensor.min()) # out: tensor(-1.9121, grad_fn=<MinBackward1>)
# print(linearTensor.max()) # out: tensor(6.5373, grad_fn=<MinBackward1>)

# print(linearTensor.type(torch.float32).mean()) # out: tensor(0.9067, grad_fn=<MeanBackward0>)
# need to specify dtype or else error

# print(linearTensor.sum()) # out: tensor(13.6003, grad_fn=<SumBackward0>)

# uses row-major traversal with zero based indexing
# print(linearTensor.argmax()) # out: tensor(10)
# print(linearTensor.argmin()) # out: tensor(13)

rangedTensor = torch.arange(start=1, end=10.1, step=0.1) # 1.0000 -> 10.0000 by += 0.1000
# print(rangedTensor.dtype) # torch.float32
rangedTensor = rangedTensor.type(torch.int8)
# print(rangedTensor.dtype) # torch.int8