num1s = int(input("please enter the size of the first array: "))
num1 = []
for i in range(num1s):
    num1.append(int(input("Enter numbers in first array: ")))

num2s = int(input("please enter the size of the second array: "))
num2 = []
for i in range(num2s):
    num2.append(int(input("Enter numbers you want in second array: ")))

print ("First Array: ", (num1))
print ("Second Array: ", (num2))

ans = []
curr = num1 if len(num1) > len(num2) else num2

for i in range(len(curr)):
    try:
        ans.append(num1[i])
    except:
        pass
    try:
        ans.append(num2[i])
    except:
        pass
print("Shuffled Array: ", (ans))