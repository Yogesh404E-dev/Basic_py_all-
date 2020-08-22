# Data types 
#     ->  None
#     -> numeric 
#     -> list 
#     -> tuple
#     -> set
#     -> string 
#     -> range 
#     -> dictionary (map)

# None -> in other programing luague having null in python its none , varibel not assign to any value 

# #numeric 
#  -> int -> store integer data
#  -> float -> store floating value 
#  -> complex -> complex number 
#  -> bool -> true fales value or 0 1 numberic 

# type consting or converting data type as follow

a = 4.6 
print('\n a=:',a)
b = int(a)
print('\n b =:',b)


com = complex(a,b)
print('\n complex =:',com)


#o/p
# a=: 4.6

#  b =: 4

#  complex =: (4.6+4j)


# List -> list cololect no of values or elements 

list = [4,34,34,5435,4454,45654]

print('\n list :=' ,list)

#O/P  list := [4, 34, 34, 5435, 4454, 45654]

#Tuple -> collection of same type of values or elements 

tuple = (2,234,434,3,45,4)

print('\ntuple =:',tuple)

#O/P tuple =: (2, 234, 434, 3, 45, 4)


# set  is collection of unique values or elements

a = {42,45,54,55,54,543,34,43} 

print('\n set =:',a)

#O/P set =: {34, 42, 43, 45, 54, 55, 543}

# string -> string is coolection of charachters but in python do't have char data type it also string 

str ="YOgesh"

print('\n string =:',str)

#O/P string =: YOgesh

# Range -> range is datatpe you get range from one number to anther number 

ra = range(10)

print('\n 0 to 10 range =:',ra)

#1 to 10 range =: range(0, 10)
# but  if you want print every number in range use following 


#ran =list(range(10))
# print('\Every no of range =:',ran) Here if you use ID it work its i file you need for loop


# Even no 1 to 10  
# print('\n Even no 1 to 10  =:',list(range(2,10,2)))

# dictionary (map) -> is unique ke value pair Every key have value key can't repeated value can repeated
# key may be numeric or string 
# Is similer to json 

dic = {'Yogesh':'Iphone SE','Abhi':'samsumng','Akash':'One pluse'}
print('\n Dictionry = :',dic)

#Dictionry = : {'Yogesh': 'Iphone SE', 'Abhi': 'samsumng', 'Akash': 'One pluse'}

keydic = dic.keys()
print('\n only key print =: ',keydic)

# O/p only key print =:  dict_keys(['Yogesh', 'Abhi', 'Akash'])

valuedic = dic.values()

print('\n only value print =: ',valuedic)

# o/p only value print =:  dict_values(['Iphone SE', 'samsumng', 'One pluse'])

