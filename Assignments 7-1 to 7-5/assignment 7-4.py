import random

lst = []
n = 0

while n < 5:
    x = random.randint(0,99)
    lst.append(x)
    n += 1

lst.sort()
print (lst)


user = int(input("Enter number to insert: "))

lst.append(user)
lst.sort()
print (lst)


