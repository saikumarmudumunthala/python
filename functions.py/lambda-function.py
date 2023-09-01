list = [5,7,22,97,54,62,77,23,73,61]
final_list = list(filter(lambda x:(x%2 !=0),list))
print(final_list)


# lambda function with map

list = [5,7,22,97,54,62,77,23,73,61]
final_list = list(map(lambda x:x*2,list))
print(final_list)