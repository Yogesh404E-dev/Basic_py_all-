# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

def my_function():
    print("Hello from a function")

my_function() #this calling function

#Arguments
# a passed information to the function required for proccess. You can pass number of argumentsfor one function
# using comma seprate values,

def my_info(faname,lname,job):
    print("First name:"+faname)
    print("Last name:"+lname)
    print("My job :"+job)

my_info("Yogesh","ss","Developer")

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
