# Set is an unordered and unindexed collection of elements enclosed with {}
# duplicates are not allowed in set 

a1={"sai",True,2,"kumar",False}
a1.add("hello")
print(a1)

# update multiple elements
a1={"sai",True,2,"kumar",False}
a1.update([10,20,30])
print(a1)

# remove an element
a2={"sai",True,2,"kumar","b",False}
a2.remove("b")
print(a2)

#union of two sets
a1 = {1,2,3}
a2 = {"a","b","c"}
print(a1.union(a2))

# Intersection
s1 = {1,2,3,4,5,}
s2 = {4,5,6,7}
print(s1.intersection(s2))
