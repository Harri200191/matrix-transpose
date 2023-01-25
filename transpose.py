import numpy as np #import numpy

matrix = [] 

for x in range(9):
    matrix.append(int(input("Enter value: "))) #created empty list and enter 9 values in it

arr = np.array(matrix, ndmin = 1) #convert list into array
newarr = arr.reshape(3,3) #create a 3x3 2D array
x = newarr.copy() #create copy of 3x3 array

for row in range(3):
    for col in range(3):
        if row != col:
            x[row][col] = newarr[col][row] #if row is not = column then swap row and column elements

#DISPLAY ALL RELEVANT INFO
print("Following is the matrix you entered:")
print("---------------------------------------")
print(newarr)
print("---------------------------------------")

print("Following is the transposed matrix:")
print("---------------------------------------")
print(x)
print("---------------------------------------")
            

            



