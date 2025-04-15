import numpy as np
array = np.random.randint(1,10, size=(5,5), dtype=int)
print(array)
print(array[1,2])
print(array.sum())
print(np.mean(array, axis=1))
print(np.max(array, axis=0))
#:)