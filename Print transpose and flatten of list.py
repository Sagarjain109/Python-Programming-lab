import numpy as np
M,N = map(int,input('Enter the rows and colims: ').split())
ls1 = []
for i in range(M):
    ls2 = list(map(int,input('Enter the elements: ').split()))[:N]
    ls1.append(ls2)
arr = np.array(ls1)
print(arr.transpose())
print(arr.flatten())

