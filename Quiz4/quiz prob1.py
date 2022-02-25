import random


even = False

while True:
    num1 = random.randint(0,100)
    num2 = random.randint(0,100)
    print (num1, num2)
    if (num1 % 2 == 0) and (num2 % 2 == 0):
        even = True
        break
    
if even:
    print ("There are two consecutive even numbers:", num1, num2)



