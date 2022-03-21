x = input("enter list of numbers: ")
nums = x.split(" ")

for i in range(len(nums)):
    j = int(nums[i])
    if j < 0:
        nums = nums[0:i]
        break


nums = list(map(int, nums))

print (nums)

average = sum(nums)/len(nums)

print ("average:", average)

for i in nums:

    print("Distance from average:", i - average if i - average > 0 else average - i )