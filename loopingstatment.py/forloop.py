# for loop is used to iterate over a sequence (tuple,list,dictionary...)

l1 = ["apple","mango","grape","cherry"]
for ele in l1:
    print(ele)
    print("sachin")


l1 = ["apple","mango","grape","cherry"]
l2 = ["chair","book","phone"]
for i in l1:
    for j in l2:
        print(i,j)
        


for i in range(10):
    print(i)   

l3 = ["saikumar","mounika","bolla"]
for i in l3:
    print(i)         


E1 = ["number","id","email","role"]
for i in E1:
    print(i)    

S1 = ["roll1","branch","college","id"]
S2 = ["exam","lab","records"]
for i in S1:
    for j in S2:
        print(i,j)


#                    i
fruits1 = ["apple","mango","banana","grape","watermilon"]
#           j
fruits2 = [22,33,74]

for i in fruits1:

    for j in fruits2:

        print(i,j)


# 1.TASK
for i in range(1,101):
    print(i)
 
# 2,TASK
num = 5
for i in range(1,11):
    print(num,'*',i,'=',num*i)

# 3,TASK

n = 5
for i in range(0, n):
	for j in range(0, i+1):
		print("*",end=" ")
	print()



for i in range(5):
    for j in range(i,n):
        print("",end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i,n):
        print("",end=" ")
    print()
    
n=10
for i in range(10):
    for j in range(i,n):
        print("",end=" ") 
    for j in range(i):
        print("*", end=" ")
    for j in range(i,n):
        print("",end=" ")
    print()               



for i in range(65,70):
    k=i
    for j in range(65,i+1):
        print(chr(k),end=" ")
        k=k+1
    print( )    