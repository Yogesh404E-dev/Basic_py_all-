# List -
#       you can store string, number, floating values,etc.
#       having similer to array but in advance 
#       sntax :-> list_name = [elements1,elements2,elements13...etc]

# Eg as follows

nums = [25,14,14,45,77, 98]
print(nums)

# O/p
# jarvis@Blackperl:~/Python/Basic_py_all-$ python3 List.py 
# [25, 14, 14, 45, 77, 98]

# if you want print with index value as follow

print('with index value ',nums[3])

#O/p
#with index value  45

# if you want user start postion to end  you can 

print('\nstart postion to end\n',nums[2:4])

#O/p
# start postion to end
#  [14, 45]
# Note :-> Yes you can provide negative index as well 


# Lets create anther with string list 
names = ['Yogesh','Abhi','Akash','praqtap','mandar']

print('\n Nmaes =: ',names)

#O/p
# Nmaes =:  ['Yogesh', 'Abhi', 'Akash', 'praqtap', 'mandar']

# list of list create combo of list or concanet list 

mil = [nums,names]
print('\n Combo =:',mil)

#O/p
#Combo =: [[25, 14, 14, 45, 77, 98], ['Yogesh', 'Abhi', 'Akash', 'praqtap', 'mandar']]
# you can use list leng,copy and many more function 
#mutable -> appending list num list 

nums.append(45)
print('\n after append :',nums)


#O/P
#after append : [25, 14, 14, 45, 77, 98, 45]
#Note -> You can use clear list using list.clear()
# Diiferance between append & insert 
#append -> append value to last 
# insert -> using index number as you want you can add element

nums.insert(2,27)
print('\n After inser 27 of 2 posiotion ',nums)

#O/p
#After inser 27 of 2 posiotion  [25, 14, 27, 14, 45, 77, 98, 45]
# Remove element -> removeing the element from list 

nums.remove(77)
print('\n After remove 77 from list ',nums)

#O/p 
#After remove 77 from list  [25, 14, 27, 14, 45, 98, 45]

# POP method is also user remove element with advance 

nums.pop(1)
print('\n pop element from 1 postion',nums)

#O/p
# pop element from 1 postion [25, 27, 14, 45, 98, 45]
# Note -> if you don't pass index for pop method it will remove last element.FIFO algo work here.
# NOte-> If you want delete multiple elements with index value you can 
# del nums([2])
# print(nums)
#
# Using extend method add multiple elemnts 

nums.extend([1,2.3])
print('\nAfter 1,2,3 extend method =:',nums)  

#O/p
#After 1,2,3 extend method =: [25, 27, 14, 45, 98, 45, 1, 2.3]

# her you can user max(),min(),sum() ..etc methods.
#red python doc for this end of session
