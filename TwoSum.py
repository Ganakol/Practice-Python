def TwoSum(nums,target):
    if len(nums)<=0:
        print("In First If Statement!")
        return False
    dict1 = {}
    for i in range(len(nums)):
        if nums[i] in dict1:
            return [dict1[nums[i]], i]
            
        else:
            dict1[target-nums[i]] = i 
            
            
nums = [int(i) for i in input().split()]
target = int(input())
#print(nums)
print(TwoSum(nums,target))
