#因为要判断nums[fast]和nums[fast+1]，所以会提前一格退出循环
#又由于最后一个数肯定不会跟它后面一个数相等，所以需要循环外再执行一次
#        nums[slow] = nums[fast]
#        slow += 1


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        n = len(nums)
        while fast < n-1:
            if nums[fast] != nums[fast+1]:
                nums[slow] = nums[fast]
                slow += 1
                
            

            fast += 1
        nums[slow] = nums[fast]
        slow += 1
        return slow