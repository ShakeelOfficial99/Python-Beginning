#Python Data Type

#Number
#Boolean Type
#String
#Tuple
#Set
#Dictionary

# 1. Number
# There are three numeric types of python
    #int            e.g: age = 20 (data type of age is integer)
    #float          e.g: price = 34.33 
    #Complex
# e.g
a = 5 + 5j
print(a) # (5+5j) 


# 2. Boolean Type
#  True or False
x = True 
y = False

s = bool(10) 
print(s) # True 
#for 0, None , "" output is False 


# 3. String
state = "Hunza"
# for multiplelines 
address = """ AliBusiness Complex, 
Zulfiqarabad Gilgit """
print(address)

program = "Python Programming"

print(program[0]) #output: P
print(program[-1]) #output: g

#length of string
print(len(program)) #output : 18

print('thon' in program) #output: True

# slicing in string
like = 'I like you'
print(like[2:6]) #output: like (it start from index 2 and end at index 6 but last index is not included)
print(like[2:])  #output: like you
print(like[:2]) #output: I

#concat
a1 = 'cat'
a2 = 'dog'
a3 = a1 +' '+ a2
print(a3) #output : cat dog

#string format
#eg:
item = 'Apple'
qty = 2
price = 20
sf = 'I want {} kg {} for {} dollors'
print(sf.format(qty,item,price)) #output: I want 2 kg Apple for 20 dollors

#Escape Sequencing (to put single or double quotes in a string)

txt = "python is \"great\" language"
print(txt) #output : python is "great" language

# String Methods
ten = 'ten ten'
tenn = ten.split()
print(tenn)




# Logical Operatiors  and , or , not
x1 = 10
y1= 20
z1=30

print(x1<10 and y1>10 or y1<z1 and not(y1>z1))

# Identitly operatiors (is and is not)