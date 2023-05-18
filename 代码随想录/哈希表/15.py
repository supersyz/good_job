#三数之和，先思考去重很麻烦，不能用哈希表法所以考虑清楚用双指针
##然后想清楚怎么去重，包括a的去重和b，c的去重



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
    
        ans = []
        flag = True
        l_tmp = -1e6
        r_tmp = 1e6
        i_tmp = -1e6
        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            if nums[i] > 0:
                break
            
            if (i >= 1 and nums[i] == nums[i-1]):
                continue
            while True:
               # print(nums)
                #print(i,l,r)

                if nums[i] + nums[l] + nums[r] == 0:
                    if (nums[l] == l_tmp and nums[i] == i_tmp) or (nums[l] == l and nums[r] == r_tmp) or (nums[r] == r_tmp  and nums[i] == i_tmp):
                        flag = False
                    else: 
                        flag = True
                    if flag:
                        ans.append([nums[i],nums[l],nums[r]])
                        i_tmp = nums[i]
                        l_tmp = nums[l]
                        r_tmp = nums[r]
                    l += 1
                    if l == r:
                        break
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1

                    if l == r:
                        break
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1

                    if l == r:
                        break
        return ans
            
            
            


##优化一下

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []
        flag = True
        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            if nums[i] > 0:
                break
            
            if (i >= 1 and nums[i] == nums[i-1]):
                continue
            while True:
                
               # print(nums)
                #print(i,l,r)
                sm = nums[i] + nums[l] + nums[r]
                if sm == 0:
                    if flag:
                        ans.append([nums[i],nums[l],nums[r]])
                    l += 1
                    flag = False
                elif sm < 0:
                    l += 1
                    flag = True
                elif sm > 0:
                    r -= 1
                    flag = True
                if l == r:
                    #考虑到上一轮最后就是append了，但是被置为false，下一轮的开始就得是true
                    flag = True
                    break
        return ans
            


##不要用flag，判断很混乱，考虑一下需要去重的情况，其实就是a要去重，然后a+b+c==0的时候要看看b后面和c前面，要去重，别的时候都不需要去重
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []

        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            if nums[i] > 0:
                break
            
            if (i >= 1 and nums[i] == nums[i-1]):
                continue
            while True:
                
               # print(nums)
                #print(i,l,r)
                sm = nums[i] + nums[l] + nums[r]
                if sm == 0:

                    ans.append([nums[i],nums[l],nums[r]])
                    while (l != r and nums[l] == nums[l + 1]): l += 1
                    while (l != r and nums[r] == nums[r - 1]): r -= 1
                    l += 1
                    r -= 1
                elif sm < 0:
                    l += 1

                elif sm > 0:
                    r -= 1

                if l >= r:

                    break
        return ans