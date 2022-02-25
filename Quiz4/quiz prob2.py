listcomplete = False
list1 = []
countp = 0
while True:
    userin = input("Enter words here: ")
    list1.append(userin)
    
    if (userin == "stop"):
        list1.remove("stop")
        listcomplete = True
        break
    elif "p" in (userin):
        countp = countp + 1

if listcomplete:
    p = " ".join(list1)
    print ("Given string: ", (p))
    print ("Number of times a word with 'p' appears: ", countp)


    