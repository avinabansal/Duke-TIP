import numpy as np

ones = np.ones(4)
print ones
onesM = np.ones((3,4))
print onesM
onesM[0][0] = 2
print onesM
ones[2] = 0
ones = ones * 4
print ones
onesM = onesM * ones
print onesM
print onesM.sum()
print onesM.sum(axis = 0)
print onesM.sum(axis = 1)

randomM = np.random.rand(3,4) * 10
randomM[2,3] = 11
randomM[1, :] = 2
randomM[:, 2] = 3
print randomM

print randomM.max()
print randomM.max(axis = 1)
print randomM.argmax()
print np.argwhere(randomM == randomM.argmax())
print randomM.mean()

