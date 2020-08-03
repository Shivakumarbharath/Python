import numpy as np

# to create an array of zeros
print(np.zeros((2, 3)))  # tuple as the shape of the matrix

# to create an array of oness
print(np.ones((2, 3)))

# identitiy
print(np.eye(3))

# array of random numbers
print(np.random.random((2, 3)))

# to get numbers from normal distribution
print(np.random.randn(2, 3))  # shape is not tuple it is individual parameters

# Create random normal distribution and mean of array
R = np.random.randn(10000)
print(R.mean())

# varience
print(R.var())

# Standard deviation

print(R.std())

# matrix of random data

K = np.random.randn(10000, 3)
print(K, ' K')
# calculate mean of each column
print(K.mean(axis=0))  # 0 means columns 1 means rows

# shape of th ematrix
print(K.shape)

# covarience
print(np.cov(R))

# create random integers

print(np.random.randint(0, 15, size=(2, 3)), ' randint')  # (low ,high, size)
