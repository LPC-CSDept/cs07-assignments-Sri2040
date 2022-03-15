import random
greater = False

while True:
    num1 = random.randint(0,99)
    num2 = random.randint(0,99)
    print (num1, num2)
    if (num1 == num2):
        print (num1, num2)
    else:
        if (num2 > num1):
            break
        greater = True

if greater:
    print ("number 2 is greater than number 1")

