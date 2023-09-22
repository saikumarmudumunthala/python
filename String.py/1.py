# String Methods
# to find the length of characters  >>> len()
name = "saikumar"
print(len(name))

names = "gouda"
print(len(names))


# Find Method
# to find the character place
name1 = "saikumar"
print(name1.find("k"))

name2 = "sachin"
print(name2.find("i"))

# Capitalize() but only 1st word will be capital

name2 = "saikumar"
print(name2.capitalize())

name2 = "sachin"
print(name2.capitalize())

# UpperCase() it is used to all capitals in print statement

name3 = "saikumar"
print(name3.upper())

# Lower() it is used to all lower in print statement

name4 = "SAIKUMAR"
print(name4.lower())

# Isdigit() it is used to string is digit or not 
# down 1st example is Flase bcz it is in words.

name5 = "saikumar"
print(name5.isdigit())
# down 2nd example is True bcz it is in numeric.

name6 = "404"
print(name6.isdigit())

# isalpha() is used to only alphabetical TRUE or FALSE

name7 = "sai kumar"
print(name7.isalpha())

# Count() method used to count how many repeated letters

name8 = "saisai"
print(name8.count("s"))

# Replace() is used to replace the one character to other character

name9 = "saikumar"
print(name9.replace("saikumar","tiger"))

# multiple
name10 = "saikumar"
print(name10*5)

x = 1 
y = 3.6
z = "sai"
# z = int("sai")
print(int("sai"*3))