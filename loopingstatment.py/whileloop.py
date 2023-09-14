# While loop in python
# looping statment are used to reapeat a task multiple times

i = 1
while i<=10:
    print(i)
    i=i+1

#create a table 
i = 1
n = 2
while i<=10:
    print(n, "*",i,"=",n*i)
    i=i+1

#example by using List

l1 = [1,2,3,4,5]
i=0
while i < len(l1):
    l1[i]=l1[i]+100
    i=i+1
print(l1)


# for i in range(0,5): 
#     for j in range(0,5):
#         print("*",end=" ")
#     print("")

# for i in range(1,5):
#     for j in range(0,i-1):
#         print("*",end=" ")
#     print("")    


n = 5
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    print(" ")    


