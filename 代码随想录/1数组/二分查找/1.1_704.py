#二分法 
#1.递归  40 ms	16.1 MB

class Solution:

    
    def search(self, nums: List[int], target: int) -> int:

        def f(nums,target,start,end):

            
            if start == end :
                return start if nums[start] == target else -1
            mid = (start + end) //2 


            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                ind = f(nums,target,start,mid)
            elif nums[mid] < target:
                ind = f(nums,target,mid+1,end)
            return ind
        n = len(nums)

        return f(nums,target,0,n-1)
    

#2.while循环 32 ms	16.1 MB
class Solution:

    
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while(left<=right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1 

        return -1

