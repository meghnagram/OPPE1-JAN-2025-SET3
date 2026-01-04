


m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]

column_sums = [0] * n

for i in range(m):
    for j in range(n):
        column_sums[j] += matrix[i][j]

max_column_sum = max(column_sums)
max_sum_column_index = column_sums.index(max_column_sum)

print(max_sum_column_index)
print(max_column_sum)

# #AnotherMethod
# # Write your code here to read the input and print the output

# x,y=map(int,input().split())
# m=[]
# s=[]
# for i in range(x):
#     s=list(map(int,input().split()))
#     m.append(s)

# # print(m)

# max=0
# sum=0
# index=0

# for j in range(y):
#     for i in range(x):
#         sum=sum+m[i][j]
#     if sum>max:
#         max=sum
#         index=j
        
#     sum=0
    
# print (index)
# print (max)

# Max Column sum and Max column sum index
# Write a program to find the index of the column with the maximum sum of elements in a given m x n matrix. Find the 0-based index of the column that has the largest sum and the largest column sum.

# If more than two columns have the same sum, the output should be the index of the first column (with the smallest index) among those with the maximum sum.

# Input Format

# The first line contains two integers, m and n, the number of rows and columns in the matrix.
# The next m lines each contain n space-separated integers representing the elements of the matrix.
# Output Format

# The first line has a integer, the index of the column with the maximum sum.
# The second line has the maximum column sum.
# Example

# Input

# 3 4
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# Output

# 3
# 24

