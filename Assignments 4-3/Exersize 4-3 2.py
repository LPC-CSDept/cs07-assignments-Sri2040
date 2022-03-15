import random

while True:
    num = random.randint(1,100)
    print (num)
    user = input("Enter letter: ")
    if (user == "q"):
        print ("Loop end")
        break
