#四数之和，要搞清楚三数之和怎么搞的，四数就是在三数的基础珊多一层循环
##注意a的去重和三数之和一样
##b的去重要注意跟a有关，b是从a+1开始的，那么b的去重就是b >= a+1+1 and nums[b] == nums[b-1]


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        ans = []


        for a in range(n-3):
            
            if a >= 1 and nums[a] == nums[a-1]:
                continue

            for b in range(a+1,n-2):

                if b >= a+2 and nums[b] == nums[b-1]:
                    continue
                c = b + 1
                d = n - 1
                while True:
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        ans.append([nums[a],nums[b],nums[c],nums[d]])
                        while(c!=d and nums[c] == nums[c+1]): c += 1
                        while(c!=d and nums[d] == nums[d-1]): d -= 1

    
                        c += 1
                        d -= 1

                        print(a,b,c,d)
                    elif nums[a] + nums[b] + nums[c] + nums[d] > target:
                        d -= 1

                    elif nums[a] + nums[b] + nums[c] + nums[d] < target:
                        c += 1
 
                    if c >= d:
                        break

        return ans