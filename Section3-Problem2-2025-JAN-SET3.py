

n = int(input())
for i in range(1,n+1):
    zeros = " ".join("0"*i)
    print(" "*(n-i)+zeros)

# #AnotherMethod:

# n=int(input())
# space=n-1
# c=1

# for i in range(n):
#     print(' '*space,end='')
#     for j in range(c):
#         if j==i:
#             print('0')
#         else:
#             print('0 ',end='')
#     c +=1
#     space -=1


# Pattern printing - Centered Triangle Of Zeroes
# Print a centered triangle up to a given number of rows, where all elements are zeroes. The number of rows is taken as input.

# There is space between zeros in a same line and also no space after the last zero in a line.

# NOTE: This is an I/O type question, you need to write the whole code for taking input and printing the output.

# Input Format

# A single integer n, representing the number of rows in the pattern.
# Output Format

# A centered triangle having n number of rows, where all elements are zeroes
# Examples

# Input:

# 3
# Output:

#   0
#  0 0
# 0 0 0
# Input:

# 2
# Output:

#  0
# 0 0
# Input:

# 4
# Output:

#    0
#   0 0
#  0 0 0
0 0 0 0
