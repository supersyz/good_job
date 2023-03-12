def twoSum(nums, target):
    for a in nums:
        if (target - a) in nums:
            print(a,(target - a))
            return [nums.index(a),nums.index((target-a))] 


a = twoSum(nums = [3,2,4],target = 6)
print(a)
        
        