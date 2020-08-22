# variables 
#     -> Assigne varibles for storing value may be integer,folat,string,etc
    


num = 5
# if you want adress of variabe you use ad()

print(id(num))

#o/p
#9752288 the o/p ma be change in you pc beacuse of its memory addres so its differnt 

# In python having same data of two or more variable point the same address not create seprate 
# space for every variable for same data

a = 10

print('\n id a =: ',id(a))

b = a

print('\n id b =: ',id(b))

k = 10 

print('\n id k =: ',id(k))

print('\n 10 id =:',id(10))

#o/P
#same addess 
#  id a =:  9752448

#  id b =:  9752448

#  id k =:  9752448

#  10 id =: 9752448

#Constant 

PI = 3.14

print('\n pi = ',PI)


PI =3.13

print('\n After changing pi constatn value =:',PI)



# pi =  3.14

# After changing pi constatn value =: 3.13

# here you can change the value of constatn 