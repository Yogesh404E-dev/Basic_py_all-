# list -> is collection which ordered and changable.Allowed duplicate

mylist = ["Yogesh","satish","yash","abhi"]
print(mylist)

#Allowed duplicate
mylist = ["Yogesh","satish","yash","abhi","satish"]
print(mylist)

#lenght of list 

print(len(mylist))

# A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]
print(list1)

#type of list class 
print(type(list1))

# Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Access Items
# List items are indexed and you can access them by referring to the index number

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Note: The first item has index 0.

# If you want to access index from reverse order you use -1 this way 
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Range of list 
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


# Note: The search will start at index 2 (included) and end at index 5 (not included).
# Remember that the first item has index 0.


