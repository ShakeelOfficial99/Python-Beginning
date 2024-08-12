#Python Variables

#A-Z a-z 0-9 _ 


age = 20
name = 'Shakeel'


print(age)


#Case sensitive    small or capital latters  are not same 

Name = 'Haroon'


# Naming conventions 

# first_name  (Snake case)
# firstName  (camel case)
# FirstName  (Pascal case )


x = y = z = 10
print(z) # output:10 , same value in all the variables 

# one to one maping 
x,y,z = 100,200,300
print(y) #output : 200

# type of any variable 
float_type = 2.99
print(type(x)) # output : <class 'int'>
print(type(float_type)) # output : <class 'float'>


# Casting (change data type of one variable to another data type)
# Int to float
a = 10
print(float(a)) #output : 10.0

#Float to Int
y = 20.6878
print(int(y)) # output : 20

# Int to string
z = 10.87
t = str(z)
print(t) #output : 10
print(type(t)) # output:  <class 'str'>

# Delete variable from memory
del z 
print(z) #output : NameError: name 'z' is not defined