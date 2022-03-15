user = int(input("enter value here: "))
while (user < 0) or (user > 100):
    print ("Input is invalid")
    user = int(input("enter value here: "))
else:
    print ("Input is valid")

