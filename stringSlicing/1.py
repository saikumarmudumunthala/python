# Slicing = create a substring by extracting elements from another srting

# indexing[] or slice()
# [start:stop:step]

# start
name = "saikumar"
print(name[0])

#stop
name1 = "saikumar"
print(name1[0:8])

# step
name2 = "saikumar"
print(name2[::3])

#Reversed()
name3 = "saikumar"
reversed_name3 = name3[::-1] 
print(reversed_name3)

# website = "http://wikipedia.com"
# slice = slice(7,-4)
# print(website[slice])

name = "MUDUMUNTHALA SAI KUMAR YADAV"
slice = slice(13,-6)
print(name[slice])