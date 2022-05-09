from enum import unique
import sys
from xml.sax.handler import property_interning_dict
import numpy as np
import pandas as pd
print(np.__version__)    #  1.20.3
np.set_printoptions(threshold= sys.maxsize)


# shape, size, ndim, dtype, itemsize, data

# arary creation: np.ones, np.zeros, np.empty, np.arange, np.linspace
a = np.zeros(shape= (3, 4), dtype= np.int16)
b= np.ones(shape=(3, 4), dtype= np.float16)
c= np.empty(shape= (3, 4), dtype= np.float16)

print(c)
print(c.shape)    #  (3, 4)
print(c.ndim)    #  2

d = np.arange(0, 9, 1)    # (start, stop, stepsize),   [0 1 2 3 4 5 6 7 8]
print(d)

f= np.linspace(0, 1, 5)  # (start, stop, #elements)
print(f)

#--------------------------------------------------------------------------------
## Basic operations:
"""
*: elementwise product
@: matrix dot product
"""

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A)
print(B)

print(A * B)    # elementwise product
#############################################
print(A.dot(B))
print( A @ B)
"""
A: 
[[1 2]
 [3 4]]

B:
 [[5 6]
 [7 8]]
 
 elementwise product * :  
  [[(1*5)  (2*6)]
   [(3*7) (4*8)]]

Dot product np.dot, @: row*column
(1*5 + 2*7) = 19
(3*5 + 4*7) = 43

(1*6 + 2*8) = 22
(3*6 + 4*8) = 50

[[19 22]
 [43 50]]
"""
print('______________________________________')
### += , *= act in place ti modify an existing array rather than create a new one.

rg= np.random.default_rng(1)
b = rg.random((2, 3))
print(b)
               # [[0.51182162 0.9504637  0.14415961]
               #  [0.94864945 0.31183145 0.42332645]]
# extract dtype name

c= np.ones(shape= (2, 3), dtype= np.float16)
print(c.dtype.name)    #  float16
######################################################
b= np.arange(12).reshape(3,4)
print(b)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print(b.sum(axis= 0)) #|
# [12 15 18 21]

print(b.sum(axis= 1)) # ___
# [ 6 22 38]
#--------------------------------------------------------------------------------
## Universal functions: ufunc --> sin, cos and exp, sqrt, add
#--------------------------------------------------------------------------------
# Convert a 1D array into a 2D array (how to add a new axis to an array)
a = np.arange(1, 7)    #  [1 2 3 4 5 6]
print(a.shape)    # (6,)

row_vector = a[np.newaxis, :]
print(row_vector)    # [[1 2 3 4 5 6]]
print(row_vector.shape)    # (1, 6)
#-----------------------------------
col_vector = a[:, np.newaxis]
print(col_vector.shape)    #  (6, 1)
print(col_vector)
# [[1]
#  [2]
#  [3]
#  [4]
#  [5]
#  [6]]
#--------------------------------------------------------------------------------
# You can also expand an array by inserting a new axis at a specified position with np.expand_dims.
b = np.expand_dims(a, axis=1)
print(b.shape)    # (6, 1)
print(b)
# [[1]
#  [2]
#  [3]
#  [4]
#  [5]
#  [6]]

c = np.expand_dims(a, axis= 0)
print(c.shape)    # (1, 6)
print(c)    #  [[1 2 3 4 5 6]]

