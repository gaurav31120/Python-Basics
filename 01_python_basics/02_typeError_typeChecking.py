# len(4837) # gives error

num_char = len(input("What is your name?"))  #input ----- gaurav
# print("Your name has " + num_char + "characters")  # will give error # TypeError: can only concatenate str (not "int") to str

# print(type(num_char)) # <class 'int'> -----# typechecking ----

new_num_char = str(num_char)
print(new_num_char)  # 6
print("Your name has " + new_num_char + " characters")  # Your name has 6 characters

a = 123
print(type(a)) # <class 'int'>

b = str(123)
print(type(b)) # <class 'str'>

c = float(123)
print(type(c)) # <class 'float'>

print(70 + float("100.5")) # 170.5
print(str(70) + str(100)) # 70100
