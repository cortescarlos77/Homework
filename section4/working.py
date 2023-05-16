# score = float(input("Please enter your grade: "))

# txt = "\nYour grade in this course is: "

# if score >= 90:
#     print(txt, "A")
# elif score >= 80:
#     print(txt, "B")
# elif score >= 70:
#     print(txt, "C")
# elif score >= 60:
#     print(txt, "D")
# else:
#     print(txt, "F... you are failing")

# print("\nDone.")

# name1 = str(input("Person 1- please enter your name: "))
# age1 = int(input(f"{name1}- please enter your age: "))
# print(f"{name1} your age is {age1}.")

# name2 = str(input("Person 2- please enter your name: "))
# age2 = int(input(f"{name2}- please enter your age: "))
# print(f"{name2} your age is {age2}.")

# name3 = str(input("Person 3- please enter your name: "))
# age3 = int(input(f"{name3}- please enter your age: "))
# print(f"{name3} your age is {age3}.")

# if age1 > age2 and age1 > age3:
#     print(f"{name1} is the oldest")
# elif  
# # age2 = int(input("Person 2- Please enter your age: "))
# # age3 = int(input("Person 3- Please enter your age: "))

# myList = [23, 45, 12, 10, 25]
# # print(len(myList))
# sum = myList[0]
# b = 1

# while b < len(myList):
#     sum = sum + myList[b]
#     b = b + 1
#     if b == len(myList):
#          print(sum)

# nums = [12,3,56,67,89,90]
# count = 0

# for x in nums:
#     count = count + 1
# else:
#     print("in ths liste there are the following number of items: ", count)

# nums.pop(2)
# print(nums)

# import numpy as np
# # pyArray = np.arange(1000)   # allocate a NumPy array
# # print("Memory size of NumPy Array ...", pyArray.size*pyArray.itemsize)
# a1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# a2 = np.array([[1,2,3], [4,5,6]])

# print("a1... \n", a1)
# print("a2... \n", a2)

# # creates arrey [01234]
# b = np.arange(5)
# print("b... ",b)

# # creates incremented intervals array between 2-9 [2468]
# f = np.arange(2,9,2)
# print("f... ", f)

# newShape = a1.reshape(3,2,2)
# print("this is the new shape...\n",newShape)

import numpy as np

# array1 = np.array([3,0,9,12,6])
# print(np.sort(array1))

# array2 = np.array([[3,2,4],[5,0,1]])
# print(np.sort(array2))

# array3 = np.array(["b","c","a"])
# print(np.sort(array3))

# arrayX = np.array([[2,1],[3,4]])
# arrayY = np.array([[5,6]])
# arrayZ = np.array([[8,7],[7,9],[12,11]])

# arrayC = np.concatenate((arrayX,arrayY,arrayZ), axis = 0)
# print(arrayC)

# arrayC_sort = np.sort(arrayC)
# print(arrayC_sort)

# newShape = arrayC_sort.reshape(3,-1)
# print("Now\n", newShape)


# tt = ([ [ [0, 1, 2, 3], [4, 5, 6, 7] ],
#         [ [10, 11, 12, 13], [14, 15, 16, 17] ],
#         [[20, 21, 22, 23], [24, 25, 26, 27] ] ])

# a,b,c = tt
# print(a)
# print(b)
# print(c)
# print(type(a))

# a0,a1 = a
# print(a0)
# print(a1)
# print(type(a0))

# example = ([ [ [0, 1, 2, 3], [14, 15, 16, 17] ],
#         [ [20, 21, 22, 23], [34, 35, 36, 37] ],
#         [[40 ,41 ,42, 43], [54, 55, 56, 57] ] ])

# [[[a,b,c,d], [e,f,g,h]],
#  [[i,j,k,l], [m,n,o,p]],
#  [[q,r,s,t], [u,v,w,x]]] = example

#  print(f"first group: {a}, ")

array2 = np.array([[1,2,3],[3,4,5], [4,5,6]])
print(array2[1:])