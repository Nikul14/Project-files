import numpy as np
# arr = np.array([1])#0 ndim
# print(arr)
# print(type(arr))
# print(arr.ndim)



# 1dimention array
# arr = np.array([1,2,4,5,6,7,8,9])
# print(arr[0::])#slicing
# print('1st element of 1d is: ',arr[0]) it is indexing
# print('3rd element of 1d is:',arr[2])
# print(arr)
# print(type(arr))
# print(arr.ndim)



#2dimention array
# arr = np.array([[1,2,3],[4,5,6]])
# print(arr[0,0::],arr[1,0::])#slicing
# # print(arr[0,2],arr[1,2])
# print(arr)
# print(type(arr))
# print(arr.ndim)



# 3dimention array
# arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[11,12,13]]])
# print(arr[0,0,0::],arr[0,1,0::],arr[1,0,0::],arr[1,1,0::])
# print(arr[0,0,2],arr[0,1,2],arr[1,1,2],arr[1,0,2])
# print(arr)
# print(type(arr))
# print(arr.ndim)




# data type
# arr = np.array([1,2,3,4,5,6])
# print(arr)
# print(arr.dtype)


# arr = np.array(['apple','banan'])
# print(arr)
# print(arr.dtype)

# arr = np.array(['dog','cat','kite','tree'])
# print(arr)
# print(arr.dtype)

# data tpe define 
# arr = np.array([1,2,3,4,5,65,6,7,2],dtype='str')
# print(arr)
# print(arr.dtype)

# arr = np.array([1,2,3,4,5,65,6,7,2],dtype= 'i4')
# print(arr)
# print(arr.dtype)



# numpy.shape it means number of elements in that dimention
# arr = np.array([1,2,3,4,5])
# print(arr)
# print(arr.shape)1dimention

# 2 dimention
# arr = np.array([[1,2,3,4,5],[6,7,8,9,0]])
# print(arr)
# print(arr.shapae)

# 3 dimention
# arr = np.array([[[1,2,3,4,5],[3,4,5,6,7]],[[1,2,3,4,5],['a','b','c','d','e']]])
# arr1=np.array_split(arr,4)
# print(arr1)
# print(arr.shape)



# Numpy joining via concatenate
# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# arr = np.concat((arr1,arr2) )
# print(arr)

# 2dimention
# arr1 = np.array([[1,2],[4,5]])
# arr2 = np.array([[7,6],[8,9]])
# arr = np.concat((arr1,arr2),axis=1)
# print(arr)
# joining numpy
# arr1 = np.array([[1,2],[4,5]])
# arr2 = np.array([[7,6],[8,9]])
# arr = np.concat((arr1,arr2),axis=0)
# print(arr)



# how to split array 
# arr1 = np.array([1,3,4,5,6,7,8,9])
# arr=np.array_split(arr1,4)
# print(arr)



# ravel/flatten ; simply convert from multidimention to 1 dimention array 
# m = np.array([[[1,2,34],[5,6,7]],[[8,9,0],[3,5,6]]])
# print(m)
# n= m.ravel()
# print(n)



# unique value
# k = np.array([2,3,4,5,6,7,8,8,8,899,6,6,7,8,9,0])
# print(k)
# p= np.unique(k,return_index=True)
# print(f'print distinct values only:',p)


# delete
# m=np.array([1,2,3,4,4])
# n=np.delete(m,1)
# print(n)
# multidimention delete
# a=np.array([[[1,2,7],[4,8,5]],[[1,2,3],[1,2,3]]])
# b=np.delete(a,1,axis=0 )
# print(b)