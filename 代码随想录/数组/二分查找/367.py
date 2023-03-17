#第一种二分法，是用于l和r不清晰时，可以求边界
#第二种是不管l和r，不用讨论特殊情况下l和r的值，比如此题就只判断是还是不是完全平方数，不需要进一步操作l和r


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r,ans = 0,num,-1
        while (l<=r):
            mid = (l+r) // 2
            if mid * mid <= num:
                l = mid + 1
                ans = mid
                
            else:
                r = mid - 1


        return True if ans != -1 and ans * ans == num else False
    
    
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r,ans = 0,num,None
        while (l<=r):
            mid = (l+r) // 2
            if mid * mid < num:
                l = mid + 1
            elif mid * mid > num:
                r = mid - 1
            else:
                return True
        return False