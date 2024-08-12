'''
**Q1:**
1) Create a class called bank Account
2) Create constructor which takes two arguments owner, balance=0
3) Create method called deposit with 1 argument namely amount (to be deposit). 
The method would add new amount to the balance and print out new balance in the account

'''


# class Account():
#     def __init__(self,accountNo,name,balance):
#         self.accountNo = accountNo
#         self.name = name
#         self.balance = balance

#     def Deposit(self):
#         account_no = input('Enter your Account Number : \n')
#         amount_dep = int(input('Enter Amount to deposit : \n'))
        
#         if(account_no == '405996041'):
#             self.balance += amount_dep
#             return self.balance
#         else:
#             print('Invilid account Number')
        
    

# account_1 = Account("405996041",'S.Ahmad',1000)
# account_1.Deposit()


# print(f"Your new balace is : {account_1.balance}")


'''
**Q2:**

Write a Python class called Rectangle that has attributes 

length and width. Implement methods to calculate the area 

and perimeter of the rectangle.

$\text{Area} = \text{length}*\text{width}$

$\text{perimeter} = (\text{length}+\text{width})*2$

'''


class Rectangle():
    def __init__(self,length, width):
       
        self.length = length
        self.width = width

    def Area(self):
        return self.length * self.width

    def Perimeter(self):
        return  2 * (self.length + self.width)


print("---------Calculate Area and Perimeter of a Rectangle-------")
l = int(input('Pleae Enter Length :\n'))
w = int(input('Pleae Enter Width :\n'))


r1 = Rectangle(l,w)
print(f"The Area of Rectangle with Length : {r1.length} and width : {r1.width} is : {r1.Area()}")

print(f"The Perimeter of Rectangle with Length : {r1.length} and width : {r1.width} is : {r1.Perimeter()}")




