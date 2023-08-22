#笨办法，时间复杂度为O（n）

class Solution:
    def replaceSpace(self, s: str) -> str:
        ls_s = list(s)
        for i in range(len(ls_s)):
            if ls_s[i] == ' ':
                ls_s[i] = '%20'
                #print(ls_s)
        return ''.join(ls_s)
    
    
    
#其实很多数组填充类的问题，都可以先预先给数组扩容带填充后的大小，然后在从后向前进行操作
#把前面的搬到后面，如果遇到' '，就填充
class Solution:
    def replaceSpace(self, s: str) -> str:
        from collections import Counter
        cnt = Counter(s)
        nums = cnt[' ']
        exp_num = 2 * nums
        n = len(s)
        s = list(s)
        l = len(s) - 1
        s.extend([0]*exp_num)
        r = len(s) - 1
        while l < r:
            if s[l] == ' ':
                s[r-2:r+1] = '%20'
                r -= 3
                l -= 1
            else:
                s[r] = s[l]
                r -= 1
                l -= 1
        return ''.join(s)