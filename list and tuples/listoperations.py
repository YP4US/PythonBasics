x=[4,5,7,8,2,1,5,9,6,4,3]
print("original list value",x)

#append list(add element)
x.append(33)
print("appended:",x)

#insert element at specific index
x.insert(1,22)
print("22 inserted at index 1:",x)

#remove value
x.remove(2)#first element in list that has value 2
print("first value of 2 is removed:",x)

#or

x.remove(x[6])#specify index value
print("data removed at index 6:",x)

#get part of list
print("pirnting value from index 2 to 6:",x[2:6])  

#get index value of specified data
print("index of data 8 in list is:",x.index(8))

#count number of specified data present in list
print("number of 5 present in list is:",x.count(5))

#sort the list
x.sort()
print("sorted list is:",x)

#multi dimention list
y=[
  [2,3],
  [5,6],
  [7,8]
  ]
print("value at index[2,0] is: ",y[2][0])
