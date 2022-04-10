import random
rows = int(input("please enter the length of the matrix"))
cols = int(input("please enter the height of the matrix"))
matrix = []

for i in range(rows):
    matrix.append([])
    for j in range(cols):
        matrix[-1].append(random.randint(0,100))

print(matrix)
maxi = float("-inf")
for i, j in enumerate(matrix):
    if(sum(j) > maxi):
        maxi = i
print(maxi)
matrix = list(map(list, zip(*matrix)))
maxi = float("-inf")
for i, j in enumerate(matrix):
    if(sum(j) > maxi):
        maxi = i
print(maxi)