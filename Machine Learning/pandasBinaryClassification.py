import torch
from torch.utils.data import Dataset, DataLoader
from data.pandasDataGen import getDataFrame

df = getDataFrame()
# print(df.head(50))

features = df[['performance', 'engagement', 'math_extracurriculars']].values
print(features)
labels = df['love_for_math'].values
print(labels)

xTensor = torch.from_numpy(features).float()
yTensor = torch.from_numpy(labels).long()

print(xTensor, yTensor)