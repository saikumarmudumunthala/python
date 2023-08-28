s1 = [1, "sai",3.14,True,404]
print(s1)

#extracting individuals elements
s2 = [1,"a",2,"b",3,"c"]
temp=s2[1]
print(temp)

#example 2
s2 = [1,"a",2,"b",3,"c"]
add=s2[2:5]
print(add)

# changing the element at 0th index
s1 = [1,"a",2,"b",3,"c"]
add=s1[0]=100
print(s1)

# .append
s2 = [1,"a",2,"b",3,"c"]
s2.append("saikumar")
print(s2)

# popping the last element

s3 = [1,"a",2,"b",3,"c"]
s3.pop()
print(s3)

# reversing element
s4 = [1,"a",2,"b",3,"c"]
s4.reverse()
print(s4)

# inserting elements at a specified index
s5 = [1,"a",2,"b",3,"c"]
s5.insert(1,"saikumar")
print(s5)

# sorting elements >> it means convert in to A-Z order

s6 = ["mango","apple","grape","guava"]
s6.sort()
print(s6)

# concatenating list 

s1 = [1,2,3,4]
s2 = ["a","b","c","d"]
#s1+s2
print(s1+s2)

# repating elements 
s1 = [1,"a",True]
#s1*3
print(s1*3)