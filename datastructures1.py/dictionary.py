# Dictionary is an unordered collection of key value/pair enclosed with {}
#it is an mutable

fruits = {"apple":10,"orange":20,"banana":30}
print(fruits.keys())

#example 1 Extracting values
fruits = {"apple":10,"orange":20,"banana":30}
print(fruits.values())

#adding new element
fruits = {"apple":10,"orange":20,"banana":30}
fruits["mango"]=40
print(fruits)

#changing an existing elements
fruits = {"apple":10,"orange":20,"banana":30}
fruits["apple"]=100
print(fruits)

#update one dictionarys element with another
fruits1 = {"apple":10,"orange":20,"banana":30}
fruits2 = {"cherry":40,"guava":60}
fruits1.update(fruits2)
print(fruits1)

#pop method
fruits = {"apple":10,"orange":20,"banana":30}
fruits.pop("orange")
print(fruits)

