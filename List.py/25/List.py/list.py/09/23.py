# List = used to store multiple iteams in a single variable.

food = ["apple","mango","grape","berry"]
food[0] = "kivi"
for i in food:
    print(i)
    
# .append() > it is used to add a value in last at list.


food1 = ["apple","mango","burger","cola"]
food1.append("icecream")
for i in food1:
    print(i)    

# .remove() > it is us ed to remove the values in the list.

food2 =  ["apple","mango","burger","cola"]
food2.remove("cola")
for i in food2:
    print(i)

# .pop() > it is used to remove the last value in list.
food3 = ["apple","mango","burger","cola"]
food3.pop() 
for i in food3:
    print(i)


# .insert()
food4 = ["apple","mango","grape","juice"]
food4.insert(0,"sushi")
for i in food4:
    print(i)

#  sort() > it will sort by alphabetical order.

food5 = ["mango","grape","cake","pineapple"]
food5.sort()
for i in food5:
    print(i)

# clear()

food6 = ["mango","grape","cake","pineapple"]
food6.clear()
for i in food6:
    print(i)