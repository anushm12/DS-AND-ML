import numpy as np


list= [1,2,3,4]
arr= np.array(list)

print(arr)
print(list)

# arange(start,stop,step)
print(np.arange(0,100,9))
# arange(stop) default is 0
arr= np.arange(25)

# array of zeros 
print(np.zeros((2,5)))
print(np.zeros(4))

# prints array of ones
print(np.ones(5))
print(np.ones((2,5)))

#linspace(start,stop,step)
print(np.linspace(0,10,5))
print(np.linspace(4,13))

#identity matrix
print(np.eye(3))

#random number matrix +ve
x=np.random.rand(5,3)
print(x)
#random number matrix +-
print(np.random.randn(2))
print(np.random.randn(4,4))
#random number matrix integer
print(np.random.randint(0,100,(5,5)))
rarr = np.random.randint(0,25,10)
print(rarr)

#reshape(cols,rows)
print(arr.reshape(5,5))
print(arr.reshape(1,25))

#finding max and min
print(rarr.max())
print(rarr.min())
#finding pos of max and min
print(rarr.argmax())
print(rarr.argmin())

#shape of the matrix (cols,rows)
print(arr.shape)
#datatype of matrix
print(arr.dtype)
print(rarr.dtype)
print(x.dtype)

#Moving about an array
arr= np.arange(0,10)
print(arr)
print(arr[4:9])
print(arr[4:])
arr[0:5]=100
print(arr[0:5])


#does not initalize values but takes up the place where arr has stored its values,if arr changes sarr also changes and vice versa
sarr=arr[:6]
print(sarr)
sarr[:]=99
print(sarr[:])
print(sarr)
print(arr)

#copying the array
arrc= arr.copy()
print(arrc)
arr[:]=99
print(arr[:])
print(arr)
print(arrc)

#initalizing and traversing as 2d array
twod =np.array([[0,5,10],[15,20,25],[30,35,40]])
print(twod)
print(twod[1][2])
print(twod[1])
print(twod[2][1])
print(twod[2,1])
print(twod[0:,2:])

#checking boolean condition for if arr has values greter than 5
arr= np.arange(0.10)
bool_arr=arr>5
print(arr[bool_arr])
print(arr[arr>5])
print(arr[arr<3])

#creating a 2d array using arange and tranforming it using reshape
arr2d = np.arange(0,50).reshape(5,10)
print(arr2d)
print(arr2d[0:,4:7])
print(arr2d[4])

#using arithemetic and trignometric operations in the arrays
arr=np.arange(11)
print(arr)
print(arr +arr)
print(arr-arr)
print(arr*arr)
print(arr/arr)
print(arr-50)
print(arr*21)
print(1/arr)
print(arr**2)
print(np.sqrt(arr))
print(np.exp(arr))
print(np.sin(arr))
print(np.log(arr))
print(np.cos(arr))
