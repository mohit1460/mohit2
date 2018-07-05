#question1
import numpy as np
a=np.random.random((10,1))
print(a)
print(a.shape)
print(np.mean(a))

#question2
b=np.random.random((20,1))
print(b)
print(b.shape)
print(np.var(b))
print(np.std(b))

#question3
import numpy as np
c=np.random.random((10,20))
print(c)
d=np.random.random((20,25))
print(d)
e=np.matmul(c,d)
print(e)
print(e.shape)
print(e.sum())

#question4

import numpy as np
from math import *
x=np.full((10,1),2)
print(x)
def f(x):
    return 1/(1+exp(-x))
f_v=np.vectorize(f)
sc=np.array(x)
n= f_v(sc)
print(n)