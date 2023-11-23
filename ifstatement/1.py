 #IF statement = a block of code that will execute if it's condition is true

# Age = int(input("How old are you: "))

# if Age == 100:
#     print("u are a older ")
# elif Age >= 18:
#     print("u are an adult")
# elif Age < 18:
#     print("U ARE A CHILD") 
# else:
#     print("be good ")      

marks = int(input("How Many Marks You Got :"))

if marks >= 90:
    print("Grade A")
elif marks > 80 and marks <=90:
    print("Grade B")
elif marks >=60 and marks <=80:
    print("Grade C")
elif marks <=60:
    print("Grade D")        