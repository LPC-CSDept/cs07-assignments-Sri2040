import random

lst1 = []
for i in range(10):
    lst1.append(random.randint(0,100))
print (lst1)

z = lst1.index(min(lst1))

lst1[z], lst1[0] = lst1[0], lst1[z]
print (lst1)

lst2 = lst1

x = lst2[0]
lst2.pop(0)

print (lst2)

y = lst2.index(min(lst2))
lst2[y], lst2[0] = lst2[0], lst2[y]
lst2.insert(0, x)
print (lst2)







