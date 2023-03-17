#注意left赋值为mid+1需要考虑此时left是否已经满足条件，right也一样
#第二种二分法更简单，注意每次把ans赋给mid*mid <= x的mid
#第三种为牛顿迭代法，随机取一个值，x0, x0-f(x0)/f'(x)可以得到更接近的根，原理可以画图看，把切线画出来。f(x) = x**2 - a

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x ==1:
            return x
        # elif x == 4:
        #     return 2
        
        left = 0
        right = x

        while(left < right - 1):
            mid = (left + right) // 2
            if mid*mid < x:
                left = mid + 1 if (mid + 1) * (mid + 1) < x else mid
            elif mid * mid > x:
                right = mid - 1 if (mid - 1) * (mid - 1) > x else mid
            else:

                return mid
        return left


class Solution:
    def mySqrt(self, x: int) -> int:
        l,r,ans = 0,x,-1
        while(l<=r):
            mid = (l+r) // 2
            if mid * mid <= x:
                l = mid + 1
                ans = mid
            else:
                r = mid - 1

        return ans


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        begin0 = x // 2

        for i in range(100):
            begin0 = begin0 - (begin0 * begin0 - x) / (2 * begin0)
        return int(begin0)
        