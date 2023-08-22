
class Solution:

    
    def searchInsert(self, nums: List[int], target: int) -> int:

        def f(nums,target,start,end):

            
            if start == end :
                if nums[start] >= target:
                    return start
                else:
                    return start + 1
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
    

##看特殊情况时到底return哪个，聚焦left==right时，然后进循环做判断
class Solution:

    
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while(left<=right):
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1 
            else:
                return mid
        # if left == right:
        #     mid = (left + right) // 2
        #     if nums[mid] >= target:
        #         return mid
        #     elif nums[mid] < target:
        #         return mid + 1
        # else:
        #     return left
        return right +1 