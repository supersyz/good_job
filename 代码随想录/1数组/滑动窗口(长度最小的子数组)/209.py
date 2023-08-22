#第一种方法，sum(nums[a:b])操作很费时间，不要用，替换成sums = 0, 在循环中加减
#while和for的区别：




class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        fast,slow = 0,0
        lowest = len(nums) + 1
        while(fast<=len(nums)):
            if sum(nums[slow:fast]) < target:
                fast += 1
            else:
                slow += 1
                if fast - slow < lowest:
                    lowest = fast - slow + 1
        if lowest == len(nums) + 1:
            lowest = 0
        return lowest
        
                

###想清楚先做什么再做什么，是先判断还是先操作！！！
#少写多想
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        fast,slow = 0,0
        sums = 0
        lowest = len(nums) + 1

        while fast<len(nums):
            
            sums += nums[fast]

            while( sums >= target):
     
                if fast - slow + 1 < lowest:
                    lowest = fast - slow + 1
                sums -= nums[slow]
                slow += 1
            fast += 1
            
            

        if lowest == len(nums) + 1:
            lowest = 0
        return lowest