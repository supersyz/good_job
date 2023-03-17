


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