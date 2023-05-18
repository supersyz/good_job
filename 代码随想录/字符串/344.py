#双指针
#用while也可以


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if  len(s) <= 1:
            return s 
        r = len(s) - 1
        for l in range(len(s)//2 + 1):
            s[l],s[r] = s[r],s[l] 
            l += 1
            r -= 1
            if l >= r:
                break
        return s