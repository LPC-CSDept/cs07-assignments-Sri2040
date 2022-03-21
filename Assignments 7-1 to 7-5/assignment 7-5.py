import random

lst = []

for i in range(20):
    x = random.randint(0,10)
    lst.append(x)

print (lst)
user = int(input("Enter number in list to delete: "))

i = 0
while (i < len(lst)):
    if(lst[i] == user):
        lst.remove(user)
    i+= 1
print(lst)