import numpy as np

from timeit import default_timer as timer

a = np.random.randn(1000)
b = np.random.randn(1000)

print("a: ")
print(a)
print("////////////////////////////////////////")
print("b: ")
print(b)
print("////////////////////////////////////////")

A = list(a)
B = list(b)

print("A: ")
print(A)
print("////////////////////////////////////////")
print("B: ")
print(B)
print("////////////////////////////////////////")

T = 1000

def dot1():
    dot = 0
    for i in range(len(A)):
        dot += A[i]*B[i]
    return dot

def dot2():
    return np.dot(a,b)

start = timer()
for t in range(T):
    dot1()
end = timer()
t1 = end - start


start = timer()
for t in range(T):
    dot2()
end = timer()
t2 = end - start

print('list calculation time: ', t1)
print('np.dot time: ', t2)
print('Ratio: ',t1/t2)