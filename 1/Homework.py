#задание N3.1
matrix = [[1,2,3],[4,5,6],[7,8,9]]
a = 0
for i in range(3):
    for j in range(3,1,-1):
        a += matrix[i][j]
print(a)

#задание N4
matrix = [[1,2,3],[4,5,6],[7,8,9]]
c = int(input())
d = int(input())
a = 0
b = 0
for i in range(3):
    a += matrix[c][i]
for i in range(3):
    b += matrix[i][d]
print(a,b)