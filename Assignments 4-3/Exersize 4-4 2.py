import random 

i = 1
sum = 0

while i < 10:
    rand = random.randint(0,100)
    i = i + 1
    sum = sum + rand
    print ("random value:", rand, "sum:", sum)
    if (sum > 100):
        print (sum)
        break
else: 
    if (sum <= 100):
        print ("total number of values reached")
        print ("sum:", sum)





