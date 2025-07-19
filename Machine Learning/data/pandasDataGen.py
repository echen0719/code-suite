import pandas as pd
import numpy as np

# np.random.seed(37)
size = 10000
binSize = size // 2

performance = []
engagement = []
mathExtra = []
lovesMath = []

'''
What it does basically is:

- Generate a number from 0 to 100 to represent performance in math (as in grade).
- Generate a number from 0 to 10 to represent a person's interest (engagement) for math.
- Generate a binary number to represent wheter a person participates in math extracurriculars.
- If performance is greater than 80% and interest is greater than 7/10, then they love math.
- However, there is a 20% chance that their love is negated to introduce randomness.
- Keeps repeating this cycle until it reaches binSize for both sides of the classification.

55% - 100% should represent most US students...I think...I hope
'''

def generatePerson():
    e = np.random.randint(1, 11)
    m = np.random.choice([0, 1], p=[0.85, 0.15])

    if m:
        p = np.random.randint(75, 101)
        e = np.random.randint(5, 11)
    else:
        p = np.random.randint(55, 75)
        e = np.random.randint(0, 5)

    l = (p >= 80) & (e >= 7)

    if np.random.rand() < 0.20:
        l = not l

    return p, e, m, l

# idk about variable names
countLoves = 0
countNotLoves = 0

while countLoves < binSize or countNotLoves < binSize:
    p, e, m, l = generatePerson()

    if l and countLoves < binSize or e >= 9:
        performance.append(p)
        engagement.append(e)
        mathExtra.append(m)
        lovesMath.append(1)
        countLoves += 1
    elif not l and countNotLoves < binSize:
        performance.append(p)
        engagement.append(e)
        mathExtra.append(m)
        lovesMath.append(0)
        countNotLoves += 1

df = pd.DataFrame({
    'performance': performance,
    'engagement': engagement,
    'math_extracurriculars': mathExtra,
    'love_for_math': np.array(lovesMath).astype(int),
})

def getDataFrame():
    return df

# print(df.head(50))
counts = df['love_for_math'].value_counts()
# print(counts)