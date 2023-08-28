tuple = (1,"sai",True)
print(tuple)

#example 1

tuple1 = (1,"a",True,2,"b",False)
tuple1[-1]
print(tuple1)

#example 2

tuple2 = (1,"a",True,2,"b",False)
tuple2[1:4]
print(tuple2)

#finding length of tuple
tuple3 = (1,"a",True,2,"b",False)
len(tuple3)
print(tuple3)

#concatenating tuple
tuple1 = (1,2,3)
tuple2 = (4,5,6)

print(tuple1+tuple2)

#Repeating tuple 
tuple1 = ("sai",404)
temp=tuple1*3
print(temp)

#Repeating & concatenation
tup1 = ("sai",404)
tup2 = (2,3,4,5)
temp=tup1*3+tup2
print(temp)

#min value & max 
tuple = (1,2,3,4,5)
minimum=min(tuple)
print(minimum)