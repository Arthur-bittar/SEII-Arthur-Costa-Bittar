import numpy as np

l1 = [1,2,3]
l2 = [4,5,6]
dot = 0
for i in range(len(l1)):
    dot += l1[i] * l2[i]
print(dot)

a1 = np.array([1,2,3])
a2 = np.array([4,5,6])

dot = np.dot(a1,a2)
print(dot)

sum1 = a1 * a2
dot = np.sum(sum1)
print(dot)

dot = (a1 * a2).sum()
print(dot)

dot = a1 @ a2
print(dot)