x = input("Enter input: ")
ans = x.split(" ")
print(ans)
for i in range(len(ans)):
    j = int(ans[i])
    if(j < 0):
        ans = ans[0:i]
        break
print(ans)

ans = list(map(int, ans))
print (ans)

ans.remove(min(ans))
ans.remove(max(ans))


sm = sum(ans)
print ("Sum of values excluding min and max: ", sm)

average = sm/len(ans)
print ("Average of values excluding min and max: ", average)
