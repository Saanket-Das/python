
import numpy as np
# arr=np.array([[3,5,4,6,7]],np.int32) #creating numpy array np.int32 is setting the data type and its size
# print(arr[0,2:])
# print (arr.dtype,arr.shape)

# #more ways sto create array in python


# listarray=np.array([[1,2,3],[5,6,7],[8,9,0]])
# print(listarray)
# print(listarray.shape, listarray.size,)



import numpy as np
# np.array({32,23,23}) #dtype object can be created
import numpy as np

#intrisnic numpy array creation object like arage ones,zeros some functions thaat numpy gives
# zeros=np.zeros((2, 5))
# print(zeros)
# ones=np.ones((2, 5))
# print(ones)


#random no generretor a randpom numpy array generetor
# rng =np.arange(10)
# print(rng)
# lspace=np.linspace(1,50,10)#equally linearly spaced random number henerator 10 numbers btw 1 to 50
# print(lspace)

# emp=np.empty((4,6))
# print(emp) # will give empty arrayof random arrays  so we can assign anything
 
# emp_like =np.empty_like(lspace) #copies an array and makes it empty of the same size


# ide=np.identity #gives identity matrix

# arr=np.arange(99)
# arr=arr.reshape(3,33) #reshape it to 3X33 mtrix
# print(arr)

# arr.ravel() #make it one d array


 #numpy axis

 #one d array [1,2,3,4,5] 1[axis 0]
 #2d array [] 2 [axis 0 ,axis 1]

x=np.array([[1,2,3],[5,6,7],[8,9,0]])
print(x)
a=x.sum(axis=0) 
print(a)
x.T #traspose

x.flat #use for loop


for item in x.flat:
 print (item)


# x.argmin() 
# x.argmax() # min max

# x.argsort()

# x+arr #sum of array




import numpy as np

# Seucibilityed for reproductibiity
rng = np.random.default_rng(seed=1701)

# One-dimensional array
x1 = rng.integers(10, size=6)

# Two-dimensional array
x2 = rng.integers(10, size=(3, 4))

# Three-dimensional array
x3 = rng.integers(10, size=(3, 4, 5))

# Accessing array attributes
print("x3 ndim: ", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)
print("dtype: ", x3.dtype)



x1 = np.array([3, 4, 0, 3, 8, 6])
print(x1[:3])    # Output: [3 4 0]
print(x1[3:])    # Output: [3 8 6]
print(x1[1:4])   # Output: [4 0 3]
print(x1[::2])   # Output: [3 0 8]
print(x1[::-1])  # Output: [6 8 3 0 4 3]





x2 = np.array([[12, 1, 3, 7],
               [4, 0, 2, 3],
               [0, 0, 6, 9]])
print(x2[:2, :3])  # First two rows and three columns
print(x2[:3, ::2]) # Three rows, every second column
print(x2[::-1, ::-1]) # All rows and columns reversed





print(x2[:, 0])  # First column
print(x2[0, :])  # First row
print(x2[0])     # Equivalent to x2[0, :]



x2_sub = x2[:2, :2]
x2_sub[0, 0] = 99
print(x2_sub)
print(x2)





x2_sub_copy = x2[:2, :2].copy()
x2_sub_copy[0, 0] = 42
print(x2_sub_copy)
print(x2)




grid = np.arange(1, 10).reshape((3, 3))
print(grid)

x = np.array([1, 2, 3])
print(x.reshape((1, 3))) # Row vector
print(x.reshape((3, 1))) # Column vector

# Using np.newaxis
print(x[np.newaxis, :]) # Row vector
print(x[:, np.newaxis]) # Column vector





x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
z = np.array([99, 99, 99])

# Concatenate one-dimensional arrays
print(np.concatenate([x, y]))
print(np.concatenate([x, y, z]))

# Concatenate two-dimensional arrays
grid = np.array([[1, 2, 3],
                 [4, 5, 6]])
print(np.concatenate([grid, grid]))        # Along first axis
print(np.concatenate([grid, grid], axis=1)) # Along second axis

# Using np.vstack and np.hstack
print(np.vstack([x, grid]))
y = np.array([[99], [99]])
print(np.hstack([grid, y]))





x = np.array([1, 2, 3, 99, 99, 3, 2, 1])
x1, x2, x3 = np.split(x, [3, 5])
print(x1, x2, x3)

grid = np.arange(16).reshape((4, 4))

# Vertical split
upper, lower = np.vsplit(grid, [2])
print(upper)
print(lower)

# Horizontal split
left, right = np.hsplit(grid, [2])
print(left)
print(right)
