key = input("Please enter the key: ")
list = []
for i in range(int(input("Please enter the length of the list: "))):
    list.append(input("Enter a string: "))
print(key in list)