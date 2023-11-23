# nested function call = fuction calss inside other function calls.
#                        innermost function calls are resolved first
#                        returned value is used as arguments for the next outer function

# num = input("Enter positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)

# print(num)

print(round(abs(float(input("Enter the positive number")))))