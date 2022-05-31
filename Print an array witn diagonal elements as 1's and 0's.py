import numpy as np
lst=list(map(int,input().strip().split()))
x,y =lst[0],lst[1]
ar=np.eye(x,y)
print(ar)
