import random


even = False
num2 = 1
while True:
    num1 = random.randint(0,100)
    print (num1)
    if (num1 % 2 == 0) and (num2 % 2 == 0):
        even = True
        break
    num2=num1
if even:
    print ("There are two consecutive even numbers:", num2, num1)