#--------------------------------------------------------------------------------
# Indexing and slicing
a = np.arange(1, 13).reshape(3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

print(a[a < 5])    # [1 2 3 4]

five_up = (a >= 5)
print(a[five_up])    # [ 5  6  7  8  9 10 11 12]

divisible_by_2 = a[a%2 == 0]
print(divisible_by_2)    #  [ 2  4  6  8 10 12]
#------------------------------------
# Multiple conditions with &, | operators
c= a[(a>2) & (a<11)]
print(c)    #  [ 3  4  5  6  7  8  9 10]

five_up = (a > 5) | (a == 5)
#------------------------------------
# You can use np.nonzero() to print the indices of elements that are, for example, less than 5:

b= np.nonzero(a < 5)
print(b)    #  (array([0, 0, 0, 0], dtype=int64), array([0, 1, 2, 3], dtype=int64))
# In this example, a tuple of arrays was returned: one for each dimension. The first array represents the row indices where
# these values are found, and the second array represents the column indices where the values are found.
#------------------------------------
# crate a list of coordinates using b array
list_of_coordinates = list(zip(b[0], b[1]))

for coord in list_of_coordinates:
   print(coord)

# (0, 0)
# (0, 1)
# (0, 2)
# (0, 3)

# use np.nonzero() to print the elements in an array that are less than 5 with
print(a)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
print(b)    # (array([0, 0, 0, 0], dtype=int64), array([0, 1, 2, 3], dtype=int64))
print(a[b])    # [1 2 3 4]
#--------------------------------------------------------------------------------
# How to create an array from existing data: hstack, vstack, hsplit, vsplit
a1 = np.array([[1, 1],[2, 2]])
a2 = np.array([[3, 3],[4, 4]])

print(a1)
# [[1 1]
#  [2 2]]

print(a2)
# [[3 3]
#  [4 4]]

c = np.vstack((a1, a2))
# [[1 1]
#  [2 2]]
# [[3 3]
#  [4 4]]
print(c.shape)    #  (4, 2)

d = np.hstack((a1, a2))
# [[1 1 3 3]
#  [2 2 4 4]]
print(d.shape)    # (2, 4)
#------------------------------------
x = np.arange(1, 25).reshape(2, 12)
print(a)
# [[ 1  2  3  4  5  6  7  8  9 10 11 12]
#  [13 14 15 16 17 18 19 20 21 22 23 24]]

y = np.hsplit(x, 3)    #  split this array into three equally shaped arrays
print(y)
# [array([[ 1,  2,  3,  4],
#        [13, 14, 15, 16]]),
# array([[ 5,  6,  7,  8],
#        [17, 18, 19, 20]]), 
# array([[ 9, 10, 11, 12],
#        [21, 22, 23, 24]])]
#------------------------------------
z = np.hsplit(x, (3, 4))    # split your array after the third and fourth column
print(z)
# [array([[ 1,  2,  3], [13, 14, 15]]), 
# array([[ 4],[16]]), 
# array([[ 5,  6,  7,  8,  9, 10, 11, 12],
#        [17, 18, 19, 20, 21, 22, 23, 24]])]

#------------------------------------
b2 = a.copy()
#------------------------------------
b2[0] = 99
b2[:] = 0     # b2[:, : ] = 0 

#------------------------------------
# Basic Operations
b = np.array([ [1, 1], [2, 2] ])
print(b)
# [[1 1]
#  [2 2]]

print(b.sum(axis = 0))    #  [3 3]

print(b.sum(axis = 1))    #  [2 4]

print(b.min(axis = 0))
print(b.max(axis = 1))
#--------------------------------------------------------------------------------
# Creating matrices (matrix ==> 2D array)
data = np.array([[1, 2], [3, 4], [5, 6]])
# [[1 2]
#  [3 4]
#  [5 6]]

print(data.max())    #  6
print(data.min())    #  1
print(data.sum())    #  12

print(data.max(axis = 0))    #  [5 6]
print(data.max(axis = 1))    # [2 4 6]
#--------------------------------------------------------------------------------
# simplest way to generate random numbers: All you need to do is pass in the number of elements you want it to generate
rng= np.random.default_rng(0)
print(rng)    #  Generator(PCG64)
print(rng.random(3))    #  [0.63696169 0.26978671 0.04097352]
print(rng.random((3, 2)))
# [[0.01652764 0.81327024]
#  [0.91275558 0.60663578]
#  [0.72949656 0.54362499]]

#------------------------------------
# Generating random numbers
# With Generator.integers, you can generate random integers from low (inclusive) to high (exclusive)
# You can set endpoint=True to make the high number inclusive.
print(rng.integers(5, size = (2, 4)))
# [[2 4 1 4]
#  [3 0 1 4]]

print(rng.integers(5, size= (3, 3), endpoint = True))
# [[3 0 4]
#  [4 5 1]
#  [0 5 0]]
#--------------------------------------------------------------------------------
# How to get unique items and counts
a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
unique_values = np.unique(a)
print(unique_values)
# [11 12 13 14 15 16 17 18 19 20]

#------------------------------------
# To get the indices of unique values in a NumPy array (an array of first index positions of unique values in the array), just
# pass the return_index argument in np.unique() as well as your array
unique_values, indices_list = np.unique(a, return_index = True)
# [ 0  2  3  4  5  6  7 12 13 14]

# You can pass the return_counts argument in np.unique() along with your array to get the frequency count of
# unique values in a NumPy array.

unique_values, occurrance_count = np.unique(a, return_counts = True)
print(occurrance_count)
# [3 2 2 2 1 1 1 1 1 1]
#------------------------------------
#  2D array
a_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]])
print(a_2d)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [ 1  2  3  4]]
unique_values = np.unique(a_2d)
print(unique_values)
# [ 1  2  3  4  5  6  7  8  9 10 11 12]

