# e.g 1

# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5


# i = 1 

# while i<=5:
#     j=1
#     while(j<=5):
#         print(j , end = ' ')
#         j = j + 1
#     print()
#     i = i+1



# e.g 2
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# i = 1 

# while i<=5:
#     j=1
#     while(j<=i):
#         print(j , end = ' ')
#         j = j + 1
#     print()
#     i = i+1


# alternate way to print the triangle

# i = 1 
# while i<=5:
#     print('*'*i)
#     i = i + 1



# pyramid shape


i = 1
n = 5  # number of rows
while i <= n:
    # print leading spaces
    j = n
    while j > i:
        print(" ", end=" ")
        j -= 1
    # print numbers in increasing order
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    # print numbers in decreasing order
    j = i - 1
    while j >= 1:
        print(j, end=" ")
        j -= 1
    print()
    i += 1
