# Logical Operators (and,or,not) = used to check if two are more conditional statements

# and operators

temp = int(input("what is temperature outside? :"))

if temp >= 0 and temp <= 30:
    print("the temperature is good:")
elif temp < 0 or temp >30:
    print("the temperature is bad today. ")

# about not operator
# "NOT" operator is performed if > True statement it gives False result.
#    ''          ''     ''       >  Flase statement it gives True statement.

temp = int(input("what is temperature outside? :"))

if not(temp >= 0 and temp <= 30):
    print("the temperature is good:")
elif not(temp < 0 or temp > 30):
    print("the temperature is bad today. ")
