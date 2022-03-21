num1 = (input("Enter series of numbers: ")).split(" ")
num1 = list(map(int, num1))
print (num1)

num2 = (input("Enter 2nd series of numbers: ")).split(" ")
num2 = list(map(int, num2))
print (num2)

for i in (num2):
    if (not i in num1):
        print (i, "is not in first series")
    else:
        print (i, "is in first series")