# Note: If the axis argument isn’t passed, your 2D array will be flattened.
# If you want to get the unique rows or columns, make sure to pass the axis argument. To find the unique rows, specify
# axis=0 and for columns, specify axis=1.
unique_rows = np.unique(a_2d, axis = 0)
print(unique_rows)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
#------------------------------------
unique_rows, indices, occuranve_count = np.unique(a_2d, axis = 0, return_counts = True, return_index = True)
print(unique_rows)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
print(indices)    #  [0 1 2]
print(occuranve_count)    #  [2 1 1]
#--------------------------------------------------------------------------------
# Transposing and reshaping a matrix: arr.reshape(), arr.transpose(), arr.T
# reverse an array: np.flip()
# NumPy’s np.flip() function allows you to flip, or reverse, the contents of an array along an axis. When using np.
# flip(), specify the array you would like to reverse and the axis. If you don’t specify the axis, NumPy will reverse the
# contents along all of the axes of your input array.

arr = np.arange(1, 9)    #  [1 2 3 4 5 6 7 8]
reversed_arr= np.flip(arr)
print(reversed_arr)    #  [8 7 6 5 4 3 2 1]
#------------------------------------
# Reversing a 2D array
arr_2d = np.arange(1, 13).reshape(3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

reversed_arr = np.flip(arr_2d)
# [[12 11 10  9]
#  [ 8  7  6  5]
#  [ 4  3  2  1]]

# reverse only the rows
reversed_arr_rows = np.flip(arr_2d, axis = 0) # |
# [[ 9 10 11 12]
#  [ 5  6  7  8]
#  [ 1  2  3  4]]

# reverse only the columns
reversed_arr_columns = np.flip(arr_2d, axis = 1)
# [[ 4  3  2  1]
#  [ 8  7  6  5]
#  [12 11 10  9]]

# You can also reverse the contents of only one column or row. For example, you can reverse the contents of the row at
# index position 1 (the second row):
arr_2d[1] = np.flip(arr_2d[1])
print(arr_2d)
# [[ 1  2  3  4]
#  [ 8  7  6  5]
#  [ 9 10 11 12]]

# You can also reverse the column at index position 1 (the second column):
arr_2d[:, 1] = np.flip(arr_2d[:, 1])
print(arr_2d)
# [[ 1 10  3  4]
#  [ 8  7  6  5]
#  [ 9  2 11 12]]
#--------------------------------------------------------------------------------
# Reshaping and flattening multidimensional arrays
# .flatten(), ravel()
x = np.arange(1, 13).reshape(3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# You can use flatten to flatten your array into a 1D array.
a1 = x.flatten()
# [ 1  2  3  4  5  6  7  8  9 10 11 12]
# When you use flatten, changes to your new array won’t change the parent array.
#------------------------------------
# But when you use ravel, the changes you make to the new array will affect the parent array.
a2 = x.flatten()
# [ 1  2  3  4  5  6  7  8  9 10 11 12]
#--------------------------------------------------------------------------------
# How to access the docstring for more information
# help(), ?, ??  ---> len?, len??
#--------------------------------------------------------------------------------
# How to save and load NumPy objects
# np.save, np.savez, np.savetxt, np.load, np.loadtxt

# The .npy and .npz files store data, shape, dtype, and other information required to reconstruct the ndarray in a way that
# allows the array to be correctly retrieved, even when the file is on another machine with different architecture.

# np.save('file.npy', a)
# np.load('file.npy')
#------------------------------------
# df = pd.read_csv('filename.csv')
# df.to_csv('new_file.csv')
#--------------------------------------------------------------------------------
# Array types and conversions between types
# dtype= np.float16, np.int32
#--------------------------------------------------------------------------------
# Extended Precision: np.longdouble
#--------------------------------------------------------------------------------
# Intrinsic NumPy Array Creation
# arange() will create arrays with regularly incrementing values.
# linspace() will create arrays with a specified number of elements, and spaced equally between the specified beginning and
# end values.
#--------------------------------------------------------------------------------
# Reading Arrays From Disk: h5py
#--------------------------------------------------------------------------------
x = np.arange(10,1,-1)
# [10  9  8  7  6  5  4  3  2]
z = x[np.array([3, -3, 1, 8])]
# [7 4 9 2]
#--------------------------------------------------------------------------------
# Boolean or “mask” index arrays
x = np.arange(1, 25).reshape(4, 6)
# [[ 1  2  3  4  5  6]
#  [ 7  8  9 10 11 12]
#  [13 14 15 16 17 18]
#  [19 20 21 22 23 24]]

b= x>20
x[b]    #  [21 22 23 24]
b[:, 5]    #  [False False False  True]

x[b[:, 5]]    #  [[19 20 21 22 23 24]]
#----------------------------------------------
y = np.arange(35).reshape(5,7)
# [[ 0  1  2  3  4  5  6]
#  [ 7  8  9 10 11 12 13]
#  [14 15 16 17 18 19 20]
#  [21 22 23 24 25 26 27]
#  [28 29 30 31 32 33 34]]
z = y[np.array([0, 2, 4]), 1:3]
# [[ 1  2]
#  [15 16]
#  [29 30]]

z = y[:, 1:3][np.array([0, 2, 4]), :]
# [[ 1  2]
#  [15 16]
#  [29 30]]

b = y > 20
# [[False False False False False False False]
#  [False False False False False False False]
#  [False False False False False False False]
#  [ True  True  True  True  True  True  True]
#  [ True  True  True  True  True  True  True]]
z = y[b[:, 5], 1:3]
# [[22 23]
#  [29 30]]
#--------------------------------------------------------------------------------
# Structural indexing tools
y.shape    # (5, 7)
y[:, np.newaxis, :].shape    #  (5, 1, 7)
#--------------------------------------------------------------------------------
x = np.arange(5)   #  [0 1 2 3 4]
x.shape    #  (5,)
z = x[:, np.newaxis]
print(z.shape)    #  (5, 1)
print(z)
# [[0]
#  [1]
#  [2]
#  [3]
#  [4]]
#----------------------------------------------
z2 = x[:,np.newaxis] + x[np.newaxis,:]
print(z2.shape)    #  (5, 5)
print(z2)
# [[0 1 2 3 4]
#  [1 2 3 4 5]
#  [2 3 4 5 6]
#  [3 4 5 6 7]
#  [4 5 6 7 8]]
#----------------------------------------------
z = np.arange(81).reshape(3, 3, 3, 3)
# [[[[ 0  1  2]
#    [ 3  4  5]
#    [ 6  7  8]]

#   [[ 9 10 11]
#    [12 13 14]
#    [15 16 17]]

#   [[18 19 20]
#    [21 22 23]
#    [24 25 26]]]


#  [[[27 28 29]
#    [30 31 32]
#    [33 34 35]]

#   [[36 37 38]
#    [39 40 41]
#    [42 43 44]]

#   [[45 46 47]
#    [48 49 50]
#    [51 52 53]]]


#  [[[54 55 56]
#    [57 58 59]
#    [60 61 62]]

#   [[63 64 65]
#    [66 67 68]
#    [69 70 71]]

#   [[72 73 74]
#    [75 76 77]
#    [78 79 80]]]]
#----------------------------------------------
# Note: d1 and d2 are equivalent
d1 = z[1,..., 2]
# [[29 32 35]
#  [38 41 44]
#  [47 50 53]]


d2 = z[1,:,:,2]
# [[29 32 35]
#  [38 41 44]
#  [47 50 53]]
#-------------------------------------------------------------------------------------
# Assigning values to indexed arrays
x = np.arange(10)    #  [0 1 2 3 4 5 6 7 8 9]
x[2:7] = 1
print(x)    #  [0 1 1 1 1 1 1 7 8 9]
#----------------------------------------------
x[2:7] = np.arange(5)
print(x)    #  [0 1 0 1 2 3 4 7 8 9]
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
# Tutorial: Linear algebra on n-dimensional arrays
from scipy import misc
import matplotlib.pyplot as plt

img = misc.face()
print(type(img))
plt.imshow(img)
plt.show()
print(img.shape)    #  (768, 1024, 3)
print(img.ndim)    # 3

img[:, :, 0]    # red axis
print(img[:, :, 0].shape)    #  (768, 1024)
#-------------------------------------------------------------------------------------
# Since we are going to perform linear algebra operations on this data, it might be more interesting to have real numbers
# between 0 and 1 in each entry of the matrices to represent the RGB values.
img_array = img / 255
print(img_array.max(), img_array.min())    #  1.0 0.0

print(img_array.dtype)    #  float64

# Note that we can assign each color channel to a separate matrix using the slice syntax:
red_array = img_array[:, :, 0]
green_array = img_array[:, :, 1]
blue_array = img_array[:, :, 2]
#-------------------------------------------------------------------------------------
# Operations on an axis
from numpy import linalg

# In order to extract information from a given matrix, we can use the SVD to obtain 3 arrays which can be multiplied to
# obtain the original matrix. From the theory of linear algebra, given a matrix A, the following product can be computed:

# UΣV^T = A

# where U and V^T are square and Σ is the same size as A. Σ is a diagonal matrix and contains the singular values of
# A, organized from largest to smallest. These values are always non-negative and can be used as an indicator of the
# “importance” of some features represented by the matrix A.
# Let’s see how this works in practice with just one matrix first. Note that according to colorimetry, it is possible to obtain
# a fairly reasonable grayscale version of our color image if we apply the formula

# Y = 0.2126R + 0.7152G + 0.0722B

# where Y is the array representing the grayscale image, and R,G and B are the red, green and blue channel arrays we had
# originally. Notice we can use the @ operator (the matrix multiplication operator for NumPy arrays, see numpy.matmul)
# for this:

img_gray = img_array @ [0.2126, 0.7152, 0.0722]
print(img_gray.shape)    #  (768, 1024)
plt.imshow(img_gray, cmap = 'gray')
plt.show()


U, s, Vt = linalg.svd(img_gray)

print(U.shape, s.shape, Vt.shape)    #  (768, 768) (768,) (1024, 1024)

"""
s @ Vt
Traceback (most recent call last):
...
ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0,
with gufunc signature (n?,k),(k,m?)->(n?,m?) (size 1024 is different from
768)

This happens because having a one-dimensional array for s, in this case, is much more
economic in practice than building a diagonal matrix with the same data. To reconstruct the original matrix, we can
rebuild the diagonal matrix Σ with the elements of s in its diagonal and with the appropriate dimensions for multiplying:
in our case, Σ should be 768x1024 since U is 768x768 and Vt is 1024x1024.
"""

Sigma = np.zeros((768, 1024))
for i in range(768):
   Sigma[i, i]= s[i]

# Now, we want to check if the reconstructed U @ Sigma @ Vt is close to the original img_gray matrix.

"""Approximation
The linalg module includes a norm function, which computes the norm of a vector or matrix represented in a NumPy
array. For example, from the SVD explanation above, we would expect the norm of the difference between img_gray
and the reconstructed SVD product to be small. As expected, you should see something like"""

linalg.norm(img_gray - U @ Sigma @ Vt)    #  1.3926466851808837e-12

"""We could also have used the numpy.allclose function to make sure the reconstructed product is, in fact, close to our
original matrix (the difference between the two arrays is small):"""

np.allclose(img_gray, U @ Sigma @ Vt)
# True

plt.plot(s)
plt.show()

"""In the graph, we can see that although we have 768 singular values in s, most of those (after the 150th entry or so) are
pretty small. So it might make sense to use only the information related to the first (say, 50) singular values to build a
more economical approximation to our image.
The idea is to consider all but the first k singular values in Sigma (which are the same as in s) as zeros, keeping U and
Vt intact, and computing the product of these matrices as the approximation.
For example, if we choose"""

k= 10
approx = U @ Sigma[:, :k] @ Vt[:k, :]
plt.imshow(approx, cmap="gray")
plt.show()

#-------------------------------------------------------------------------------------
# Applying to all colors
"""Now we want to do the same kind of operation, but to all three colors. Our first instinct might be to repeat the same
operation we did above to each color matrix individually. However, NumPy’s broadcasting takes care of this for us.
If our array has more than two dimensions, then the SVD can be applied to all axes at once. However, the linear algebra
functions in NumPy expect to see an array of the form (N, M, M), where the first axis represents the number of
matrices. In our case,"""

img_array.shape
# (768, 1024, 3)

"""so we need to permutate the axis on this array to get a shape like (3, 768, 1024). Fortunately, the numpy.
transpose function can do that for us:"""

np.transpose(x, axes=(i, j, k))

"""indicates that the axis will be reordered such that the final shape of the transposed array will be reordered according to
the indices (i, j, k)."""

img_array_transposed = np.transpose(img_array, (2, 0, 1))
img_array_transposed.shape
# (3, 768, 1024)

# Now we are ready to apply the SVD:
U, s, Vt = linalg.svd(img_array_transposed)
# Finally, to obtain the full approximated image, we need to reassemble these matrices into the approximation. Now, note
# that

U.shape, s.shape, Vt.shape
# ((3, 768, 768), (3, 768), (3, 1024, 1024))
# To build the final approximation matrix, we must understand how multiplication across different axes works.
#-------------------------------------------------------------------------------------
"""Products with n-dimensional arrays
If you have worked before with only one- or two-dimensional arrays in NumPy, you might use numpy.dot and numpy.
matmul (or the @ operator) interchangeably. However, for n-dimensional arrays, they work in very different ways. For
more details, check the documentation numpy.matmul.
Now, to build our approximation, we first need to make sure that our singular values are ready for multiplication, so we
build our Sigma matrix similarly to what we did before. The Sigma array must have dimensions (3, 768, 1024).
In order to add the singular values to the diagonal of Sigma, we will use the fill_diagonal function from NumPy,
using each of the 3 rows in s as the diagonal for each of the 3 matrices in Sigma:"""


Sigma = np.zeros((3, 768, 1024))
for j in range(3):
   np.fill_diagonal(Sigma[j, :, :], s[j, :])
   
# Now, if we wish to rebuild the full SVD (with no approximation), we can do
reconstructed = U @ Sigma @ Vt
# Note that
reconstructed.shape
# (3, 768, 1024)

plt.imshow(np.transpose(reconstructed, (1, 2, 0)))
plt.show()

"""should give you an image indistinguishable from the original one (although we may introduce floating point errors for this
reconstruction). In fact, you might see a warning message saying “Clipping input data to the valid range for imshow with
RGB data ([0..1] for floats or [0..255] for integers).” This is expected from the manipulation we just did on the original
image.
Now, to do the approximation, we must choose only the first k singular values for each color channel. This can be done
using the following syntax:"""

approx_img = U @ Sigma[..., :k] @ Vt[..., :k, :]


"""You can see that we have selected only the first k components of the last axis for Sigma (this means that we have used
only the first k columns of each of the three matrices in the stack), and that we have selected only the first k components
in the second-to-last axis of Vt (this means we have selected only the first k rows from every matrix in the stack Vt and
all columns). If you are unfamiliar with the ellipsis syntax, it is a placeholder for other axes."""

approx_img.shape
# (3, 768, 1024)

"""which is not the right shape for showing the image. Finally, reordering the axes back to our original shape of (768,
1024, 3), we can see our approximation:"""

plt.imshow(np.transpose(approx_img, (1, 2, 0)))
plt.show()