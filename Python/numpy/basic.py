import numpy as np

# creating array
arr = np.array([1, 2, 3, 4, 5])

print(arr)  # print array
print(type(arr))  # print type :ndarray type
print(np.__version__)  # print version of numpy

# dimension of array

# 0-D array
arr0 = np.array(43)
print("\n", arr0)
print(arr0.ndim)  # print number of dimension

# 1-D array
arr1 = np.array([1, 2, 3, 4, 5])
print("\n", arr1)
print(arr1.ndim)  # print number of dimension
print(arr1[0])  # 1st element of array
print(arr1[1])  # 2nd element of array
print(arr1[-1])  # last element of array
print(arr1.dtype)  # data type
print(arr1.shape)  # print shape of array

# 2-D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n", arr2)
print(arr2.ndim)  # print number of dimension
print(arr2[0, 1])  # 2nd element on 1st row
print(arr2[1, -1])  # last element of 2nd row
print(arr2.shape)  # print shape of array
for x in arr2:  # Iterating
    for y in x:
        print(y)

# 3-D array
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("\n", arr3)
print(arr3.ndim)  # print number of dimension
print(arr3[0, 1, 2])
print(arr3.shape)  # print shape of array
for x in arr3:  # Iterating
    for y in x:
        for z in y:
            print(z)

for x in np.nditer(arr3):  # Iterating using nditer func
    print(x)

# higher dimension arrays
arr5 = np.array([1, 2, 3, 4], ndmin=5)
print("\n", arr5)
print(arr5.ndim)  # print number of dimension

# Slicing array
# ? [start:end] or [start:end:step]
slice_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("\n", slice_array[1:5])  # slicing from index 1 to 5
print("\n", slice_array[5:])  # slicing from index 5 to last
print("\n", slice_array[:5])  # slicing from beginning to index 5
print(
    "\n", slice_array[-3:-1]
)  # Slice from the index 3 from the end to index 1 from the end
print("\n", slice_array[1:5:2])  # return every other element from index 1 to index 5
print("\n", slice_array[::2])  # return every other element from entire array

# slicing 2d array
slice_2d_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(
    slice_2d_array[1, 1:4]
)  # From the second element, slice elements from index 1 to index 4 (not included)
print(
    slice_2d_array[0:2, 1:4]
)  # From both elements, slice index 1 to index 4 (not included), this will return a 2-D array

# create array with default data type

type_array = np.array([1, 2, 3, 4], dtype="S")  # creating array with datatype string
print("\n", type_array)
print(type_array.dtype)  # print datatype

i4_array = np.array([1, 2, 3, 4], dtype="i4")  # create array with data type 4 bytes int
print("\n", i4_array)
print(i4_array.dtype)  # print datatype

# converting datatype on existing array
first_arr = np.array([1.1, 2.1, 3.1])
newarr = first_arr.astype(
    "i"
)  # hange data type from float to integer by using 'i' as parameter value
print("\n", newarr)
print(newarr.dtype)  # print datatype

"""
can be used like 
- astype(int)
- astype(bool)
"""

# copy
# The copy SHOULD NOT be affected by the changes made to the original array.
x = arr.copy()  # make copy of 'arr' array
print("\n", x)

# view
# The view SHOULD be affected by the changes made to the original array.
y = arr.view()
y[0] = 23
print("\n", y)
print(
    arr.base
)  # Print the value of the base attribute to check if an array owns it's data or not
print(
    y.base
)  # Print the value of the base attribute to check if an array owns it's data or not

# array reshaping
arr1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr2d = arr1d.reshape(
    4, 3
)  # The outermost dimension will have 4 arrays, each with 3 elements
print("\n", arr1d)
print(newarr2d)

newarr3d = arr1d.reshape(2, 3, 2)
print(newarr3d)

# Join array

arr1djoin1 = np.array([1, 2, 3])
arr1djoin2 = np.array([4, 5, 6])

arr_1d_result = np.concatenate((arr1djoin1, arr1djoin2))
print("1D array join", arr_1d_result)

arr2djoin1 = np.array([[1, 2], [3, 4]])
arr2djoin2 = np.array([[5, 6], [7, 8]])

arr_2d_result = np.concatenate((arr2djoin1, arr2djoin2), axis=1)
print("2D array join", arr_2d_result)

# Join array using stack() func

arr_stack_result = np.stack((arr1djoin1, arr1djoin2), axis=1)
print("join array using stack", arr_stack_result)

arr_hstack_result = np.hstack((arr1djoin1, arr1djoin2))
print("join array using hstack", arr_hstack_result)

arr_vstack_result = np.vstack((arr1djoin1, arr1djoin2))
print("join array using vstack", arr_vstack_result)

arr_dstack_result = np.dstack((arr1djoin1, arr1djoin2))
print("join array using dstack", arr_dstack_result)

# splitting array

split_1d_arr = np.array([1, 2, 3, 4, 5, 6])
split_3_new_arr = np.array_split(split_1d_arr, 3)
print("new split into 3 array", split_3_new_arr)

split_4_new_arr = np.array_split(split_1d_arr, 4)
print("new split into 4 array", split_4_new_arr)

# Searching array

val4 = np.where(arr1 == 4)
print("value 4 in arr1", val4)

sch_val4 = np.searchsorted(arr1, 4)
print("search sorted arr1", sch_val4)

# Sort array

unsorted_arr = np.array([5, 9, 0, 3, 4])
print("sorted array", np.sort(unsorted_arr))
