import numpy as np

l = [1,2,3]
a = np.array([1,2,3])

print(l)
print(a)

l = l + [4]
print(l)
a = a + np.array([4]) #Igual a a + np.array([4,4,4])
print(a)

l = [1,2,3]
a = np.array([1,2,3])
l = l * 2
print(l)
a = a * 2
print(a)

a = np.array([1,2,3])
a = np.sqrt(a)
print(a)

a = np.array([1,2,3])
a = np.log(a)
print(a)

