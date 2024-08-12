#Input and output


print('Hello world')


print('Hello Python 1', end = '=')
print('Hello Python 2', end = '=')
print('Hello Python 3')
print('Hello Python 4')

'''
output : 

Hello Python 1=Hello Python 2=Hello Python 3
Hello Python 4

'''
name =  'shakeel'
age = 12
print('my name is ', name , 'and my age is', age)

print(f"my name is {name} and my age is {age}") #formating 

# Input 

# name = input('Please type you Name: ' )
# print(f"your name is {name}")


num1 = input('please enter num1: ')
num2 = input('please enter num2: ')
result = int(num1) + int(num2)
print(f"sum of {num1} and {num2} is : {result}") #output : sum of 5 and 4 is : 9

