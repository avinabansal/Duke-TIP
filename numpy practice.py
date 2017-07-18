import numpy as np

ones = np.ones([5,4])
print ones

zeros = np.zeros([1,4])
zeros[0][0] = 1
print ""
print zeros
print ""

new = ones * zeros
print new
print ""

new[1][2] = 10
print new
print ""

times_two = new * 2
print times_two
print ""
print times_two.sum()

print times_two.max(axis = 1)
print times_two.mean(axis = 0)

