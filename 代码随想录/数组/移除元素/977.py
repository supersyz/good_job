#思考：和普通排序的区别，是否利用了原来的非递减
#思考：是否需要新数组。

class Solution:
    
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >=0:
            return [i*i for i in nums]
        
        l,r = 0,len(nums) - 1
        if nums[r] <= 0:
            return [nums[i]*nums[i] for i in range(r,-1,-1)]

        new_ls = nums.copy()
        k = -1
        while(l<=r):
            if nums[l] * nums[l] <= nums[r] * nums[r]:
                new_ls[k] =  nums[r] * nums[r]
                r -= 1
                k -= 1
            else:
                new_ls[k] =  nums[l] * nums[l]
                l += 1
                k -= 1
        return new_ls