# Add two numbers in python
numA = 5
numB = 8
result=(numA+numB)
print(result) 

# Subtract two numbers

numA = 9
numB = 15
result=(numA-numB)
print(result)

#Product of two numbers

numA = 8
numB = 12
result=(numA*numB)
print(result)

# Divide two numbers
numA = 5
numB = 14
result=(numA/numB)
print(result)

# Average of numbers
numA = 10
numB = 20
avg=(numA+numB)/2
print(avg)

def per(apple,mango):
    result=apple+mango
    answer=result/2
    print(answer)
per(10,20)

#Square of a number

def sum(num1):
    result=(num1*num1)
    print(result)
sum(2)   


# Cube root

def sum(num1):
    result=(num1**num1)
    print(result)
sum(5)    

#Swapping 
a = 30
b = 27
#a,b = b,a
sai=a
a=b
b=sai
print(a,b)

# Simple interest

#Simple_Interest(P,R,T):
P = 100000
R = 3
T = 12
Simple_Interest=(P*R*T)/100
print(Simple_Interest)      
 
# convert km to miles 
# miles = 0.62
km = 15
miles = 0.62
cal = km*miles
print(cal)

# Finding square root
import math
print(math.sqrt(4))

byte = 5
kb = 1024
cal = byte/kb
print(cal)

bytes = 6
mb = 1024*1024
cal = byte/mb
print(cal)

bytes = 4
gb = 1024*1024*1024
cal = byte/gb
print(cal)

bytes = 9
tb = 1024*1024*1024*1024
cal = byte/tb
print(cal) 

# convert bytes to kb on python
bytes = 2
kb = 1024
cal = byte/kb
print(cal)

# Convert bytes to megabytes 
bytes = 4
mb = 1024*1024
cal = bytes/mb
print(cal)

# convert bytes to TB
bytes = 7
tb = 1024*1024*1024*1024
cal = bytes/tb
print(cal)

# converting bytes to KB,MB,GB,TB
bytes = 2
kb = 1024
mb = 1024*1024
gb = 1024*1024*1024
tb = 1024*1024*1024*1024
cal1 = bytes/kb
cal2 = bytes/mb
cal3 = bytes/gb
cal4 = bytes/tb
print(cal1,cal2,cal3,cal4)
