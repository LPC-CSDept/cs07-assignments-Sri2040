rnum = int(input("How many rows: "))
cnum = int(input("How many columns: "))

names = []
scores = []

for i in range(cnum):
    names.append(input("Enter name: "))
    scores.append([])
    for i in range(rnum):
        scores.append(int(input("Enter score for student: ")))

print (names, scores)



    
