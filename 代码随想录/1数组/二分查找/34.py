#36 ms	16.5 MB
#j设置为负，那就应该是+
#第一种思路（自己想的）是定位相等值，前后找
#第二种思路是继续一下一下移动left和right，具体移动为：超右寻找时，把不停向右拓宽right的范围
#朝左寻找时，不停拓宽left范围

#第二种的思路精髓是：本题要解决的是，如果定位到nums[mid] = target,这个mid不能直接取，而是要朝右扩朝左扩，
#扩到!= target为止。
#精髓就在于，，求右边界时，夹逼的过程中，如果nums[mid] = target，就让right朝右扩，扩到不满足为止
#求左边界时，相反！
#主要求了左后，left和right值改变！

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                i = 0
                j = 0
                
                while (nums[i+mid]) == target:
                    i += 1
                    if  (i + mid) >= len(nums) :
                        break

                while (nums[mid+j]) == target: 
                    j -= 1
                    if ((mid + j) < 0):
                        break
                return [mid + j + 1  , mid + i - 1]
        return [-1,-1]
    
    


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def getRightBorder(nums:List[int], target:int) -> int:
            left, right = 0, len(nums)-1
            rightBoder = -2 # 记录一下rightBorder没有被赋值的情况
            while left <= right:
                middle = left + (right-left) // 2
                if nums[middle] > target:
                    right = middle - 1
                else: # 寻找右边界，nums[middle] == target的时候更新left
                    left = middle + 1
                    rightBoder = left
    
            return rightBoder
        
        def getLeftBorder(nums:List[int], target:int) -> int:
            left, right = 0, len(nums)-1 
            leftBoder = -2 # 记录一下leftBorder没有被赋值的情况
            while left <= right:
                middle = left + (right-left) // 2
                if nums[middle] >= target: #  寻找左边界，nums[middle] == target的时候更新right
                    right = middle - 1
                    leftBoder = right
                else:
                    left = middle + 1
            return leftBoder
        leftBoder = getLeftBorder(nums, target)
        rightBoder = getRightBorder(nums, target)
        # 情况一
        if leftBoder == -2 or rightBoder == -2: return [-1, -1]
        # 情况三
        if rightBoder -leftBoder >1: return [leftBoder + 1, rightBoder - 1]
        # 情况二
        return [-1, -1]